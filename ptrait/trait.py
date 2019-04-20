import functools

from ptrait.exceptions import NamedParamsNotExist, MethodDefinitionError
from itertools import groupby, chain
from types import MethodType


class TraitExtends():
    traitmark = "__traitmark__"

    @classmethod
    def mark(cls, target_method):
        setattr(target_method, cls.traitmark, True)
        return target_method

    @classmethod
    def check_params(cls, _func=None, *, param_names):
        def check_params_decorator(func):
            @functools.wraps(func)
            def wrapper_check_params(*args, **kwargs):
                param_names_not_exist = [
                    x for x in param_names if x not in kwargs]
                if param_names_not_exist:
                    raise NamedParamsNotExist(
                        "Param names(%s) not exists" % ", ".join(param_names_not_exist))
                return func(*args, **kwargs)
            return wrapper_check_params
        if _func is None:
            return check_params_decorator
        return check_params_decorator(_func)

    @classmethod
    def override(cls, *traits):
        def define_decorator(target_cls):
            for tr in traits:
                for elem_name in dir(tr):
                    elem = getattr(tr, elem_name, None)
                    if getattr(elem, cls.traitmark, False):
                        setattr(target_cls, elem_name, elem)
            return target_cls
        return define_decorator

    @classmethod
    def _cas_method_define(cls, ename, method_dict):
        # for subname in dir(method_dict[ename][0][1]):
        #    print(subname, getattr(method_dict[ename][0][1], subname))

        @cls.mark
        def new_method(*args, **kwargs):
            for fname, tmethod, trait_cls in method_dict[ename]:
                args, kwargs = tmethod(*args, **kwargs)
                # todo Is there any need to process return value of tmethod
                return args, kwargs
        return new_method

    @classmethod
    def cascade(cls, *traits):
        """check all traits and merge traits and call sequentially
        """
        def define_decorator(target_cls):

            method_dict = dict([(y[0], tuple(y[1])) for y in groupby(
                sorted([x for x in chain(
                        *[[(elem_name, getattr(tr, elem_name), tr)
                           for elem_name in dir(tr)]
                            for tr in traits])
                        if getattr(x[1], cls.traitmark, False)], key=lambda x: x[0]),
                key=lambda x: x[0])])
            for ename in method_dict.keys():
                if getattr(target_cls, ename, None) is not None:
                    raise MethodDefinitionError(
                        f"Method definition({ename}) in class {target_cls.__name__} "
                        "have to be deleted")
                setattr(target_cls, ename, MethodType(
                    cls._cas_method_define(ename, method_dict), target_cls))
            return target_cls
        return define_decorator

from ptrait import TraitExtends
import copy
from pytest_assertutil import assert_equal


class IntfA:

    @classmethod
    @TraitExtends.mark
    def a_classmethodA(cls, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 1
        return args, kwa

    @classmethod
    @TraitExtends.mark
    def a_classmethodC(cls, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa

    @staticmethod
    @TraitExtends.mark
    def a_staticmethodA(*args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 1
        return args, kwa

    @staticmethod
    @TraitExtends.mark
    def a_staticmethodC(*args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa

    @TraitExtends.mark
    def a_instancemethodA(self, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 1
        return args, kwa

    @TraitExtends.mark
    def a_instancemethodC(self, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa


class IntfB:

    @classmethod
    @TraitExtends.mark
    def a_classmethodB(cls, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 2
        return args, kwa

    @classmethod
    @TraitExtends.mark
    def a_classmethodC(cls, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa

    @staticmethod
    @TraitExtends.mark
    def a_staticmethodB(*args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 2
        return args, kwa

    @staticmethod
    @TraitExtends.mark
    def a_staticmethodC(*args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa

    @TraitExtends.mark
    def a_instancemethodB(self, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 2
        return args, kwa

    @TraitExtends.mark
    def a_instancemethodC(self, *args, **kwargs):
        kwa = copy.deepcopy(kwargs)
        kwa['a'] = kwargs.get('a', 0) + 3
        return args, kwa


@TraitExtends.cascade(IntfA, IntfB)
class A:
    pass


def test_cascade_call_instanceA():
    assert_equal(
        ((), {'a': 1}),
        A().a_instancemethodA()
    )


def test_cascade_call_instanceB():
    assert_equal(
        ((), {'a': 2}),
        A().a_instancemethodB()
    )


def test_cascade_call_instanceC():
    assert_equal(
        ((), {'a': 3}),
        A().a_instancemethodC()
    )


def test_cascade_call_staticmethodA():
    assert_equal(
        ((), {'a': 1}),
        A.a_staticmethodA()
    )


def test_cascade_call_staticmethodB():
    assert_equal(
        ((), {'a': 2}),
        A.a_staticmethodB()
    )


def test_cascade_call_staticmethodC():
    assert_equal(
        ((), {'a': 3}),
        A.a_staticmethodC()
    )


def test_cascade_call_classmethodA():
    assert_equal(
        ((), {'a': 1}),
        A.a_classmethodA()
    )


def test_cascade_call_classmethodB():
    assert_equal(
        ((), {'a': 2}),
        A.a_classmethodB()
    )


def test_cascade_call_classmethodC():
    assert_equal(
        ((), {'a': 3}),
        A.a_classmethodC()
    )

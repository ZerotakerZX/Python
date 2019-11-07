import unittest
from nose.tools import assert_equal, assert_false, assert_true
from operators import task47, task410, task411, task416a, task416b


class TestOperators(unittest.TestCase):
    def test_task47(self):
        a = 1
        b = 2
        result_min, result_max = task47(a, b)
        assert_equal(result_min, a)
        assert_equal(result_max, b)

        a = 3
        b = 4
        result_min, result_max = task47(a, b)
        assert_equal(result_min, a)
        assert_equal(result_max, b)

        a = 2
        b = 1
        result_min, result_max = task47(a, b)
        assert_equal(result_min, b)
        assert_equal(result_max, a)

    def test_task410(self): #тест на круг
        a = 2
        b = 2
        result = task410(a, b)
        assert_equal(result, 'circle')

    def test_task410(self): #тест на квадарт
        a = 1
        b = 2
        result = task410(a, b)
        assert_equal(result, 'square')

    def test_task411(self): #тест на A
        a = tuple([2, 2])
        b = tuple([4, 2])
        result = task411(a, b)
        assert_equal(result, a)

    def test_task411(self): #тест на B
        a = tuple([4, 2])
        b = tuple([2, 2])
        result = task411(a, b)
        assert_equal(result, b)

    def test_task416a(self): #круг влезает в квадрат
        a = 2
        b = 20
        result = task416a(a, b)
        assert_true(result)

        a = 20 #круг НЕ влезает в квадрат
        b = 2
        result = task416a(a, b)
        assert_false(result)

    def test_task416b(self): #квадрат влезает в круг
        a = 2
        b = 20
        result = task416a(a, b)
        assert_true(result)

        a = 20 #квадрат НЕ влезает в круг
        b = 2
        result = task416a(a, b)
        assert_false(result)

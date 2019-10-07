import unittest
from nose.tools import assert_true, assert_false
from ifs import solution327a, solution327b, solution327z, solution328b, solution328g, solution330b, solution332a, solution332e, solution332b, solution332c, solution332d, solution332f, solution332g, solution332z


class TestEquationa(unittest.TestCase):
    def test_equationiftrue327a(self):
        x = 3
        y = 4
        result = solution327a(x, y)
        assert_true(result)

    def test_equationiffalse327a(self):
        x = 2
        y = 4
        result = solution327a(x, y)
        assert_false(result)

        x = 3
        y = 3
        result = solution327a(x, y)
        assert_false(result)

        x = 2
        y = 3
        result = solution327a(x, y)
        assert_false(result)

    def test_equationiftrue327b(self):  # тест на правильность обоих
        x = 2
        y = -1
        result = solution327b(x, y)
        assert_true(result)

        x = 2  # тест на правильность x
        y = -10
        result = solution327b(x, y)
        assert_true(result)

        x = 0  # тест на неправильность y
        y = -1
        result = solution327b(x, y)
        assert_true(result)

    def test_equationiffalse327b(self):
        x = -10  # тест на неправильность обоих
        y = -10
        result = solution327b(x, y)
        assert_false(result)

    def test_equationiftrue327z(self):  # тест на правильность x
        x = 20
        result = solution327z(x)
        assert_true(result)

    def test_equationiffalse327z(self):
        x = 200  # x неверен и больше 20
        result = solution327z(x)
        assert_false(result)

        x = 10  # x неверен и меньше  10
        result = solution327z(x)
        assert_false(result)

    def test_equationiftrue328b(self):
        a = 2
        b = 3
        result = solution328b(a, b)
        assert_true(result)

        a = 3
        b = 3
        result = solution328b(a, b)
        assert_false(result)

        a = 2
        b = 2
        result = solution328b(a, b)
        assert_false(result)

        a = 3
        b = 2
        result = solution328b(a, b)
        assert_true(result)

    def test_equationiftrue328g(self):
        a = 3
        b = 6
        c = 9
        result = solution328g(a, b, c)
        assert_true(result)

        a = 4
        b = 6
        c = 9
        result = solution328g(a, b, c)
        assert_false(result)

    def test_equationiftrue330b(self):
        a = 20
        result = solution330b(a)
        assert_true(result)

        a = 21
        result = solution330b(a)
        assert_false(result)

    def test_equationiftrue332a(self):
        x = -2  # тест на правильность
        y = 1
        result = solution332a(x, y)
        assert_true(result)

        x = 1  # тест на неправильность
        y = 0
        result = solution332a(x, y)
        assert_false(result)

    def test_equationiftrue332b(self):
        x = 666  # тест на правильность
        y = 1.5
        result = solution332b(x, y)
        assert_true(result)

        x = 666  # тест на неправильност
        y = 1.6
        result = solution332b(x, y)
        assert_false(result)

    def test_equationiftrue332c(self):
        x = 2  # тест на правильность
        y = 4
        result = solution332c(x, y)
        assert_true(result)

        x = 4  # тест на неправильность
        y = 6
        result = solution332c(x, y)
        assert_false(result)

    def test_equationiftrue332d(self):
        x = 666  # тест на правильность
        y = 4
        result = solution332d(x, y)
        assert_true(result)

        x = 0  # тест на неправильность
        y = 4
        result = solution332d(x, y)
        assert_false(result)

    def test_equationiftrue332e(self):
        x = 1  # 1 тест на правильность
        y = -1
        result = solution332e(x, y)
        assert_true(result)

        x = 0  # 1 тест на неправильность
        y = 4
        result = solution332e(x, y)
        assert_false(result)

        x = 2  # 2 тест на правильность
        y = 1
        result = solution332e(x, y)
        assert_true(result)

        x = 0  # 2 тест на неправильность
        y = 4
        result = solution332e(x, y)
        assert_false(result)

    def test_equationiftrue332f(self):
        x = 2  # 1 тест на правильность
        y = 1
        result = solution332f(x, y)
        assert_true(result)

        x = 0  # 1 тест на неправильность
        y = 4
        result = solution332f(x, y)
        assert_false(result)

        x = 2  # 2 тест на правильность
        y = -1.5
        result = solution332f(x, y)
        assert_true(result)

        x = 0  # 2 тест на неправильность
        y = 4
        result = solution332f(x, y)
        assert_false(result)

    def test_equationiftrue332g(self):
        x = 1  # тест на правильность
        y = -1
        result = solution332g(x, y)
        assert_true(result)

        x = 0  # тест на неправильность
        y = 4
        result = solution332g(x, y)
        assert_false(result)

    def test_equationiftrue332z(self):
        x = 0  # 1 тест на правильность
        y = 0.5
        result = solution332z(x, y)
        assert_true(result)

        x = 0  # 1 тест на неправильность
        y = 4
        result = solution332z(x, y)
        assert_false(result)

        x = 2  # 2 тест на правильность
        y = 0
        result = solution332z(x, y)
        assert_true(result)

        x = 0  # 2 тест на неправильность
        y = 4
        result = solution332z(x, y)
        assert_false(result)
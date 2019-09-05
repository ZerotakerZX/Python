import unittest
from calculator import add, multiplication, devide, subtract, chain


class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        first = 1
        second = 2
        expected = 3
        result = add(first, second)
        assert expected == result

    def test_calculator2(self):
        first = 2
        second = 2
        expected = 4
        result = add(first, second)
        assert expected == result

    def test_calculator3(self):
        first = 2
        second = 2
        expected = 4
        result = multiplication(first, second)
        assert expected == result

    def test_caclulator4(self):
        first = 3
        second = 3
        expected = 9
        result = multiplication(first, second)
        assert expected == result

    def test_caclulator5(self):
        first = 10
        second = 2
        expected = 5
        result = devide(first, second)
        assert expected == result

    # TODO: write check on devided by zero
    def test_caclulator6(self):
        first = 20
        second = 2
        expected = 10
        result = devide(first, second)
        assert expected == result

    def test_caclulator7(self):
        first = 2
        second = 2
        expected = 0
        result = subtract(first, second)
        assert expected == result

    def test_calculator8(self):
        first = 2
        second = 3
        third = 3
        expected = 11
        result = chain(first, second, third)
        assert expected == result
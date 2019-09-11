import unittest
from nose.tools import assert_equal
from highlightnumbers import find_second_digit, find_first_digit, find_prod, swap_digits, swap_digits_alt, slice_number_singular, arbitrary_shuffle, arbitrary_double_shuffle, sum_and_prod


class TestHnumbers(unittest.TestCase):
    def test_find_first_digit(self):
        digit = 45
        expected_result = 4
        result = find_first_digit(digit)
        assert_equal(result, expected_result)


    def test_find_second_digit(self):
        digit = 45
        expected_result = 5
        result = find_second_digit(digit)
        assert_equal(result, expected_result)


    def test_find_prod(self):
        digit = 45
        expected_result = 20
        result = find_prod(digit)
        assert_equal(result, expected_result)


    def test_swap_digits(self):
        digit = 92
        expected_result = 29
        result = swap_digits(digit)
        assert_equal(result, expected_result)

    def test_slice_number_singular(self):
        digit = 123
        expected_result = 3
        result = slice_number_singular(digit)
        assert_equal(result, expected_result)

    def test_arbitrary_shuffle(self):#2.14
        digit = 123
        expected_result = 231
        result = arbitrary_shuffle(digit)
        assert_equal(result, expected_result)

    def test_arbitrary_double_shuffle(self):#2.17
        digit = 123
        expected_result = 132
        result = arbitrary_double_shuffle(digit)
        assert_equal(result, expected_result)
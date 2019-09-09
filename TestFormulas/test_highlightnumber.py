import unittest
from highlightnumbers import find_second_digit, find_first_digit, find_prod


class TestHnumbers(unittest.TestCase):
    def test_find_first_digit(self):
        digit = 45
        expected_result = 4
        result = find_first_digit(digit)
        assert expected_result == result


    def test_find_second_digit(self):
        digit = 45
        expected_result = 5
        result = find_second_digit(digit)
        assert expected_result == result


    def test_find_prod(self):
        digit = 45
        expected_result = 20
        result = find_prod(digit)
        assert result == expected_result
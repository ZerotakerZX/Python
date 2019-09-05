import unittest
from findx import square


class TestFindx(unittest.TestCase):
    def test_1stage(self):
        # y=7x**2 -3x+6
        x = 1
        result = square(x)
        expected_result = 10
        assert result == expected_result

    def test_2stage(self):
        # y=7x**2 -3x+6
        x = 0
        result = square(x)
        expected_result = 6
        assert result == expected_result
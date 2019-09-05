import unittest
from finda import square


class TestFindx(unittest.TestCase):
    def test_1stage(self):
        # x=12a**2+7a-16
        a = 0
        result = square(a)
        expected_result = -16
        assert result == expected_result

    def test_2stage(self):
        # x=12a**2+7a-16
        a = 1
        result = square(a)
        expected_result = 3
        assert result == expected_result
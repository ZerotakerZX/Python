import unittest

from sidesquare import findperimetr

class TestOne(unittest.TestCase):
    def test_one(self):
        sidesquare = 1
        result = findperimetr(sidesquare)
        expected_result = 4
        assert result == expected_result
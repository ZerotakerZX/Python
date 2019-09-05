import unittest

from circle import finddiametr

class TestCircle(unittest.TestCase):
    def test_radius(self):
        radius = 1
        result = finddiametr(radius)
        expected_result = 2
        assert  result == expected_result
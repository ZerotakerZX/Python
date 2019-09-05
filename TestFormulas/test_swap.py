import unittest

from swap import swapab


class TestSwap(unittest.TestCase):
    def test_swap(self):
        a = 1
        b = 2
        result_a, result_b = swapab(a, b)
        expected_result_a, expected_result_b = 2, 1
        assert result_a == expected_result_a
        assert result_b == expected_result_b
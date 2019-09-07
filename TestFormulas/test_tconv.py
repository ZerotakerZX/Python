import unittest
from tconv import tconverter


class TestTconvert(unittest.TestCase):
    def test_tconverter(self):
        f = 0
        k = 0
        c = 10
        result_f, result_k, result_c = tconverter(f, k, c)
        expected_result_f, expected_result_k, expected_result_c = 50, 283.15, 10
        assert result_f == expected_result_f
        assert result_k == expected_result_k
        assert result_c == expected_result_c

import unittest
from nose.tools import assert_equal
from number_operation import sum_all, prod_all

class TestNumbers_operation(unittest.TestCase):
    def test_sum_all_and_prod_all(self): #2.19 a/b
        digit = 1234
        expected_result_sum_all = 10
        expected_result_prod_all = 24
        result_sum_all = sum_all(digit)
        result_prod_all = prod_all(digit)
        assert_equal(result_sum_all, expected_result_sum_all)
        assert_equal(result_prod_all, expected_result_prod_all)
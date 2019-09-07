import unittest
from age import findage


class TestTconvert(unittest.TestCase):
    def test_findavg(self):
        tania = 4
        mitia = 2
        avgage = 0
        taniadif = 0
        mitiadif = 0
        result_avgage, result_mitiadif, result_taniadif = findage(tania, mitia)
        expected_result_avgage, expected_result_taniadif, expected_result_mitiadif = 3, -1, 1
        assert result_avgage == expected_result_avgage
        assert result_taniadif == expected_result_taniadif
        assert result_mitiadif == expected_result_mitiadif
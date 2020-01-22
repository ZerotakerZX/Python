import unittest
from nose.tools import assert_equal, assert_false, assert_true, assert_list_equal
from operators import task528a, task527a, task515, task59, task53b, task53a, task47, task410, task411, task416a, task416b, task423a, task427, task431a, task431b, task436, task464, task465, task466, task467, task469, task4100, task4100b, task4103, task4103b, task4104, task510


class TestOperators(unittest.TestCase):
    def test_task47(self):
        a = 1
        b = 2
        result_min, result_max = task47(a, b)
        assert_equal(result_min, a)
        assert_equal(result_max, b)

        a = 3
        b = 4
        result_min, result_max = task47(a, b)
        assert_equal(result_min, a)
        assert_equal(result_max, b)

        a = 2
        b = 1
        result_min, result_max = task47(a, b)
        assert_equal(result_min, b)
        assert_equal(result_max, a)

    def test_task410(self): #тест на круг
        a = 2
        b = 2
        result = task410(a, b)
        assert_equal(result, 'circle')

    def test_task410(self): #тест на квадарт
        a = 1
        b = 2
        result = task410(a, b)
        assert_equal(result, 'square')

    def test_task411(self): #тест на A
        a = tuple([2, 2])
        b = tuple([4, 2])
        result = task411(a, b)
        assert_equal(result, a)

    def test_task411(self): #тест на B
        a = tuple([4, 2])
        b = tuple([2, 2])
        result = task411(a, b)
        assert_equal(result, b)

    def test_task416a(self): #круг влезает в квадрат
        a = 2
        b = 20
        result = task416a(a, b)
        assert_true(result)

        a = 20 #круг НЕ влезает в квадрат
        b = 2
        result = task416a(a, b)
        assert_false(result)

    def test_task416b(self): #квадрат влезает в круг
        a = 2
        b = 20
        result = task416a(a, b)
        assert_true(result)

        a = 20 #квадрат НЕ влезает в круг
        b = 2
        result = task416a(a, b)
        assert_false(result)

    def test_task423a(self):
        number = 12 #проверка на большую ВТОРУЮ цифру
        result = task423a(number)
        expected_result = 2
        assert_equal(result, expected_result)

        number = 21  # проверка на большую ПЕРВУЮ цифру
        result = task423a(number)
        expected_result = 2
        assert_equal(result, expected_result)

        number = 33  # проверка на одинаковость
        result = task423a(number)
        assert_equal(result, 3)

    def test_task427(self):
        number = 121
        result = task427(number)
        assert_true(result, "polyndrome test")

        number = 321
        result = task427(number)
        assert_false(result, "failed polyndrome test")

    def test_task431a(self):
        number = 111
        result = task431a(number)
        assert_true(result, "all-same test")

        number = 121
        result = task431a(number)
        assert_false(result, "failed all-same test")

    def test_task431b(self):
        number = 211
        result = task431b(number)
        assert_true(result, "any-same test")

        number = 112
        result = task431b(number)
        assert_true(result, "any-same test")

        number = 121
        result = task431b(number)
        assert_true(result, "any-same test")

        number = 123
        result = task431b(number)
        assert_false(result, "failed any-same test")

    def test_task436(self):
        minute = 1
        green = 3
        red = 2
        color = task436(minute, green, red)
        expected_color = 'green'
        assert_equal(color, expected_color)

        minute = 4
        color = task436(minute, green, red)
        expected_color = 'red'
        assert_equal(color, expected_color)

        minute = 6
        color = task436(minute, green, red)
        expected_color = 'green'
        assert_equal(color, expected_color)

        minute = 8
        color = task436(minute, green, red)
        expected_color = 'red'
        assert_equal(color, expected_color)

        minute = 4
        green = 5
        red = 2
        color = task436(minute, green, red)
        expected_color = 'green'
        assert_equal(color, expected_color)

    def test_task465(self):
        """
        year = 2004
        result = task465(year)
        assert_true(result)

        year = 1900
        result = task465(year)
        assert_false(result)
        """

        year = 2019
        result = task465(year)
        assert_false(result)

        year = 2020
        result = task465(year)
        assert_true(result)

        year = 1900
        result = task465(year)
        assert_false(result)

        year = 2000
        result = task465(year)
        assert_true(result)

        year = 1600
        result = task465(year)
        assert_true(result)

    def test_task464(self):
        number = 333072
        result = task464(number)
        assert_true(result)

        number = 111111
        result = task464(number)
        assert_true(result)

        number = 111222
        result = task464(number)
        assert_false(result)

        number = 1000000
        result = task464(number)
        assert_false(result)

    def test_task466(self):
        a = 20
        b = 10
        c = 3
        d = 2
        e = 1
        result = task466(a, b, c, d, e)
        expected_result = ('upward_position')
        assert_equal(result, expected_result) #тест на нормальную кость

        a = 20
        b = 10
        c = 1
        d = 2
        e = 3
        result = task466(a, b, c, d, e)
        expected_result = ('normal_position')
        assert_equal(result, expected_result) #тест слишком толстую кость

        a = 20
        b = 10
        c = 1
        d = 3
        e = 2
        result = task466(a, b, c, d, e)
        expected_result = ('side_position')
        assert_equal(result, expected_result) #тест слишком широкую кость

    def test_task467(self):
        k = 1
        result = task467(k)
        expected_result = ('work')
        assert_equal(result, expected_result)  #тест на рабочий день

    def test_task469(self):
        first_hor_lenght = 1 #параметры первого прямоугольника
        first_ver_lenght = 1
        first_angle_coordinat_hor = 0
        first_angle_coordinat_ver = 0
        second_hor_lenght = 2 #параметры второго прямоугольника
        second_ver_lenght = 2
        second_angle_coordinat_hor = 0
        second_angle_coordinat_ver = 0
        result = task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_angle_coordinat_hor, first_angle_coordinat_ver, second_angle_coordinat_hor, second_angle_coordinat_ver)
        expected_result = ("второй принадлежит первому")
        assert_equal(result, expected_result)  #тест на все точки первого принадлежат второму

        first_hor_lenght = 10 #параметры первого прямоугольника
        first_ver_lenght = 10
        first_hor_start = 0
        first_ver_start = 0
        second_hor_lenght = 2 #параметры второго прямоугольника
        second_ver_lenght = 2
        second_ver_start = 0
        second_hor_start = 0
        result = task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start, second_ver_start, second_hor_start)
        expected_result = ("первый принадлежит второму")
        assert_equal(result, expected_result)  #тест на все точки второй принадлежит первому.

        first_hor_lenght = 10 #параметры первого прямоугольника
        first_ver_lenght = 10
        first_hor_start = 10
        first_ver_start = 10
        second_hor_lenght = 2 #параметры второго прямоугольника
        second_ver_lenght = 2
        second_ver_start = 0
        second_hor_start = 0
        result = task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start, second_ver_start, second_hor_start)
        expected_result = ("не пересекаются")
        assert_equal(result, expected_result)  #тест что не пересекаются

        first_hor_lenght = 1 #параметры первого прямоугольника
        first_ver_lenght = 2
        first_hor_start = 0
        first_ver_start = 0
        second_hor_lenght = 2 #параметры второго прямоугольника
        second_ver_lenght = 1
        second_ver_start = 0
        second_hor_start = 0
        result = task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start, second_ver_start, second_hor_start)
        expected_result = ("пересекаются частично")
        assert_equal(result, expected_result)  #тест что пересекаются частично

    def test_task4100(self):
        first = 1
        second = 2
        third = 3
        result = task4100(first, second, third)
        expected_result = 2
        assert_equal(result, expected_result)  #тест на 1*2=2

    def test_task4100(self):
        first = 6
        second = 5
        third = 4
        result = task4100(first, second, third)
        expected_result = 20
        assert_equal(result, expected_result)  #тест на 4*5=20

    def test_task4100b(self):
        first = 3
        second = 2
        third = 10
        result = task4100b(first, second, third)
        expected_result = 6
        assert_equal(result, expected_result)

    def test_task4103(self):
        first = 1
        second = 2
        third = 3
        result = task4103(first, second, third)
        expected_result = 3 #наибольшее
        assert_equal(result, expected_result)

    def test_task4103b(self):
        first = 1
        second = 2
        third = 3
        result = task4103b(first, second, third)
        expected_result = 1 #наименьшее
        assert_equal(result, expected_result)

    def test_task4104(self):
        day = 8
        result = task4104(day)
        expected_result = 'много'
        assert_equal(result, expected_result)

    def test_task53a(self):
        expected_result = [20, 21, 22, 23, 24, 25]
        result = task53a(20, 26, 1)
        assert_list_equal(expected_result, result)
        expected_result = [25, 26, 27, 28, 29, 30]
        result = task53a(25, 31, 1)
        assert_list_equal(expected_result, result)

        expected_result = [20, 22, 24, 26, 28, 30]
        result = task53a(20, 31, 2)
        assert_list_equal(expected_result, result)

    def test_task53b(self):
        expected_result = [4, 9, 16, 25]
        result = task53b(2, 6, 1)
        assert_list_equal(expected_result, result)

        expected_result = [4, 9, 16]
        result = task53b(2, 5, 1)
        assert_list_equal(expected_result, result)

    def test_task59(self):
        expected_result = [25.0, 27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 55.0] #дюйм = ~2.5см
        result = task59(10, 23, 1)
        assert_list_equal(expected_result, result)

        expected_result = [27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 55.0] #дюйм = ~2.5см
        result = task59(11, 23, 1)
        assert_list_equal(expected_result, result)

    def test_task510(self):
        expected_result = [0, 60, 120, 180] #от нуля до трёх баксов
        result = task510(60) #старт, финиш, текущий курс
        assert_list_equal(expected_result, result)

    def test_task515(self):
        expected_result = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63] #результаты умножения на 7
        result = task515(10) #до скольки прописать таблицу
        assert_list_equal(expected_result, result)

    def test_task527a(self):
        expected_result = 5050 #сумма всех чисел от 1 до 100
        result = task527a(101) #до скольки считать
        assert_equal(expected_result, result)

    def test_task528a(self):
        expected_result = 259459200 #произведение всех чисел от 8 до 15
        result = task528a(8, 15) #от/до скольки умножать
        assert_equal(expected_result, result)
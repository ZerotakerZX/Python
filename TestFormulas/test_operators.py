import unittest
from nose.tools import assert_equal, assert_false, assert_true, assert_list_equal
from operators import task614, task9185, task9108b, task9187, task9114, task991, task9184b, task9184, task9115, task9158, task9157, task9155, task9156, task9153, task9109b, task9112, task9111, task9111b, task992, task9103, task9106, task9105, task9107, task9104, task993, task9102, task989, task9101, task9100, task92, task832, task976b, task975a, task836, task835, task829, task825, task6108, task686, task6105, task653, task677, task669, task666, task657, task661, task660, task658, task656, task655, task654, task643, task651, task643b, task628a, task633, task632, task631, task630, task628b, task622d, task622e, task622g, task619, task617, task616, task61b, task613, task612, task610a, task610b, task69, task62, task576, task574, task581, task575, task572b, task573a, task573b, task573v, task572a, task570, task571a, task571b, task538b, task538a, task533, task532, task530a, task529a, task528a, task527a, task515, task59, task53b, task53a, task47, task410, task411, task416a, task416b, task423a, task427, task431a, task431b, task436, task464, task465, task466, task467, task469, task4100, task4100b, task4103, task4103b, task4104, task510


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

    def test_task410a(self): #тест на квадарт
        a = 1
        b = 2
        result = task410(a, b)
        assert_equal(result, 'square')

    def test_task411(self): #тест на A
        a = tuple([2, 2])
        b = tuple([4, 2])
        result = task411(a, b)
        assert_equal(result, a)

    def test_task411a(self): #тест на B
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
        expected_result = 'upward_position'
        assert_equal(result, expected_result) #тест на нормальную кость

        a = 20
        b = 10
        c = 1
        d = 2
        e = 3
        result = task466(a, b, c, d, e)
        expected_result = 'normal_position'
        assert_equal(result, expected_result) #тест слишком толстую кость

        a = 20
        b = 10
        c = 1
        d = 3
        e = 2
        result = task466(a, b, c, d, e)
        expected_result = 'side_position'
        assert_equal(result, expected_result) #тест слишком широкую кость

    def test_task467(self):
        k = 1
        result = task467(k)
        expected_result = 'work'
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
        expected_result = "второй принадлежит первому"
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
        expected_result = "первый принадлежит второму"
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
        expected_result = "не пересекаются"
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
        expected_result = "пересекаются частично"
        assert_equal(result, expected_result)  #тест что пересекаются частично

    def test_task4100(self):
        first = 1
        second = 2
        third = 3
        result = task4100(first, second, third)
        expected_result = 2
        assert_equal(result, expected_result)  #тест на 1*2=2

    def test_task4100a(self):
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

    def test_task529a(self):
        expected_result = 50 #средне арифметические всех целых чисел от 1 до 100
        result = task529a(100) #до скольки считать
        assert_equal(expected_result, result)

    def test_task530a(self):
        expected_result = 25502500 #сумма кубов всех чисел от 1 до 100
        result = task530a(100) #до скольки считать
        assert_equal(expected_result, result)

    def test_task532(self):
        expected_result = 3.283333333333333 #итоговая сумма
        result = task532(5) #до скольки поднимать делитель
        assert_equal(expected_result, result)

    def test_task533(self):
        expected_result = 1.9166666666666665 #итоговая сумма
        result = task533(1, 3, 2, 5) #1 первый/последний делитель, первое/последнее делимое
        assert_equal(expected_result, result)

    def test_task538a(self):
        expected_result = -40250 #ответ в метрах
        road_length = 1000 #длинна дороги  в м.
        husband_cycle = 100 #количество муже-циклов
        result = task538a(road_length, husband_cycle)
        assert_equal(expected_result, result)

    def test_task538aa(self):
        expected_result = -40666.666666666664 #ответ в метрах
        road_length = 1000 #длинна дороги  в м.
        husband_cycle = 100 #количество муже-циклов
        result = task538a(road_length, husband_cycle)
        assert_equal(expected_result, result)

    def test_task538b(self):
        expected_result = 109333.3333333332 #ответ в метрах
        road_length = 1000 #длинна дороги  в м.
        husband_cycle = 100 #количество муже-циклов
        result = task538b(road_length, husband_cycle)
        assert_equal(expected_result, result)

    def test_task570(self):
        expected_result = [4, 8, 16, 32, 64, 128, 256, 512] #ответ в клетках на такой-то час
        time_elapsed = [3, 6, 9, 12, 16, 19, 21, 24] #контрольные часы
        cells = 2 #изначальное кол-во клеток
        result = task570(time_elapsed, cells)
        assert_list_equal(expected_result, result)

    def test_task571b(self):
        expected_result = [1020, 1040, 1060, 1081, 1102, 1124, 1146, 1168, 1191, 1214, 1238, 1262, 1287] #прирост по месяцам
        deposit = 1000 #изначальный вклад
        time = 12 #длительность вклада в месяцах
        allowance = 2 #рост в процентах
        result = task571b(deposit, time, allowance)
        assert_list_equal(expected_result, result)

    def test_task571a(self):
        expected_result = [20, 40, 60, 81, 102, 124, 146, 168, 191, 214, 238, 262, 287] #прирост по месяцам
        deposit = 1000 #изначальный вклад
        time = 12 #длительность вклада в месяцах
        allowance = 2 #рост в процентах
        result = task571a(deposit, time, allowance)
        assert_list_equal(expected_result, result)

    def test_task572a(self):
        expected_result = [11000, 12100, 13310, 14641, 16105, 17715, 19486, 21434, 23577, 25934, 28527] #пробеги по дням
        run = 10000 #изначальный пробег в метрах
        days = 10 #кол-во дней
        gain = 10 #ежедневный прирост в процентах
        result = task572a(run, days, gain)
        assert_list_equal(expected_result, result)

    def test_task572b(self):
        expected_result = 125791 #пробеги по дням
        run = 10000 #изначальный пробег в метрах
        days = 7 #кол-во дней
        gain = 10 #ежедневный прирост в процентах
        result = task572b(run, days, gain)
        assert_equal(expected_result, result)

    def test_task573a(self): #а) урожайность за второй, третий, ..., восьмой год;
        expected_result = [2100, 2200, 2300, 2400, 2520, 2640, 2760, 2880, 3020] #урожаи по годам
        s = 100 #площадь поля
        harvest = 20 #урожайтность в центнерах на гектар
        harvest_gain = 2 #ежегодной прирост к урожайности в процентнах
        s_gain = 5  #ежегодной прирост к площади в процентнах
        year = 8 #кол-во лет
        result = task573a(harvest, s, harvest_gain, s_gain, year)
        assert_list_equal(expected_result, result)

    def test_task573b(self): #б) площадь участка в четвертый, пятый, ..., седьмой год
        expected_result = [105, 110, 115, 120, 126, 132, 138, 144] #площадь по годам
        s = 100 #площадь поля
        harvest = 20 #урожайтность в центнерах на гектар
        harvest_gain = 2 #ежегодной прирост к урожайности в процентнах
        s_gain = 5  #ежегодной прирост к площади в процентнах
        year = 7 #кол-во лет
        result = task573b(harvest, s, harvest_gain, s_gain, year)
        assert_list_equal(expected_result, result)

    def test_task573v(self): # В какой урожай будет собран за первые шесть лет
        expected_result = 16920 #урожаи итого
        s = 100 #площадь поля
        harvest = 20 #урожайтность в центнерах на гектар
        harvest_gain = 2 #ежегодной прирост к урожайности в процентнах
        s_gain = 5  #ежегодной прирост к площади в процентнах
        year = 6 #кол-во лет
        result = task573v(harvest, s, harvest_gain, s_gain, year)
        assert_equal(expected_result, result)

    def test_task574(self): # Определить суммарный объем в литрах двенадцати вложенных друг в друга шаров со стенками толщиной 5 мм. Внутренний диаметр внутреннего шара равен 10 см. Принять, что шары вкладываются друг в друга без зазоров.
        expected_result = 5567.453333333334 #объём в литрах
        shell_width = 0.5 #толщина стенки в см
        internal_d = 10 #Внутренний диаметр внутреннего шара в см
        number = 12 #число шаров
        result = task574(shell_width, internal_d, number)
        assert_equal(expected_result, result)

    def test_task575(self):
        expected_result = 60 #сумма
        num = 2 #исходное число
        deg = 5 #степень до которой повышать
        result = task575(num, deg)
        assert_equal(expected_result, result)

    def test_task576(self):
        expected_result = 60 #сумма
        num = 2 #исходное число
        deg = 5 #степень до которой повышать
        result = task576(num, deg)
        assert_equal(expected_result, result)

    def test_task581(self): #Даны натуральные числа х и у. Вычислить произведение x y , используя лишь операцию сложения.
        expected_result = 6 #сумма
        x = 2 #число раз
        y = 3 #число два
        result = task581(x, y)
        assert_equal(expected_result, result)

    def test_task61b(self): #найти количество всех чисел последовательности.
        expected_result = 6 #сумма
        seq = [5, 4, 3, 2, 1, 0] #последовательность чисел
        result = task61b(seq)
        assert_equal(expected_result, result)

    def test_task62(self): #найти количество всех чисел последовательности.
        expected_result = 3 #сумма
        seq = [5, 4, 3, 2, 1, -1] #последовательность чисел
        result = task62(seq)
        assert_equal(expected_result, result)

    """def test_task65(self): #Дана последовательность целых чисел в начале которой записано несколько равных между собой элементов. Определить количество таких элементов последовательности. Условный оператор не использовать.
        expected_result = 3 #колво
        seq = [1, 1, 1, 2, 3, 4] #последовательность чисел
        result = task65(seq)
        assert_equal(expected_result, result)"""

    def test_task69(self): #Среди чисел 1, 4, 9, 16, 25, ... найти первое число, большее n.
        expected_result = 20 #первое число больше 15
        seq = [5, 10, 15, 20, 25, 30] #последовательность чисел
        result = task69(seq)
        assert_equal(expected_result, result)

    def test_task610a(self): #Напечатать те натуральные числа, квадрат которых не превышает n.
        expected_result = [0, 1, 2, 3]
        n = 2
        result = task610a(n)
        assert_list_equal(expected_result, result)

    def test_task610b(self): #Найти первое натуральное число, квадрат которого больше n.
        expected_result = 2
        n = 2
        result = task610b(n)
        assert_equal(expected_result, result)

    def test_task612(self): #Дано число а (1 < а 1,5). Среди чисел 1+1/2 1+1/3... найти первое меньше а
        expected_result = 1.25
        a = 1.33
        result = task612(a)
        assert_equal(expected_result, result)

    def test_task613(self): #Рассмотрим последовательность чисел: 1+1/2 1+1/3... 1+1/n. Напечатать все значения n, при которых все числа последовательности будут не меньше а (1 < а 1,5).
        expected_result = [1, 2, 3]
        a = 1.33
        result = task613(a)
        assert_list_equal(expected_result, result)

    def test_task614(self): #Дано число а (1 < а 1,5). Найти такое наименьшее n, что в последовательности чисел 1+1/2 1+1/3... 1+1/n последнее число будет меньше а.
        expected_result = 4
        a = 1.33
        result = task614(a)
        assert_equal(expected_result, result)

    def test_task616(self): #Среди чисел 1, (1+1/2)+(1+1/3)...  найти первое, больше числа n.
        expected_result = 3.5
        n = 2
        result = task616(n)
        assert_equal(expected_result, result)

    def test_task617(self): #Дано вещественное число а. Напечатать все значения n, при которых 1, (1+1/2)+(1+1/3)...(1+1/n) > a
        expected_result = [46, 47, 48, 49]
        a = 50
        result = task617(a)
        assert_list_equal(expected_result, result)

    def test_task619(self): #Рассмотрим последовательность, образованную дробями: 1/1, 2/1, 3/2, ...,в которой числитель знаменатель) следующего члена последовательностиполучается сложением числителей (знаменателей) двух предыдущих ленов. Числители двух первых дробей равны 1 и 2, знаменатели — 1 и 1. Найти первый член такой следовательности, который отличается от предыдущего члена не более чем на 0,001.
        expected_result = 1.618033988749895
        num1 = 1 #числитель
        den1 = 1 #знаменатель
        num2 = 2 #числитель
        den2 = 1 #знаменатель
        result = task619(den1, den2, num1, num2)
        assert_equal(expected_result, result)

    def test_task622g(self): #найти сумму его цифр, больших пяти.
        expected_result = 14
        number = 2468
        result = task622g(number)
        assert_equal(expected_result, result)

    def test_task622d(self): #произведение его цифр, больших семи;
        expected_result = 64
        number = 2488
        result = task622d(number)
        assert_equal(expected_result, result)

    def test_task622e(self): #сколько раз в нем встречаются цифры 0 и 5 (всего).
        expected_result = 4
        number = 5050
        result = task622e(number)
        assert_equal(expected_result, result)

    def test_task68a(self): #Дано натуральное число, в котором все цифры различны. Определить:порядковый номер его максимальной цифры, считая номера:от конца числа
        expected_result = -1 #минус значит что с конца
        number = 1234
        result = task628a(number)
        assert_equal(expected_result, result)

    def test_task68b(self): #Дано натуральное число, в котором все цифры различны. Определить:порядковый номер его минимальной цифры, считая номера:от начала числа
        expected_result = 1
        number = 1234
        result = task628b(number)
        assert_equal(expected_result, result)

    def test_task630(self): #Дано натуральное число. Определить номер цифры 8 в нем, считая от концачисла. Если такой цифры нет, тветом должно быть число 0, если таких цифр в числе несколько — должен быть определен номер самой левой из них.
        expected_result = -8 #минус значит что с конца
        number = 82345678 #самая левая 8-ка стоит в начале
        target = 8 #число, что ищем
        result = task630(number, target)
        assert_equal(expected_result, result)

    def test_task631(self): #Дано натуральное число. Определить, сколько раз в нем встречается максимальная цифра
        expected_result = 2 #две 8-ки
        number = 82345678 # 8ка тут самая большая
        result = task631(number)
        assert_equal(expected_result, result)

    def test_task632(self): #Дано натуральное число. Определить, сколько раз в нем встречается минимальная цифра
        expected_result = 1 #одна 2-ки
        number = 82345678 # 2ка тут самая мелкая
        result = task632(number)
        assert_equal(expected_result, result)

    def test_task633(self): #Напечатать все кратные тринадцати натуральные числа, меньшие 100.
        expected_result = [13, 26, 39, 52, 65, 78, 91]
        number = 100 # до скольки считать
        result = task633(number)
        assert_list_equal(expected_result, result)

    def test_task643(self): #Дана непустая последовательность вещественных чисел, оканчивающаясячислом 100. Последовательность является неубывающей. Несколько чисел,идущих подряд, равны между собой. Сколько различных чисел имеется в последовательности?
        expected_result = 5 #сколько РАЗНЫХ значений в последовательности
        seq = [20, 20, 40, 60, 80, 100] #последовательность
        result = task643(seq)
        assert_equal(expected_result, result)

    def test_task643b(self): #Дана непустая последовательность вещественных чисел, оканчивающаясячислом 100. Последовательность является неубывающей. Несколько чисел,идущих подряд, равны между собой. Найти количество таких чисел?
        expected_result = 2 #сколько образчиков чисел имеют дубли, их две - 20 и 40
        seq = [20, 20, 40, 40, 60, 80, 100] #20 и 40 имеют дубли
        result = task643b(seq)
        assert_equal(expected_result, result)

    def test_task651(self): #Дано натуральное число. Выяснить, является ли оно палиндромом ("перевертышем"), т. е. числом,десятичная запись которого читается одинаково слева направо и справа налево.
        expected_result = True
        number = 696
        result = task651(number)
        assert_true(expected_result, result)

    def test_task653(self): #Дано натуральное число. Установить, является ли последовательность егоцифр при просмотре их справа налево упорядоченной по возрастанию. Например, для числа 5321 ответ положительный, для чисел 7820 и 9663 — отрицательный и т. п.
        expected_result = True
        number = 4321
        result = task653(number)
        assert_true(expected_result, result)

    def test_task654(self): #Дано натуральное число. Установить, является ли последовательность его цифр при просмотре их справа налево упорядоченной по возрастанию. Например, для числа 5321 ответ положительный, для чисел 7820 и 9663 — отрицательный и т. п
        expected_result = True
        number = 1234
        result = task654(number)
        assert_true(expected_result, result)

    def test_task655(self): #Дано натуральное число. Установить, является ли последовательность его цифр при просмотре их слева направо упорядоченной по возрастанию. Например, для числа 1478 ответ положительный, для чисел 1782 и668 — отрицательный и т. п.
        expected_result = True
        number = 1234
        result = task655(number)
        assert_true(expected_result, result)

    def test_task656(self): #. Дано натуральное число. Установить, является ли последовательность его цифр при просмотре их слева направо упорядоченной по неубыванию. Например, для чисел 1368 и 1669 ответ положительный, для числа 1782 — отрицательный и т. п.
        expected_result = True
        number = 1234
        result = task656(number)
        assert_true(expected_result, result)

    def test_task657(self): #. Дано натуральное число. Установить, является ли последовательность его цифр при просмотре их слева направо упорядоченной по неубыванию. Например, для чисел 1368 и 1669 ответ положительный, для числа 1782 — отрицательный и т. п.
        expected_result = 10
        seq = [10, 20, 30, 40]
        number = 1
        result = task657(number, seq)
        assert_equal(expected_result, result)

    def test_task658(self): #. Дана последовательность вещественных чисел Определить, есть ли в последовательности отрицательные числа. В случае положительного ответа определить порядковый номер первого из них.
        expected_result = 2
        seq = [1, 2, -3, -4]
        result = task658(seq)
        assert_equal(expected_result, result)

    def test_task660(self): #Дана последовательность натуральных чисел Определить, есть ли в последовательности хотя бы одно число, оканчивающееся цифрой 7? В случае положительного ответа определить порядковый номер первого из них
        expected_result = 6
        seq = [1, 2, 3, 4, 5, 6, 7]
        result = task660(seq)
        assert_equal(expected_result, result)

    def test_task661(self): # Дана непустая последовательность целых чисел, оканчивающаяся числом –1 Определить, есть ли в последовательности хотя бы одно число, кратное семи? В случае положительного ответа определить порядковый номер первого из них
        expected_result = 3
        seq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        result = task661(seq)
        assert_equal(expected_result, result)

    def test_task666(self): #Дана последовательность целых чисел, оканчивающаяся числом –1. Количество чисел в последовательности не меньше двух. Определить, есть ли в ней хотя бы одна пара одинаковых "соседних" чисел. В случае положительного ответа определить порядковые номера чисел первой из таких пар.
        expected_result = 11, 10
        seq = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0, -1]
        result = task666(seq)
        assert_equal(expected_result, result)

    def test_task669(self): #Дана последовательность вещественных чисел Определить,является ли последовательность упорядоченной по возрастанию. В случае отрицательного ответа определить порядковый номер первого числа, нарушающего такую упорядоченность.
        expected_result = 5
        seq = [1, 2, 3, 4, 5, 0]
        result = task669(seq)
        assert_equal(expected_result, result)

    def test_task677(self): #Дано натуральное число. Определить, является ли оно членом последовательности Фибоначчи (первый ивторой члены последовательности равны 1, каждый следующий равен сумме двух предыдущих).
        expected_result = 5
        number = 5
        result = task677(number)
        assert_equal(expected_result, result)

    def test_task686(self): #Дано натуральное число. Если в нем есть цифры a и b, то определить, какая из них расположена в числе правее. Если одна или обе эти цифры встречаются в числе несколько раз, то должны быть учтены самые правые из одинаковых цифр
        expected_result = 2
        a = 1
        b = 2
        number = 9122
        result = task686(number, a, b)
        assert_equal(expected_result, result)

    def test_task6105(self): #Дан прямоугольник с размерами a b. От него отрезают квадраты максимального размера, пока это возможно. Затем от оставшегося прямоугольника вновь отрезают квадраты максимально возможного размера и т. д. На какие квадраты и в каком их количестве будет разрезан исходный прямоугольник?
        expected_result = [(3, 100), (1, 10)] #сперва кол-во квадратов, потом их сторона, потом кол-во/сторона следующего и так далее
        a = 310
        b = 100
        result = task6105(a, b)
        assert_equal(expected_result, result)

    def test_task6108(self): #В некоторой стране используются денежные купюры достоинством в 1, 2, 4,8, 16, 32 и 64. Дано натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n (указать количество каждой из используемых для выплаты купюр)? Предполагается, что имеется достаточно большое количество купюр всех достоинств.
        expected_result = [('B64', 4), ('B32', 1), ('B16', 0), ('B8', 0), ('B4', 1), ('B2', 1), ('B1', 0)]
        n = 310
        seq = [1, 2, 4, 8, 16, 32, 64]
        result = task6108(n)
        assert_equal(expected_result, result)

    def test_task825(self): #Найти количество делителей каждого из целых чисел от 120 до 130.
        expected_result = [16, 3, 4, 4, 4, 12, 2, 8, 4, 8]
        numbers = [120, 121, 122, 123, 125, 126, 127, 128, 129, 130]
        result = task825(numbers)
        assert_equal(expected_result, result)

    def test_task829(self): #Найти числа из промежутка у которых ровно 4 делителя
        expected_result = [122, 123, 125, 129]
        numbers = [120, 121, 122, 123, 125, 126, 127, 128, 129, 130]
        result = task829(numbers)
        assert_equal(expected_result, result)

    def test_task832(self): #Найти 10 первых простых чисел.
        expected_result = [122, 123, 125, 129]
        numbers = 1
        result = task832(numbers)
        assert_equal(expected_result, result)

    def test_task832(self): #Найти 10 первых простых чисел.
        expected_result = [122, 123, 125, 129]
        numbers = 1
        result = task832(numbers)
        assert_equal(expected_result, result)

    def test_task835(self): #Найти все целые числа из промежутка от 300 до 600, у которых сумма делителей кратна 10.
        expected_result = [361, 400, 441, 484, 576, 578]
        number1 = 300
        number2 = 600
        result = task835(number1, number2)
        assert_equal(expected_result, result)

    def test_task836(self): #ННайти все совершенные числа,меньшие 10 000.
        expected_result = [1, 6, 24, 28, 496, 2016, 8128, 8190]
        limit = 10000 #до скольки ищем
        result = task836(limit)
        assert_equal(expected_result, result)

    def test_task92(self): #Составить программу, которая запрашивает название футбольной команды и повторяет его на экране со словами "— это чемпион!".
        expected_result = 1
        team = str(input("Введите своё назание команды"))
        result = task92(team)
        assert_equal(expected_result, result)

    def test_task975a(self): #Дано предложение. Напечатать все его символы, предшествующие первой запятой.
        expected_result = 'казнить,'
        sentence = "казнить, нельзя помиловать"
        result = task975a(sentence)
        assert_equal(expected_result, result)

    def test_task976b(self): #Дано предложение, в котором имеется несколько букв е. найти номер последний
        expected_result = 19
        sentence = "еле-еле душа в теле"
        result = task976b(sentence)
        assert_equal(expected_result, result)

    def test_task991(self): #
        expected_result = 'шла_саша_по_шоссе'
        sentence = "шла саша по шоссе"
        result = task991(sentence)
        assert_equal(expected_result, result)

    def test_task992(self): #Дано предложение. Все его символы, стоящие на четных местах, заменить на ы
        expected_result = 'шыаысышы ыоышысы'
        sentence = "шла саша по шоссе"
        result = task992(sentence)
        assert_equal(expected_result, result)

    def test_task992(self): #Дано предложение. Все его символы, стоящие на четных местах, заменить на ы
        expected_result = 'шыаысышы ыоышысые'
        sentence = "шла саша по шоссе"
        result = task992(sentence)
        assert_equal(expected_result, result)

    def test_task923(self): #Дано предложение. Все его символы, стоящие на третьем, шестом, девятом и т. д. местах, заменить буквой а
        expected_result = 'шла сашаапоашоасе'
        sentence = "шла саша по шоссе"
        result = task993(sentence)
        assert_equal(expected_result, result)

    def test_task9100(self): #Дано слово. Поменять местами его вторую и пятую буквы.
        expected_result = 'Срвее'
        sentence = "Север"
        result = task9100(sentence)
        assert_equal(expected_result, result)

    def test_task9101(self): #Дано слово. Поменять местами его третью и последнюю буквы
        expected_result = 'Серев'
        sentence = "Север"
        result = task9101(sentence)
        assert_equal(expected_result, result)

    def test_task9102(self): #Дано слово. Поменять местами его m-ю и n-ю буквы
        expected_result = 'ревеС'
        sentence = "Север"
        posa = 1
        posb = 5
        result = task9102(sentence, posa, posb)
        assert_equal(expected_result, result)

    def test_task9103(self): #Дано слово из четного числа букв. Поменять местами первую букву со второй, третью — с четвертой и т. д.
        expected_result = 'ебераг'
        sentence = "берега"
        result = task9103(sentence)
        assert_equal(expected_result, result)

    def test_task9104(self): #Дано слово из четного числа букв. Поменять местами его половины следующим способом: первую букву поменять с последней, вторую — с предпоследней и т. д
        expected_result = 'аремих'
        sentence = "химера"
        result = task9104(sentence)
        assert_equal(expected_result, result)

    def test_task9105(self): #Дано слово из 12-ти букв. Переставить в обратном порядке буквы, расположенные между второй и десятой буквами (т. е. с третьей по девятую).
        expected_result = 'авирютнатка'
        sentence = "авантюристка"
        result = task9105(sentence)
        assert_equal(expected_result, result)

    def test_task9106(self): #Дано слово из 15-ти букв. Переставить в обратном порядке буквы, расположенные между k-й и s-й буквами(т. е. с (k + 1)-й по (s – 1)-ю). Значения k и s вводятся с клавиатуры, k < s.
        expected_result = 'автсдовокуротво'
        sentence = "авторуководство"
        first = 1
        last = 15
        result = task9106(sentence, first, last)
        assert_equal(expected_result, result)

    def test_task9107(self): #Дано слово. Поменять местами первую из букв а и последнюю из букв о. Учесть возможность того, что таких букв в слове может не быть.
        expected_result = 'копа'
        sentence = "капо"
        buka = 'а'
        buko = 'о'
        result = task9107(sentence, buka, buko)
        assert_equal(expected_result, result)


    def test_task9108b(self): #Устранить имеющуюся в заданном слове ошибку:
        expected_result = 'графика'
        sentence = "граффика"
        result = task9108b(sentence)
        assert_equal(expected_result, result)

    def test_task9109b(self): #Удалить из него k-ю букву
        expected_result = 'ад'
        sentence = "рад"
        k = 1
        result = task9109b(sentence, k)
        assert_equal(expected_result, result)

    def test_task9111(self): #Дано слово. Если его длина нечетная, то удалить среднюю букву, в противном случае — две средних буквы
        expected_result = 'ко'
        sentence = "капо"
        result = task9111(sentence)
        assert_equal(expected_result, result)

    def test_task9111b(self): #Дано слово. Если его длина нечетная, то удалить среднюю букву, в противном случае — две средних буквы
        expected_result = 'пока'
        sentence = "попка"
        result = task9111b(sentence)
        assert_equal(expected_result, result)

    def test_task9112(self): # Дано предложение. Удалить из него все символы с n1-го по n2-й
        expected_result = 'ко'
        sentence = "капо"
        n1 = 2
        n2 = 3
        result = task9112(sentence, n1, n2)
        assert_equal(expected_result, result)

    def test_task9115(self): # Дано предложение. Удалить из него все буквы о, стоящие на нечетных местах.
        expected_result = 'клесица'
        sentence = "околесица"
        result = task9115(sentence)
        assert_equal(expected_result, result)

    def test_task9114(self): # Дано слово. Удалить из него все повторяющиеся буквы, оставив их первые вхождения, т. е. в слове должны остаться только различные буквы.
        expected_result = 'длиноше'
        sentence = "длинношеее"
        result = task9114(sentence)
        assert_equal(expected_result, result)

    def test_task9153(self): # Дан текст. Найти наибольшее количество идущих подряд одинаковых символов.
        expected_result = 3
        sentence = "длинношеее"
        result = task9153(sentence)
        assert_equal(expected_result, result)

    def test_task9155(self): # В слове имеются только две одинаковых буквы. Найти их.
        expected_result = "а"
        sentence = "ваза"
        result = task9155(sentence)
        assert_equal(expected_result, result)

    def test_task9156(self): # Даны два слова. Для каждой буквы первого слова (в том числе для повторяющихся в этом слове букв) определить, входит ли она во второе слово. Например, если заданные слова информация и процессор, то для букв первого из них ответом должно быть: нет нет нет да да нет нет да нет нет.
        expected_result = [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]
        w1 = "информация"
        w2 = "процессор"
        result = task9156(w1, w2)
        assert_equal(expected_result, result)

    def test_task9157(self): # Даны два слова. Для каждой буквы первого слова (в том числе для повторяющихся в этом слове букв) определить, входит ли она во второе слово. Например, если заданные слова информация и процессор, то для букв первого из них ответом должно быть: нет нет нет да да нет нет да нет нет.
        expected_result = [0, 1, 1, 1, 0, 0]
        w2 = "информация"
        w1 = "процессор"
        result = task9157(w1, w2)
        assert_equal(expected_result, result)

    def test_task9158(self): #  Даны два слова. Напечатать только те буквы слов, которые встречаются в обоих словах только один раз. Например, если заданные слова процессор и информация, то ответом должно быть: п е ф м а я.
        expected_result = 1
        w2 = "информация"
        w1 = "процессор"
        result = task9158(w1, w2)
        assert_equal(expected_result, result)

    def test_task9184(self): #  Дан текст. Проверить, правильно ли в нем расставлены круглые скобки (т. е.находится ли справа от каждой открывающей скобки соответствующая ейзакрывающая скобка, а слева от каждой закрывающей — оответствующая ей закрывающая). Предполагается, что внутри каждой пары скобок нет других скобок.
        expected_result = 1
        sentence = "Съешь (ещё) булочек (побольше)"
        result = task9184(sentence)
        assert_equal(expected_result, result)

    def test_task9184b(self): # В случае неправильности расстановки скобок: если имеются лишние правые (закрывающие) скобки, то выдать сообщение с указанием позиции первой такой скобки;
        expected_result = 12
        sentence = "Съешь (ещё)) булочек (побольше)"
        result = task9184b(sentence)
        assert_equal(expected_result, result)

    def test_task9185a(self): # *Строка содержит арифметическое выражение, в котором используются круглые скобки, в том числе вложенные. Проверить, правильно ли в нем расставлены скобки.
        expected_result = 1 #в данном случае только одна лишняя открывающая скобка
        sentence = "Съешь (((ещё) булочек) побольше"
        result = task9185(sentence)
        assert_equal(expected_result, result)

    def test_task9185b(self): # *Строка содержит арифметическое выражение, в котором используются круглые скобки, в том числе вложенные. Проверить, правильно ли в нем расставлены скобки.
        expected_result = 'ok' #в данном случае всё норм
        sentence = "Съешь ((ещё) булочек) побольше"
        result = task9185(sentence)
        assert_equal(expected_result, result)

    def test_task9185c(self): # *Строка содержит арифметическое выражение, в котором используются круглые скобки, в том числе вложенные. Проверить, правильно ли в нем расставлены скобки.
        expected_result = 22 #лишняя скобка стоит в позиции 22
        sentence = "Съешь ((ещё) булочек)) побольше"
        result = task9185(sentence)
        assert_equal(expected_result, result)

    def test_task9185c(self): # *Строка содержит арифметическое выражение, в котором используются круглые скобки, в том числе вложенные. Проверить, правильно ли в нем расставлены скобки.
        expected_result = 22 #лишняя скобка стоит в позиции 22
        sentence = "Съешь ((ещё) булочек)) побольше"
        result = task9185(sentence)
        assert_equal(expected_result, result)

    def test_task9187(self): # *Дано натуральное число n (n 1000). Напечатать это число русскими словами (тринадцать, сто пять, двести сорок один, тысяча и т. д.).
        expected_result = "одна тысяча двести тридцать четыре"
        number = 1234
        result = task9187(number)
        assert_equal(expected_result, result)
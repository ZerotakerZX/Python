import numpy as np
from array import *

def task47(a, b):
    if a > b:
        return b, a

    if b > a:
        return a, b


def task410(a, b):
    circle = a ** 2 * 3.1415  # 12.566 при 2 и 3.1415 при 1
    square = b * b  # 4
    if circle > square:
        return 'circle'
    else:
        return 'square'


def task411(a, b):
    try:
        material_a = (a[1] / a[0])  # 1
    except ZeroDivisionError:
        material_a = 0

    try:
        material_b = (b[1] / b[0])  # 0.5
    except ZeroDivisionError:
        material_b = 0

    if material_a > material_b:
        return a
    else:
        return b


def task416a(a, b):
    circle_dia = (a / 3.14) ** .5 * 2  # 3.181808675974975 при 2
    square_side = b ** .5  # 0.5 при 4
    if square_side > circle_dia:
        return True
    else:
        return False


def task416b(a, b):
    circle_dia = (a / 3.14) ** .5 * 2
    square_dia = (b ** .5) * (2 ** .5)
    if circle_dia > square_dia:
        return True
    else:
        return False


def task423a(number):
    fst_digit = number // 10
    snd_digit = number % 10
    if fst_digit > snd_digit:
        return fst_digit

    return snd_digit


def task427(number):
    if (number // 100) == (number % 10):
        return True

    return False


def task431a(number):
    if (number // 100) == (number % 10) == (number // 10 % 10):
        return True
    return False


def task431b(number):
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10
    if first_digit == second_digit:
        return True
    if second_digit == third_digit:
        return True
    if first_digit == third_digit:
        return True
    return False


def task436(minute, green, red):
    cycle_period = red + green
    cycle = minute % cycle_period
    if 0 < cycle < green:
        return 'green'
    return 'red'


def task465(year):
    """
    if ((year / 4) % 100) == 0: #високсный кратный 400
        return True

    if (year % 4) == 0 and ((year / 4) % 100) == 0: #просто високосный не кратный 100 кроме 400
        return True

    if (year % 4) == 0: #просто високосный не кратный 100 кроме 400
        return True
    """
    if (year % 4) != 0:  # просто високосный
        return False

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return True


def task464(number):
    d1 = number // 100000
    d2 = number // 10000 % 10
    d3 = number // 1000 % 10
    d4 = number // 100 % 10
    d5 = number // 10 % 10
    d6 = number % 10
    if d1 + d2 + d3 == d4 + d5 + d6:
        return True
    return False


def task466(a, b, c, d, e):
    s_table = a * b  # площадь стола
    domino_a = c * d  # площадь домино картинкой вверх
    domino_b = c * e  # площадь домино н лежащей на боку
    domino_c = d * e  # площадь стоящей на торце
    if (s_table // domino_a) > (s_table // domino_b) and (s_table // domino_a) > (s_table // domino_c):
        return 'normal_position'
    if (s_table // domino_b) > (s_table // domino_a) and (s_table // domino_b) > (s_table // domino_c):
        return 'side_position'
    if (s_table // domino_c) > (s_table // domino_a) and (s_table // domino_c) > (s_table // domino_b):
        return 'upward_position'


def task467(k):
    weekday = k % 7
    if k <= 5:
        return 'work'
    return 'rest'


def task469a(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start,
             second_hor_start, second_ver_start):
    first_hor_end = first_hor_start + first_hor_lenght
    first_ver_end = first_ver_start + first_ver_lenght
    second_ver_end = second_ver_start + second_ver_lenght
    second_hor_end = second_hor_start + second_hor_lenght
    if (second_hor_lenght >= first_hor_lenght) and (second_hor_end >= first_hor_end) and (
            second_ver_lenght >= first_ver_lenght) and (
            second_ver_end >= first_ver_end):  # работает только если фигуры в положительном диапозоне
        return True
    return False


def task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start,
            second_hor_start, second_ver_start):
    first_hor_end = first_hor_start + first_hor_lenght
    first_ver_end = first_ver_start + first_ver_lenght
    second_ver_end = second_ver_start + second_ver_lenght
    second_hor_end = second_hor_start + second_hor_lenght
    if first_hor_start > second_hor_end and first_ver_start > second_ver_end:
        return "не пересекаются"  # задание В, что не пересекаются вовсе
    if second_hor_start > first_hor_end and second_ver_start > first_ver_end:
        return "не пересекаются"  # задание В, что не пересекаются вовсе
    if (second_hor_lenght >= first_hor_lenght) and (second_hor_end >= first_hor_end) and (
            second_ver_lenght >= first_ver_lenght) and (
            second_ver_end >= first_ver_end):  # работает только если фигуры в положительном диапозоне
        return "второй принадлежит первому"  # задание А, что второй вписывается в первый
    if (first_hor_lenght >= second_hor_lenght) and (first_hor_end >= second_hor_end) and (
            first_ver_lenght >= second_ver_lenght) and (
            first_ver_end >= second_ver_end):  # работает только если фигуры в положительном диапозоне
        return "первый принадлежит второму"  # задание Б, покрывает вариант и что первый вписывается во второй
    return "пересекаются частично"


def task4100(first, second, third):
    global b, a
    if first < second and first < third:
        a = first  # если первое число - первое наименьшее
        if second < third:
            b = second  # если второе число - второе наименьшее
        if third < second:
            b = third  # если третье число - второе наименьшее
    if second < first and second < third:
        a = second  # если второе число - первое наименьшее
        if first < third:
            b = first  # если первое число - второе наименьшее
        if third < first:
            b = third  # если третье число - второе наименьшее
    if third < first and third < second:
        a = third  # если третье число - первое наименьшее
        if first < third:
            b = first  # если первое число - второе наименьшее
        if second < first:
            b = second  # если второе число - второе наименьшее
    c = a * b
    return c


def task4100b(first, second, third):
    if first > second and first > third:
        return second * third
    if second > third and second > first:
        return third * first
    if third > first and third > second:
        return second * first


def task4103(first, second, third):
    if first > second and first > third:
        return first
    if second > third and second > first:
        return second
    return third


def task4103b(first, second, third):
    if first < second and first < third:
        return first
    if second < third and second < first:
        return second
    return third


def task4104(day):
    if day == 1:
        print('понедельник')
        return 'понедельник'
    if day == 2:
        print('вторник')
        return 'вторник'
    if day == 3:
        print('среда')
        return 'среда'
    if day == 4:
        print('четверг')
        return 'четверг'
    if day == 5:
        print('пятница')
        return 'пятница'
    if day == 6:
        print('суббота')
        return 'суббота'
    if day == 7:
        print('воскресенье')
        return 'воскресенье'
    if day > 7:
        print('много')
        return 'много'


def task53a(start, end, step):
    return [i for i in range(start, end, step)]


"""
def task53b(start, end, step):
    result = []
    for i in range(start, end, step):
        result.append(i * i)
    return result
"""


def task53b(start, end, step):
    return [i * i for i in range(start, end, step)]


def task59(start, end, step):
    result = []
    for i in range(start, end, step):
        result.append(i * 2.5)
    return result


def task510(step):
    start = 0
    end = 181
    result = []
    for i in range(start, end, step):
        result.append(i)
    return result


def task515(end):
    start = 0
    step = 1
    result = []
    for i in range(start, end, step):  # печать таблицы умножения
        quotient = i * 7
        print(f"{quotient} X 7 = {i}.")
    for i in range(start, end, step):  # просчёт результата для сверки
        result.append(i * 7)
    return result


def task527a(end):
    start = 0
    step = 1
    result = []
    all_numbers = []
    for i in range(start, end, step):
        all_numbers.append(i)  # добавить в переменную-список все нужные числа
        the_sum = sum(all_numbers)  # взять содержимое списка и суммировать
        result = the_sum  # и добавить в переменную результат
    return result


def task528a(start, end):
    step = 1
    end = end + 1  # на случай ввода максимального числа с клавы
    result = []
    all_numbers = []
    the_prod = 1
    for i in range(start, end, step):
        all_numbers.append(i)  # добавить в переменную-список все нужные числа
    for i in all_numbers:  # взять содержимое списка и перемножить
        the_prod *= i  # и добавить в переменную результат
        result = the_prod
    return result


def task529a(end):
    start = 0
    step = 1
    end = end + 1  # на случай ввода максимального числа с клавы
    result = []
    all_numbers = []
    the_avg = 1
    for i in range(start, end, step):
        all_numbers.append(i)  # добавить в переменную-список все нужные числа
    for i in all_numbers:  # взять содержимое списка и усреднить
        the_avg = sum(all_numbers) / len(all_numbers)  # и добавить в переменную результат
        result = the_avg
    return result


def task530a(end):
    start = 0
    step = 1
    end = end + 1  # на случай ввода максимального числа с клавы
    all_numbers = []
    the_cube = []
    for i in range(start, end, step):
        all_numbers.append(i)  # добавить в переменную-список все нужные числа
    for i in all_numbers:
        the_cube.append(i * i * i)  # добавить в другую переменную квадраты всех чисел
    cube_sum = sum(the_cube)  # и найте сумму их
    result = cube_sum
    return result


def task532(end):
    start = 1
    step = 1
    end = end + 1  # на случай ввода максимального числа с клавы
    all_numbers = []  # это будет делимое
    the_dividend = [1, 1, 1, 1, 1]  # делитель из условия задачи
    division_total = []  # тут будет список - результат деления всех дробных
    for i in range(start, end, step):
        all_numbers.append(i)  # добавить в переменную-список все нужные числа - делитель
    for i in range(0, len(the_dividend)):
        division_total.append(the_dividend[i] / all_numbers[i])  # взять делимое и поделить каждое число на делитель
    fraction_sum = 1 + sum(division_total)  # и найте сумму их, прибавленную к единице
    result = fraction_sum
    return result


def task533(start, end, start2, end2):
    step = 1  # степ общий для обоих
    end = end + 1  # на случай ввода максимального числа с клавы
    end2 = end2 + 1  # на случай ввода максимального числа с клавы
    all_numbers1 = []  # это будет делимое
    all_numbers2 = []  # это будет делитель
    division_total = []  # тут будет список - результат деления всех дробных
    for i in range(start, end, step):
        all_numbers1.append(i)  # добавить в переменную-список все нужные числа - делимое
    for i in range(start2, end2, step):
        all_numbers2.append(i)  # добавить в переменную-список все нужные числа - делимое
    for i in range(0, len(all_numbers1)):
        division_total.append(all_numbers1[i] / all_numbers2[i])  # взять делимое и поделить каждое число на делитель
    fraction_sum = sum(division_total)  # и найте сумму их
    result = fraction_sum
    return result


def task538a(road_length, husband_cycle):
    current_position = 0  # переменная показывающая текущие координаты мужа
    current_position = current_position + road_length  # фаза0, муж пришёл на работу
    for x in range(1, husband_cycle + 1):
        current_position = (current_position - (road_length / 2))  # фаза1, муж первый раз передумал и пошёл на дом
        current_position = (current_position + (road_length / 3))  # фаза2, муж второй раз передумал и пошёл на работу
        current_position = (current_position - (road_length / 4))  # фаза3, муж третий раз передумал и пошёл на дом
        result = current_position
    return result


def task538b(road_length, husband_cycle):
    current_position = 0  # переменная показывающая текущие координаты мужа
    current_position = current_position + road_length  # фаза0, муж пришёл на работу
    total_travel = 1000  # сколько муж прошёл уже после фазы0
    for x in range(1, husband_cycle + 1):
        current_position = (current_position - (road_length / 2))  # фаза1, муж первый раз передумал и пошёл на дом
        total_travel = (total_travel + (road_length / 2))  # сколько прошёл муж после фазы1
        current_position = (current_position + (road_length / 3))  # фаза2, муж второй раз передумал и пошёл на работу
        total_travel = (total_travel + (road_length / 3))  # сколько прошёл муж после фазы2
        current_position = (current_position - (road_length / 4))  # фаза3, муж третий раз передумал и пошёл на дом
        total_travel = (total_travel + (road_length / 4))  # сколько прошёл муж после фазы3
        result = total_travel
    return result


def task570(time_elapsed, cells):
    cells_log = []  # список куда будет записано число клеток в контрольные часы
    start = time_elapsed[0]  # найти стартый подсчёта клеток после деления
    end = time_elapsed[-1] + 1  # правильный момент для остановки
    step = time_elapsed[1] - time_elapsed[0]  # найти размер шага между контрольными часами
    for i in range(start, end, step):  # правильный цикл деления клеток по часам
        while (i % step) == 0:  # чтобы знать когда контрольный час пробил
            cells = cells * 2  # формула деления клеток
            cells_log.append(cells)  # запись клеток по часам в специальный лог
            break
    result = cells_log
    return result


def task571b(deposit, time, allowance):
    deposit_log = []  # список куда будет записано состояние счёта каждый месяц
    precent = allowance / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, time + 1, 1):  # правильный цикл по длительности вклада
        while (i % 1) == 0:  # чтобы знать когда кончился месяц и пора начислять
            deposit = deposit + int((
                    deposit * precent))  # формула получения прибыли без копеек (может лучше делать через round, но это не точно)
            deposit_log.append(deposit)  # запись прибыли по месяцам в специальный лог
            break  # без него процесс длиться бесконечно
    result = deposit_log
    return result


def task571a(deposit, time, allowance):
    income_log = []  # список куда будет записано кол-во прибыли каждый месяц
    deposit_original = deposit  # запомнить изначальную сумму
    precent = allowance / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, time + 1, 1):  # правильный цикл по длительности вклада
        while (i % 1) == 0:  # чтобы знать когда кончился месяц и пора начислять
            deposit = deposit + int((
                    deposit * precent))  # формула получения прибыли без копеек (может лучше делать через round, но это не точно)
            income_log.append(deposit - deposit_original)  # вычисление прироста каждый месяц по сравнению с оригиналом
            break  # без него процесс длиться бесконечно
    result = income_log
    return result


def task572a(run, days, gain):
    run_log = []  # список куда будет записана пробежка каждый день
    per_gain = gain / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, days + 1, 1):  # правильный цикл по тренировок
        while (i % 1) == 0:  # чтобы знать когда кончился день
            run = run + int((run * per_gain))  # формула роста длинны пробега
            run_log.append(run)  # записать результаты пробега в список
            break  # без него процесс длиться бесконечно
    result = run_log
    return result


def task572b(run, days, gain):
    run_log = []  # список куда будет записана пробежка каждый день
    per_gain = gain / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, days + 1, 1):  # правильный цикл по тренировок
        while (i % 1) == 0:  # чтобы знать когда кончился день
            run = run + int((run * per_gain))  # формула роста длинны пробега
            run_log.append(run)  # записать результаты пробега в список
            break  # без него процесс длиться бесконечно
    result = sum(run_log)
    return result


def task573a(harvest, s, harvest_gain, s_gain, year):
    harvest_log = []  # список куда будет записан урожай по годам
    harvest_gain = harvest_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    s_gain = s_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, year + 1, 1):  # цикл на 8 лет
        while (i % 1) == 0:  # чтобы знать когда кончился год
            s = s + int((s * s_gain))  # ежегодный рост площади
            harvest = harvest + int((harvest * harvest_gain))  # ежегодный прирост урожайности на гектар
            harvest_log.append(harvest * s)  # перемножить фертильность на площадь и записать в список результат
            break  # без него процесс длиться бесконечно
    result = harvest_log
    return result


def task573b(harvest, s, harvest_gain, s_gain, year):
    s_log = []  # список куда будет записан урожай по годам
    harvest_gain = harvest_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    s_gain = s_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, year + 1, 1):  # цикл на 8 лет
        while (i % 1) == 0:  # чтобы знать когда кончился год
            s = s + int((s * s_gain))  # ежегодный рост площади
            s_log.append(s)  # перемножить фертильность на площадь и записать в список результат
            break  # без него процесс длиться бесконечно
    result = s_log
    return result


def task573v(harvest, s, harvest_gain, s_gain, year):
    harvest_log = []  # список куда будет записан урожай по годам
    harvest_gain = harvest_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    s_gain = s_gain / 100  # конвертация процентов в более подходящий формат для расчётов
    for i in range(0, year + 1, 1):  # цикл на 8 лет
        while (i % 1) == 0:  # чтобы знать когда кончился год
            s = s + int((s * s_gain))  # ежегодный рост площади
            harvest = harvest + int((harvest * harvest_gain))  # ежегодный прирост урожайности на гектар
            harvest_log.append(harvest * s)  # перемножить фертильность на площадь и записать в список результат
            break  # без него процесс длиться бесконечно
    result = sum(harvest_log)
    return result


def task574(shell_width, internal_d, number):
    internal_r = internal_d / 2  # внутренний радиус - нужно для решения задачи.
    v_internal = ((
                          internal_r ** 3 * 3.14) / 3) * 4  # Объем шара пустоты внутри равен четырем третим от его радиуса в кубе помноженого на число пи.
    external_r = (internal_r + (number * shell_width))  # считаем радинус стенок внутреннего шара и всех последующих
    v_external = ((external_r ** 3 * 3.14) / 3) * 4  # Объем пространства в целом
    result = v_external - internal_r  # объём самих шаров это объём в целом, минус пустота внутри первого шара
    return result


def task575(num, deg):
    degs = []  # тут будут все степени в виде списка
    nums = []  # тут будут все степени в виде списка
    for i in range(2, deg + 1, 1):
        degs.append(i)
        while i == 2:
            nums.append(num * num)
            break
        while i == 3:
            nums.append(num * num * num)
            break
        while i == 4:
            nums.append(num * num * num * num)
            break
        while i == 5:
            nums.append(num * num * num * num * num)
            break  # вот это вот всё вместо возведения  в степень
    result = sum(nums)
    return result


def task576(num, deg):
    degs = []  # тут будут все степени в виде списка
    nums = []  # тут будут все степени в виде списка
    prod = [num]  # тут будет список с помощью кторого будет возводиться в нужную степерь
    prod2 = []  # после ручного возведения в степень результаты будут тут, чтобы потом суммироваться
    for i in range(2, deg + 1, 1):
        degs.append(i)
        while (i % 1) == 0:  # чтобы знать когда кончился цикл
            prod.append(num)  # цифра добавлятся в список столько раз, какая нужна степерь
            prod2.append(np.prod(prod))  # содержимое списка перемножается в нужную степерь и пишетсяся сюда
            break
    result = sum(prod2)
    return result


def task581(x, y):
    prod = []  # сюда будет дублироваться цифра столько раз, на сколько её нужно умножить
    for i in range(0, y, 1):
        while (i % 1) == 0:  # чтобы знать когда кончился цикл
            prod.append(x)  # запись цифры нужное число раз
            break
    result = sum(prod)
    return result


def task61b(seq):
    result = len(seq)
    return result


def task62(seq):
    result = sum(seq[:-1]) / len(seq[:-1])
    return result


"""def task65(seq):
    ab = seq[0:1]
    result = seq.count(ab)
    return result"""


def task69(seq):
    for i in seq:
        if i > 15:
            return i


def task610a(n):
    nl = []
    for i in range(0, 999, 1):
        while i < (n * n):
            nl.append(i)
            break
    return nl


def task610b(n):
    for i in range(0, 999, 1):
        if (i * i) > n:
            return i


def task612(a):
    for i in range(1, 999, 1):  # диапозон чисел которые будем перебирать
        if 1 + (1 / i) < a:  # требуемуе условия когда подобор остановится
            return 1 + (1 / i)  # и вернёт число которое при них получается, т.е. первое меньше а


def task613(a):
    n_list = []  # тут будте записан список значений n при которых выполняется условие
    for n in range(1, 999, 1):  # перечень цифр для перебора
        while 1 + (1 / n) >= a:  # сам условия
            n_list.append(n)  # годные значения пишутся в перечень
            break
    return n_list  # заполненный перечень возрвращается


def task614(a):
    temp_seq = []  # временный список для результатов вычесления последовательности 1+1/2 1+1/3... 1+1/n
    for n in range(1, 999, 1):  # перечень цифр для перебора
        temp_seq.append(1 + (1 / n))  # запись последовательностей в список
        if temp_seq[-1] < a:  # дождаться пока последний элемент в списке станет меньше а
            break
    return n  # и вернуть текущие значение n


def task616(n):
    temp_seq = []  # временный список для результатов вычесления последовательности 1, 1+1/2 1+1/3... 1+1/n
    for i in range(1, 999, 1):  # перечень цифр для перебора
        temp_seq.append(1 + (1 / i))  # запись последовательностей в список
        if sum(temp_seq) > n:  # дождаться сумма последовательности станет больше числа n
            break
    return sum(temp_seq)  # и вернуть эту сумму


def task617(a):
    temp_seq = []  # временный список для результатов вычесления последовательности 1, (1+1/2)+(1+1/3)...(1+1/n)
    n_seq = []  # хранилище походящих значений n
    for n in range(1, 50, 1):  # перечень цифр для перебора
        temp_seq.append(1 + (1 / n))  # запись последовательностей в список
        while sum(temp_seq) > a:  # дождаться сумма последовательности станет больше числа a
            n_seq.append(n)  # запись подходящих чисел n в отдельный список
            break
    return n_seq  # и вернуть эти n-ки


def task619(dem1, dem2, num1, num2):
    num_log = []  # лог всех числителей
    den_log = []  # лог всех знаменателей
    eq_log = []  # лог вычеслинных уравнений
    num_log.append(num1)  # добавляем в логи указанное уже в условиях задачи
    den_log.append(dem1)  # добавляем в логи указанное уже в условиях задачи
    num_log.append(num2)  # добавляем в логи указанное уже в условиях задачи
    den_log.append(dem2)  # добавляем в логи указанное уже в условиях задачи
    eq_log.append(num1 / dem1)  # добавляем в логи указанное уже в условиях задачи
    eq_log.append(num2 / dem2)  # добавляем в логи указанное уже в условиях задачи
    for i in range(0, 999, 1):  # запуск цикла
        num = sum(num_log[-2:])  # суммируем два последних числителя, чтобы получить текущий новый числитель
        num_log.append(num)  # и добавляем в лог для сохранности
        den = sum(den_log[-2:])  # тоже самое для знаменателя
        den_log.append(den)  # тоже самое для знаменателя
        eq = num / den  # делим текущий числитель на текущий знаменатель чтобы получить текущий результат деления дроби
        eq_log.append(eq)  # и его тоже пишем в лог для сохранности
    if (eq_log[-1] - eq_log[-2]) <= 000.1:
        return eq


def task622g(number):
    list_number = []  # список где будет лежать распиленное на цифры число
    list_number_aux = []  # список из списка, где будут подходящие числа (выше 5)
    alt_number = str(number)  # число в виде строки
    for digit in alt_number:
        list_number.append(int(digit))  # функция что распиливает число и добоавляет в список
    for i in list_number:
        if i > 5:
            list_number_aux.append(i)  # выписываем числа выше пяти в другой список
    return sum(list_number_aux)  # и возвращаем их сумумм


def task622d(number):
    list_number = []  # список где будет лежать распиленное на цифры число
    list_number_aux = []  # список из списка, где будут подходящие числа (выше 7)
    alt_number = str(number)  # число в виде строки
    for digit in alt_number:
        list_number.append(int(digit))  # функция что распиливает число и добоавляет в список
    for i in list_number:
        if i > 7:
            list_number_aux.append(i)  # выписываем числа выше пяти в другой список
    return np.prod(list_number_aux)  # и возвращаем их произведение


def task622e(number):
    list_number = []  # список где будет лежать распиленное на цифры число
    list_number_aux = []  # список из списка, где будут подходящие числа (выше 7)
    alt_number = str(number)  # число в виде строки
    for digit in alt_number:
        list_number.append(int(digit))  # функция что распиливает число и добоавляет в список
    for i in list_number:
        if i == 0:
            list_number_aux.append(i)  # считаем нолики
    for i in list_number:
        if i == 5:
            list_number_aux.append(i)  # считаем однёрки
    return len(list_number_aux)  # и возвращаем длинну списка с выписынамми числами


def task628a(number):
    string_number = str(number)  # переводим число в строку
    index_number = (string_number.index(max(string_number)))
    return index_number - len(string_number)  # разница между двумя числами покажет где нужное число с конца


def task628b(number):
    string_number = str(number)  # переводим число в строку
    return (string_number.index(min(string_number))) + 1  # +1 чтобы компенсировать отсчёт с нуля


def task630(number, target):
    string_number = str(number)  # переводим число в строку
    index_number = (string_number.index(str(target)))  # указывает индекс самой левой (первой) 8-ки
    return index_number - len(string_number)  # разница между двумя числами покажет где нужное число с конца
    return 0


def task631(number):
    string_number = str(number)  # переводим число в строку
    target = max(string_number)  # ищем наибольшую цифру
    times = 0  # тут будет считаться сколько раз мы нашли целевую цифру
    for i in string_number:
        if i == target:  # сканируем стринг на предмет целоевого числа - 8-ки
            times = times + 1  # и записываем каждое совпадение в переменную
    return times  # после чего возвращем что получилось


def task632(number):
    string_number = str(number)  # переводим число в строку
    target = min(string_number)  # ищем наименьшую цифру
    times = 0  # тут будет считаться сколько раз мы нашли целевую цифру
    for i in string_number:
        if i == target:  # сканируем стринг на предмет целоевого числа - 2-ки
            times = times + 1  # и записываем каждое совпадение в переменную
    return times  # после чего возвращем что получилось


def task633(number):
    number_list = []  # здесь будут записны подходящие числа
    for i in range(1, number, 1):
        if (i % 13) == 0:  # ищем кратные 13
            number_list.append(i)  # и фиксируем их тут
    return number_list  # после чего ввозвращаем


def task643(seq):
    return len(list(dict.fromkeys(seq)))  # превращает список в словарь, где нет дублей, и возврщает длинну


def task643b(seq):
    temp = [0]  # временный список где будут храниться цифры для счёта, для удобства он не пустой
    count = 0  # здесь будет вестись счёт сколько раз встретилиьс дубли
    for i in seq:
        temp.append(i)
        if i == temp[-2]:  # когда в список пишется последнее число, оно сравнивается с предпоследним
            count = count + 1  # и если они одинаковые, то счётчтик тикает на один вверх
    return count  # и возвращает что набежало


def task651(number):
    str_number = str(number)  # конвертим в строку
    if str_number[::-1]:  # и пробуем её прочесть наоборот
        return True


def task653(number):
    list = []
    str_number = str(number)
    str_number_inv = str_number[::-1]
    for i in str_number_inv:
        list.append(int(i))  # кое как обратили число и превратили в список цифр
    return all(i < j for i, j in zip(list, list[
                                           1:]))  # можно просчитать два числа разом, одно начав с начала списка, другое со второй позиции


def task654(number):
    list = []
    str_number = str(number)
    str_number_inv = str_number[::-1]
    for i in str_number_inv:
        list.append(int(i))  # кое как обратили число и превратили в список цифр
    return all(i > j for i, j in zip(list, list[
                                           1:]))  # можно просчитать два числа разом, одно начав с начала списка, другое со второй позиции


def task655(number):
    list = []
    str_number = str(number)
    for i in str_number:
        list.append(int(i))  # кое как обратили число и превратили в список цифр
    return all(i > j for i, j in zip(list, list[
                                           1:]))  # можно просчитать два числа разом, одно начав с начала списка, другое со второй позиции


def task656(number):
    list = []
    str_number = str(number)
    for i in str_number:
        list.append(int(i))  # кое как обратили число и превратили в список цифр
    return all(i < j for i, j in zip(list, list[
                                           1:]))  # можно просчитать два числа разом, одно начав с начала списка, другое со второй позиции


def task657(number, seq):
    absolute_difference_function = lambda list_value: abs(
        list_value - number)  # делаем лямбду что будет вычитать из каждого элемента списка ключевое число
    return min(seq,
               key=absolute_difference_function)  # пропустив последовательность через эту лямбду выдаём минимальное значение


def task658(seq):
    temp_list = []  # временный список для счёта чисел в последоватлеьности
    for i in seq:
        if i > 0:
            temp_list.append(i)  # если число положительное, то пишем его в список
        if i < 0:
            return len(
                temp_list)  # если вдруг нет, то возвращаем длинную списка положительных до него и так получим позицию первого отрицательно числа


def task660(seq):
    temp_list = []  # временный список для счёта чисел в последоватлеьности
    for i in seq:
        if (i % 10) != 7:
            temp_list.append(i)  # если число не кончается на 7, то пишем его в список и идём дальше
        if (i % 10) == 7:
            return len(
                temp_list)  # если вдруг кончается на 7, то возвращаем длинную списка положительных до него и так получим позицию


def task661(seq):
    temp_list = []  # временный список для счёта чисел в последоватлеьности
    for i in seq:
        if (i % 7) != 0:
            temp_list.append(i)  # если число не кончается на 7, то пишем его в список и идём дальше
        if (i % 7) == 0:
            return len(
                temp_list)  # если вдруг кончается на 7, то возвращаем длинную списка положительных до него и так получим позицию


def task666(seq):
    temp_list_i = []  # первый временный список для счёта
    temp_list_j = []  # второй временный список для счёта
    for i, j in zip(seq, seq[1:]):  # пускаем последовательность разом через два цикла, с первой и второй позиции разом
        if i != j:
            temp_list_i.append(i)
            temp_list_j.append(
                j)  # если значения в двух циклах не совпадают, то записываем их результаты в два отдельных списка
    for i, j in zip(seq, seq[1:]):
        if i == j:
            temp_list_j.pop(j)  # когда совпадение находиться удаляем последнее значение из второго списка
            return len(temp_list_i), len(temp_list_j)  # и тогда длинна обоих списков укажет позиции одинаковых чисел


def task669(seq):
    temp_list_j = []  # временный список для счёта
    for i, j in zip(seq, seq[1:]):  # пускаем последовательность разом через два цикла, с первой и второй позиции разом
        if i < j:
            temp_list_j.append(
                j)  # если значения в первой позиции меньше, чем во второй, значит счёт растёт и и дём дальше
    for i, j in zip(seq, seq[1:]):
        if i <= j:
            temp_list_j.append(j)  # если вдруг перестаёт расти, то делаем последнюю запись
            return len(temp_list_j)  # и считаем сколько позиций было записано ранее, это и будет позиция


def task677(number, a, b):
    fib_list = []
    fib1, fib2 = 1, 1
    for i in range(999):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib1)  # генерируем число фибоничи
    if number in fib_list:
        return number  # если нашли число в списке, то возвращаем его, это будет контрольная проверка


def task686(number, a, b):
    number_list = [int(x) for x in str(number)]  # здесь число будет в виде списка нарезано
    inverse_list = number_list[::-1]  # инвертируем список, чтобы было удобнее считать справо
    pos_a = inverse_list.index(a)  # находим позицию для инверсированного списка для А
    pos_b = inverse_list.index(b)  # находим позицию для инверсированного списка для Б
    if pos_a < pos_b:
        return a  # если а меньше б, то значит она правее
    return b  # если нет, значит правее б

def task6105(a, b):
    log = []
    sidemax = max(a, b)  # выбираем наибольшую сторону
    sidemin = min(a, b)  # выбираем наименьшую сторону
    r = 0 #тут будем временно хранить число повторов одного квадрата
    for j in range(1, 99, 1): #это чтобы код повторялся до победного
        square = min(sidemax, sidemin) #выберем сторону квадрата = наименьшей текущей стороны прямоугольника
        while sidemax >= square and sidemin >= square:
            sidemax = sidemax - square  # кромсаем прямоугольник сбоку пока можно
            r = r + 1 #не забывая считать сколько уже раз отрезали
            if sidemax < square or sidemin < square:  # а когда стоновится нельзя
                log.append((r, square))  # записываем сколько кусков отрезали на сей момент
                r = 0 #и забываем кол-во раз, после чего цикл потвориться с уже изменённым прямоугольником
            break
    return log

def task6108(n):
    b64 = n // 64 #по очереди делаем целостное деление и смотрим остаток, сколько не может отдать большой купюрой
    n = n % 64
    b32 = n // 32
    n = n % 32
    b16 = n // 16
    n = n % 16
    b16 = n // 16
    n = n % 16
    b8 = n // 8
    n = n % 8
    b4 = n // 4
    n = n % 4
    b2 = n // 2
    n = n % 2
    b1 = n // 1
    n = n % 1
    return [('B64', b64), ('B32', b32), ('B16', b16), ('B8', b8), ('B4', b4), ('B2', b2), ('B1', b1)] #возвращаем номинации банкот вместе с их количеством

def task825(numbers):
    howmany = 0 #временная переменная для текущего кол-ва делителей
    total = [] #временный список для записанных делителей
    for n in numbers: #просчитываем все числа списка
        for i in range(1, 999, 1): #выборка всех разумных чисел чтобы проверить подходят ли они как делитель
            if n % i == 0: #если подходят
                howmany += 1 #добавляем однёрку в переменную
        total.append(howmany) #конечный результат в текущем цикле пишем в список
        howmany = 0 #и обнуляем его, прежде чем начать по-новой
    return total

def task829(numbers):
    howmany = 0 #временная переменная для текущего кол-ва делителей
    total = [] #временный список для записанных делителей
    for n in numbers: #просчитываем все числа списка
        for i in range(1, 999, 1): #выборка всех разумных чисел чтобы проверить подходят ли они как делитель
            if n % i == 0: #если подходят
                howmany += 1 #добавляем однёрку в переменную
        total.append(howmany) #конечный результат в текущем цикле пишем в список
        howmany = 0 #и обнуляем его, прежде чем начать по-новой
    indexes = [i for i, x in enumerate(total) if x == 4] #после считаем кол-во 4ок и находим их индексы
    return [numbers[x] for x in indexes] #и возвращем индексы согласно списку чисел

def task832(numbers):
    howmany = 0 #временная переменная для текущего простых чисел
    total = [2, ] #временный список для найденых простых чисел
    for n in range(1, 9999, 1): #проверяем все числа подряд
        for i in range(2, 999, 1): #выборка всех разумных чисел чтобы проверить подходят ли они как делитель
            if n * n <= i and i % n != 0: #если число подходит под определиние простого числа
                howmany += 1 #добавляем однёрку в переменную для счёта простных чисел
                total.append(i) #и запоминаем текущие правильное число
                if howmany == 10: #когда цикл удачно сходит 10 раз
                    return total #возвращаем

def task835(number1, numbers2):
    temp = []
    a = 0
    for i in range(number1, numbers2, 1):
        for j in range(2, 999, 1):
            if i % j == 0:
                a += j
        if a % 10 == 0:
            temp.append(i)
        a = 0
    return temp

def task836(limit):
    sum = 0 #временная переменная где будет сумма числа
    perfect_numbers = []
    for n in range(1, limit, 1): #берём диапозон чисел, для определения соврешнности
        for i in range(1, limit, 1): #перебор возможных делителей
            if (n % i == 0):# если число делится на делитель без остатка
                sum = sum + i #запоминаем текущий делитель
                if (sum == n): #и если оно ровно самому числу
                    perfect_numbers.append(n) #радуемся, оно подходит и вносится в список
        sum = 0 #обнуляем переменную от греха
    return perfect_numbers #и возвращаем что вышло

def task92(team):
    print(team, "— это чемпион!")
    return 1

def task975a(sentence):
    temp = 0 #временный счётчик
    for i in sentence:
        temp +=1 #cчитаем проход через каждую букву
        if i == ',': #и когда наступает запятая
            print(sentence[0:temp]) #запоминаемт когда это было и отрезаем предложение до этой длинны
            return sentence[0:temp]

def task976b(sentence):
    es = [] #тут будут хранится номера букв е
    temp = 0 #временный счётчик
    for i in sentence:
        temp +=1#cчитаем проход через каждую букву
        if i == 'е': #запоминаем каждую е в отдельности и пишем в список
            es.append(temp)
    return es[-1] #после возвращаем его последнее число

def task989(sentence):
    for i in sentence:
        if i == 'с':
            return 'с'
        if i == 'т':
            return 'т'

def task991(sentence):
   return sentence.replace(' ', '_')

def task992(sentence):
    return ''.join("ы" if i % 2 == 0 else char for i, char in enumerate(sentence, 1))

def task993(sentence):
    new = ''.join("а" if i % 3 == 0 else char for i, char in enumerate(sentence, 1))
    new2 = ''.join("а" if i % 6 == 0 else char for i, char in enumerate(new, 1))
    new3 = ''.join("а" if i % 9 == 0 else char for i, char in enumerate(new2, 1))
    return new3

def task9100(sentence):
    a = sentence[1] #запоминаем позицию 2
    b = sentence[4] #запоминаем позицию 5
    new = list(sentence) #конвертируем в список
    new[1] = b #по одной заменяем те же позиции запомненным ранее
    new[4] = a
    return ''.join(new) #и возвращаем запомненным ранее

def task9101(sentence):
    a = sentence[2] #запоминаем позицию 3
    b = sentence[-1] #запоминаем позицию последнюю
    new = list(sentence) #конвертируем в список
    new[2] = b #по одной заменяем те же позиции запомненным ранее
    new[-1] = a
    return ''.join(new) #и возвращаем запомненным ранее

def task9102(sentence, posa, posb):
    posa = posa - 1 #поправка на отсчёт с нуля
    posb = posb - 1 #поправка на отсчёт с нуля
    a = sentence[posa] #запоминаем позицию 1
    b = sentence[posb] #запоминаем позицию 5
    new = list(sentence) #конвертируем в список
    new[posa] = b #по одной заменяем те же позиции запомненным ранее
    new[posb] = a
    return ''.join(new) #и возвращаем запомненным ранее

def task9103(sentence):
    odd = list(sentence)[0::2] #сперва берём нечётные буквы
    evn = list(sentence)[1::2] #потом чётные
    tmp = [] #временный список
    for i, j in zip(evn, odd): #берём оба списка разом, но сперва чётные, потом нечётные
        tmp.append(i) #и записываем и то
        tmp.append(j) #и другое
    return ''.join(tmp) #превращаем список в строку и возвращаем

def task9104(sentence):
   return sentence[::-1] #это тупо слово наоборот выходит по всем условиям

def task9105(sentence):
   first = sentence[:2] #первые две буквы взять
   second = sentence[2:8] #и с третьей по девятую
   third = sentence[9:] #и с десятой до конца
   second_a = second[::-1] #обращаем среднюю часть
   return ''.join([first, second_a, third]) #и возвращем что получится

def task9106(sentence, first, last):
   a = first #позиция первой ключевой буквы
   b = last - 1 #позиция последней ключевой буквы с поправкой на тсчёт с нуля
   first = sentence[:first] #отрезать от начала до первой позиции
   second = sentence[a:b] #и с третьей по девятую
   third = sentence[b:] #отрезать от конца до второй позиции
   second_a = second[::-1] #обращаем среднюю часть
   return ''.join([first, second_a, third]) #и возвращем что получится

def task9107(sentence, buka, buko):
    len_a = 0 #переменная для хранения координат а
    len_o = 0 #переменная для хранения координат о
    for i in sentence:
        len_a += 1 #ведём счёт
        if i == 'а': #и прерываем его завидев а
            break
        if len_a == len(sentence):
            return sentence #если искомой буквы нет до самого конца слова, то возвращаем слово как есть
    for i in sentence: #ведём счёт
        len_o += 1
        if i == 'о':  #и прерываем его завидев о
            break
        if len_o == len(sentence):
            return sentence #если искомой буквы нет до самого конца слова, то возвращаем слово как есть
    tmp1 = list(sentence) #превращем слово в список
    tmp1[len_a-1] = buko #чтобы заменить в нём а на о
    tmp1[len_o-1] = buka # и заменить в нём о на а
    return ''.join(tmp1) #возвращаем, что получилось.

def task9108b(sentence):
    return sentence.replace("фф", "ф") #заменить произвольный текст в строке и сразу вернуть

def task9109b(sentence, k):
    index = k - 1 #поправка на то что индекс считается от нуля
    if len(sentence) > index: #если К не больше самого слова
        return sentence[0:index:] + sentence[index + 1::] #можно взять часть слово до и после индекса и склеить, миновав сам индекс

def task9111(sentence):
    length = len(sentence) #запоминаем длинну слова
    if length % 2 == 0: #если она чётная, то
        index = int(length / 2) - 1 #находим половину длинны и делаем поправку на отсчёт индекса с нуля
        return sentence[0:index:] + sentence[index + 2::] #берём части слова до индекса и через два знака от него и склеиваем
    else:
        index = int((length / 2) + 0.5) - 1 #если длинна нечётная, то делаем окргуление, кроме поправки на отсчёт с нуля
        return sentence[0:index:] + sentence[index + 1::] #берём части слова до индекса и через один знак от него и склеиваем

def task9111b(sentence):
    length = len(sentence) #запоминаем длинну слова
    if length % 2 == 0: #если она чётная, то
        index = int(length / 2) - 1 #находим половину длинны и делаем поправку на отсчёт индекса с нуля
        return sentence[0:index:] + sentence[index + 2::] #берём части слова до индекса и через два знака от него и склеиваем
    else:
        index = int((length / 2) + 0.5) - 1 #если длинна нечётная, то делаем окргуление, кроме поправки на отсчёт с нуля
        return sentence[0:index:] + sentence[index + 1::] #берём части слова до индекса и через один знак от него и склеиваем

def task9112(sentence, n1, n2):
    index1 = n1 - 1 #конвертируем  индексы с поправкой на отсчёт с нуля
    index2 = n2 - 1
    return sentence[0:index1:] + sentence[index2 + 1::] #берём всё что до и после них двоих и склеиваем воедино

def task9115(sentence):
    listed = [] #здесь будет предложение в виде списка
    temp = 0 #счётчик
    for i in list(sentence):
        temp +=1 #считаем циклы
        if i == 'о' and (temp / 2) != 0: #если есть нечётная О, то проускаем её
            print(temp)
        else:
            listed.append(i) #во всех прочих случаях пишем в список
    return ''.join(listed) #потом превращаем список в строку и возвращаем

def task9114(sentence):
    myList = list(sentence)#превращем слово в список
    myList = list(dict.fromkeys(myList)) #а список в словарь, который не может содержать дубли
    return ''.join(myList) #и вуаля

def task9153(sentence):
    l1 = list(sentence) #превращаем текст в список символов
    repeat = [] #тут будут повторяющееся буквы
    for i, j in zip(l1, l1[1:]): #парно сравнивая с помощью двух циклов ищем когда буквы бывают совпадают подряд
        if i == j:
            repeat.append(j)  #и все случаи когда буквы идёт второй раз или более записываем
    r_element = max(set(repeat), key=repeat.count) #смотрим какой элемент в списке наиболее частый
    return repeat.count(r_element) + 1 #и считаем сколько раз этот элемент был в списке. +1 нужен для компенсации, так как изначально в тексте искались только повторы, без первого появления знака

def task9155(sentence):
    l1 = [] #временный список
    for k in sentence:
        for i in sentence:
            if i == k:
                l1.append(i) #цикл в цикле одну букву за другой сравнивает с другими буквами по очереди
    return max(set(l1), key=l1.count)  # смотрим какой элемент в списке наиболее частый

def task9156(w1, w2):
    temp = []
    dick = (dict.fromkeys(w2)) #превращем второе слово в простой словарь без дублей
    for i in w1:
        if i in dict.keys(dick): #с помощью цикла проходим по всем буквам и узнаём есть ли они в словаре
            temp.append(1) #если нет пишем правду
        else:
            temp.append(0) #и если нет пишем ложь в список
    return temp #который возвращаем

def task9157(w1, w2):
    temp = []
    dick2 = (dict.fromkeys(w2)) #превращем второе слово в простой словарь без дублей
    dick1 = (dict.fromkeys(w1)) #превращем первое слово в простой словарь без дублей
    for i in dick1:
        if i in dict.keys(dick2): #с помощью цикла проходим по всем буквам и узнаём есть ли они в словаре
            temp.append(1) #если нет пишем правду
        else:
            temp.append(0) #и если нет пишем ложь в список
    return temp #который возвращаем

def task9158(w1, w2):
    onelist = list(w1+w2) #превращем оба слова в набор букв
    dick = list(dict.fromkeys(onelist)) #убираем все дубли превращая временно в список
    a = np.array(onelist) #превращаем оба списка в массив
    b = np.array(dick) #
    c = a - b #так получаем список лишних букв у которых есть дубли
    return a - c #и удаляем эти дубли из чистого объеденённого списка

def task9184(sentence):
    temp1 = [] #временные списки для подсчёта разных скобок
    temp2 = []
    for i in sentence:
        if i == '(':
            temp1.append(i) #все открывающие в одну кучку
        if i == ')':
            temp2.append(i) #а закрывающие во вторую
    if len(temp1) == len(temp2) and len(set(temp1)) == 1 and len(set(temp2)) == 1: #если обе кучки одного размера и в каждой только по одному виду скобок, значит всё стоит верно
        return 1
    else: #а если нет, то нет
        return 0

def task9184b(sentence):
    temp1 = [i for i, x in enumerate(sentence) if x == "("] #засекаем индексы всех скобок одного вида в отдельыне списки
    temp2 = [i for i, x in enumerate(sentence) if x == ")"]
    if len(temp1) < len(temp2):
        temp1.append(len(sentence)) #для равной длинны этих списков к более короткому добавляем число равное длинее предложения
    else:
        temp2.append(len(sentence))
    for i, j in zip(temp1, temp2): #разом проходим оба списка и смотрим где закрывающая скобка имеет меньший индекс, чем отркывающая
        if i >= j:
            return j +1 #добавим однёрку для компенсации отсчёта с нуля и будет место, где первая лишняя скобка

def task9185(sentence): #ультимативная и полная версия подобного задания
    temp1i = [i for i, x in enumerate(sentence) if x == "("] #засекаем индексы всех скобок одного вида в отдельыне списки
    temp2i = [i for i, x in enumerate(sentence) if x == ")"]
    if len(temp1i) > len(temp2i):
        return len(temp1i) - len(temp2i) #если открывающих скобок больше, чем закрывающих, то сравним число попаданий узнаем насколько именно больше /ВАРИАНТ А
    if len(temp1i) == len(temp2i): #если и там одно число попаданий, возможно скобки стоят правильно
        for i, j in zip(temp1i, temp2i):  #разом проходим оба списка и убеждаемся что всё норм
            if i < j:
                return 'ok' #и возвращаем ок если да /ВАРИАНТ Б
    if len(temp1i) < len(temp2i): #если закрывающих больше, то нужно найти индекс лишней
        temp1i.append(len(sentence)) #добавим в список закрывающих длинну предложения, чтобы списки были равной длинны
    for i, j in zip(temp1i, temp2i): #разом проходим оба списка и смотрим где закрывающая скобка имеет меньший индекс, чем отркывающая
        if i >= j:
            return j + 1 #добавим однёрку для компенсации отсчёта с нуля и будет место, где первая лишняя скобка /ВАРИАНТ С

def task9187(number):
    num = str(number)
    one = ""
    two = ""
    thr = ""
    fou = ""
    if num[0] == '1': #пошли тыщи
        one = "одна тысяча"
    if num[0] == '2':
        one = "две тысячи"
    if num[0] == '3':
        one = "три тысячи"
    if num[0] == '4':
        one = "четыре тысячи"
    if num[0] == '5':
        one = "пять тысяч"
    if num[0] == '6':
        one = "шесть тысяч"
    if num[0] == '7':
        one = "семь тысяч"
    if num[0] == '8':
        one = "восемь тысяч"
    if num[0] == '9':
        one = "девять тысяч"
    if num[1] == '1': #пошли сотни
        two = "сто"
    if num[1] == '2':
        two = "двести"
    if num[1] == '3':
        two = "триста"
    if num[1] == '4':
        two = "четыреста"
    if num[1] == '5':
        two = "пятьсот"
    if num[1] == '6':
        two = "шестьсот"
    if num[1] == '7':
        two = "семьсот"
    if num[1] == '8':
        two = "восемьсот"
    if num[1] == '9':
        two = "девятьсот"
    if num[2] == '2': #пошли десятки
        thr = "двадцать"
    if num[2] == '3':
        thr = "тридцать"
    if num[2] == '4':
        thr = "сорок"
    if num[2] == '5':
        thr = "пятьдесят"
    if num[2] == '6':
        thr = "шестьдесят"
    if num[2] == '7':
        thr = "семьдесят"
    if num[2] == '8':
        thr = "восемьдесят"
    if num[2] == '9':
        thr = "девяносто"
    if num[3] == '0': #пошли однёрки
        fou = ""
    if num[3] == '1':
        fou = "один"
    if num[3] == '2':
        fou = "два"
    if num[3] == '3':
        fou = "три"
    if num[3] == '4':
        fou = "четыре"
    if num[3] == '5':
        fou = "пять"
    if num[3] == '6':
        fou = "шесть"
    if num[3] == '7':
        fou = "семь"
    if num[3] == '8':
        fou = "восемь"
    if num[3] == '9':
        fou = "девять"
    if num[-2:] == '10': #пошли особо запущенные случаи
        fou = "десять"
        thr = '' #в таких случаях пропись третьего числа заменяется ничем, а четвёртое заменяет собой оба
    if num[-2:] == '11':
        fou = "одинадцать"
        thr = ''
    if num[-2:] == '12':
        fou = "двенадцать"
        thr = ''
    if num[-2:] == '13':
        fou = "тринадцать"
        thr = ''
    if num[-2:] == '14':
        fou = "четырнадцать"
        thr = ''
    if num[-2:] == '15':
        fou = "пятнадцать"
        thr = ''
    if num[-2:] == '16':
        fou = "шестнадцать"
        thr = ''
    if num[-2:] == '17':
        fou = "семнадцать"
        thr = ''
    if num[-2:] == '18':
        fou = "восемнадцать"
        thr = ''
    if num[-2:] == '19':
        fou = "девятнадцать"
        thr = ''
    return one + ' ' + two + ' ' + thr + ' ' + fou

def task121(ar0):
    print(ar0[0][-1])
    return (ar0[0][-1])

def task121b(ar0):
    print(ar0[1][0])
    return (ar0[1][0])

def task123a(ar0, inp):
    inp_shift = inp - 1 #поправка на отчёт с нуля
    print(ar0[1][inp_shift])
    return (ar0[1][inp_shift])

def task125b(ar0, inp):
    answer = [] #временный список на потом
    inp_shift = inp - 1  # поправка на отчёт с нуля
    print(ar0[:,inp_shift]) #вывод стобла массива в numpy
    for i in ar0[:,inp_shift]:
        answer.append(i) #костыль чтобы конечные цифры были в удобном формате
    return answer

def task127a(ar0, inp):
    inp_shift = inp - 1  # поправка на отчёт с нуля
    ar0[1, inp_shift] = 150
    return ar0[1, inp_shift]

def task128a(ar0, inp):
    inp_shift = inp - 1  # поправка на отчёт с нуля
    ar0[inp_shift, 1] = 13
    return ar0[inp_shift, 1]

def task129a(ar0, inp): #stub
    inp_shift = inp - 1  # поправка на отчёт с нуля
    ar0[inp_shift, 1] = 13
    return ar0[inp_shift, 1]

def task1222(ar0):
    ar0.fill(0) #заполнить таблицу числами чтобы она была на что-то похожа
    ar0 = np.delete(ar0, np.s_[0:10], axis = 0) #и в принципе сразу удалить все ряды
    temp = []
    for i in range(1, 11): #для таблицы умножения берём цифры от 1 до 10 включительно
        for j in range(1, 11):
            temp.append(i * j) #потихоньку перемножаем между собой числа 1-10 десять раз
            if len(temp) == 10: #каждый раз когда временный список достигает десяти
                ar0 = np.vstack((ar0, temp))#записываем его в массив
                temp = [] #и обнуляем список, когда начинается обсчёт следующего первого числа
    return ar0[9, 9] #последнее число таблицы умножения для проверки

def task1223v(ar0):
    ar0.fill(1) #заполнить таблицу числами чтобы она была на что-то похожа
    ar0[1, 0] = 0 #один способ заполнения массива
    ar0[1, 6] = 0
    np.put(ar0[2], [0, 1, 5, 6], [0]) #другой способ (после ar0 указываем [строку] и заполняем линейно)
    np.put(ar0[3], [0, 1, 2, 4, 5, 6], [0])
    np.put(ar0[4], [0, 1, 5, 6], [0])
    np.put(ar0[5], [0, 6], [0])
    return list(ar0[5])#предпоследний ряд для сравнения

def task1224(ar0):
    ar0.fill(1) #заполнить таблицу числами чтобы она была на что-то похожа
    temp = []
    for i in range(1, 7, 1): #код генерирующий просту последовательность для первой строки масива
        temp.append(i)
    ar0[0] = temp
    n = 0 #код генерирующий более сложную последоватлеьность с линейно растущим паттерном прибавления для второй строки
    temp = []
    for i in range(1, 7, 1):
        n += i
        temp.append(n)
    ar0[1] = temp
    temp = [] #код генерирующий более сложную театрадальную последоватлеьность с линейно растущим паттерном прибавления для 3ей строки
    for i in range(1, 7, 1):
        a = i * ((i + 1) * (i + 2)) / 6
        temp.append(int(a))
    ar0[2] = temp
    ar0[3] = [1, 5, 15, 35, 70, 726] #короче остальные ряды тоже
    ar0[4] = [1, 6, 21, 56, 126, 252]
    return temp

def task1225a(ar0):
    ar0.fill(0) #заполнить таблицу числами чтобы она была на что-то похожа
    temp = []
    a = 0
    for i in range(1, 121, 1): #считаем от 1 до 120
        temp.append(i) #записываем каждое число в список
        if len(temp) == 4: #и едва список будет содержать 4 цифры
            ar0[a] = temp #включаем его в текущую строчку массива
            a += 1 #и переходим на след строку массива
            temp = [] #и очищаем временный список
    return ar0[-1, -1] #возвращаем последнее число для проверки

def task1226a(ar0, n):
    ar0.fill(0) #заполнить таблицу числами чтобы она была на что-то похожа
    a = -1 #временный число для отсчёта
    n2 = int(n / 2) #половина числа n правильного вычесления цикла
    for i in range(0, n2, 1):
        a += 1
        ar0[a, 1::2] = 1 #сперва заполняем единичками чётные позиции в нечётных строках
        a += 1
        ar0[a, 0::2] = 1 #и наоборот
    return ar0[-1, -1] #возвращаем последнее число для сравнения

def task1227(ar0, ls0, n, m):
    ar0.fill(0) #заполнить таблицу числами чтобы она была на что-то похожа
    ls0.fill(1) #заполнить таблицу числами чтобы она была на что-то похожа
    tact = 0 #временный счётчик
    temp = [] #временный список
    for i in ls0[0]: #берём одномерный массив
        temp.append(i) #и добавляем его в спиоск
        if len(temp) == len(ar0[0]): #если длинна списка равна длинее строки массива
            ar0[tact] = temp #то записываем его в первую строку
            tact += 1 #повышаем счётчки строки
            temp = [] #обнуляем список и опять сначала
    return ar0[-1, -1] #возвращаем последнее число для сравнения

def task1232a(ar0):
    return list(ar0[2, ::-1]) #берём нас массив и читаем третью стркоу задом наперёд

def task1232b(ar0, k):
    k = k - 1 #поправка на отсчёт с нуля
    return(list(ar0[::-1, k])) #берём нас массив и читаем третью стркоу задом наперёд

def task1234a(ar0):
    temp = [] #здесь будет временный список
    takt = 0 #временный счётчик
    for i in range(1, len(ar0[0]) + 1, 1): #создаём цикл длинную в колво строк массива
        temp.append(list(ar0[takt, ::-1])) #с помощью счётчика считаем строку за строкой задом наперёд
        takt += 1 #отсчитываем счётчик каждый цикл
    return temp

def task1234b(ar0):
        temp = [] #здесь будет временный список
        takt = 0 #временный счётчик
        for i in range(1, 9, 1): #создаём длинный цикл
            temp.append(list(ar0[takt, ::-1])) #с помощью счётчика считаем строку за строкой задом наперёд
            takt += 1  # отсчитываем счётчик каждый цикл дважды
            if takt == len(ar0[0]): #и когда кол-во тактов сошлось с высотой массива
                return temp #возвращаем что получилось
            temp.append(list(ar0[takt]))
            takt += 1 #дублирем это дело
            if takt == len(ar0[0]):
                return temp


def task1265(ar0):
    avg1 = np.average(ar0[0])
    avg2 = np.average(ar0[1])
    avg3 = np.average(ar0[2])
    avgmax = max(avg1, avg2, avg3)
    if avgmax == avg1:
        return 1
    if avgmax == avg2:
        return 2
    if avgmax == avg3:
        return 3

def task1285(ar0):
    return (np.argmin((ar0[0:,1])) +1) #хитрая команда, что сразу показывает индекс минимального элемента в нужном вертикальном срезе массива

def task1285b(ar0):
    a = (np.argmin((ar0[0:,-1]))) #хитрая команда, что сразу показывает индекс минимального элемента в нужном вертикальном срезе массива
    return len(ar0[0:,-1]) - a #вычитаем из результата высоту массива, чтобы индекс, фактически, считался от конца, а не начала.

def task1289c(ar0):
    min = np.where(ar0 == np.amin(ar0))
    a = list(min[0])
    b = list(min[0])
    c = (a, b)
    return c

def task1289d(ar0):
    a = np.where(ar0 == np.amin(ar0)) #функция нампая, что помогает найти минимальное значение в матрице
    b = list(zip(a[0], a[1])) #результаты её работы нужно слайснуть от мусора и объеденить в одно
    return b # а птом вернуть

def task1290a(ar0):
    a = np.amin(ar0, axis=1) #ахис1 позволяет искать по каждой строке
    return list(a)

def task1290c(ar0):
    a = np.where(ar0 == np.amin(ar0, axis=1)) #ахис1 позволяет искать по каждой строке по координатам
    return list(a[1]) #слайснуть нужный часть данных, где записаны именно коордианты и превратить в список, чтобц удобнее возвращать

def task1291c(ar0):
    a = np.where(ar0 == np.amin(ar0, axis=0)) #ахис0 позволяет искать по каждой стоблце по координатам
    return list(a[0]) #слайснуть нужный часть данных, где записаны именно коордианты и превратить в список, чтобц удобнее возвращать

def task1293(ar0):
    a = list(np.sum(ar0, axis=1)) #функция нампай, что помогает суммировать каждую строку (по оси1)
    return max(a) #ранее сконвертированный в список результата возвращем с одинм макс значением

def task1295a(ar0):
    row_sums = ar0.sum(axis=1) #позволяет найти суммы каждой строки
    return max(row_sums) #и возвращаем из них максимальнео значение

def task1296(ar0):
    row_sums = ar0.sum(axis=1) #позволяет найти суммы каждой строки
    row_sums = row_sums[::-1] #ставим список с ног на голову, чтобы было проще найти нижнею максимальную строку
    return abs((np.argmax(row_sums)) - len(row_sums)) #позволяет указать индекс самой большой позиции, минус длинна списка, чтобы узнать нижнюю позицию с конца

def task12102(ar0):
    list0 = [] #временный список
    for i, j in zip(ar0[0], ar0[0, 1:]): #можно начать считать сразу с двух мест, нулевой и первой позиции
        list0.append(i + j) #и записывать сумму каждой пары пока не кончиться ряд
    for i, j in zip(ar0[1], ar0[1, 1:]): #тоже самое во сторой строке
        list0.append(i + j)
    return max(list0) #и ответом будет самая крупаная среди них

def task12106(ar0):
    list0 = [] #временный список
    for i, j in zip(ar0[0], ar0[0, 1:]): #можно начать считать сразу с двух мест, нулевой и первой позиции
        list0.append(i + j) #и записывать сумму каждой пары пока не кончиться ряд
    for i, j in zip(ar0[1], ar0[1, 1:]): #тоже самое во сторой строке
        list0.append(i + j)
    max_ind = np.argmax(list0)
    print(max_ind)
    prepos = (len(list0) - max_ind)
    print(prepos)
    postpos = abs(prepos - ar0.size)
    print(postpos)
    return postpos, (postpos - 1)

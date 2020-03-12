import numpy


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
            prod2.append(numpy.prod(prod))  # содержимое списка перемножается в нужную степерь и пишетсяся сюда
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
    return numpy.prod(list_number_aux)  # и возвращаем их произведение


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
    temp = [0] #временный список где будут храниться цифры для счёта, для удобства он не пустой
    count = 0 #здесь будет вестись счёт сколько раз встретилиьс дубли
    for i in seq:
        temp.append(i)
        if i == temp[-2]: #когда в список пишется последнее число, оно сравнивается с предпоследним
            count = count + 1 #и если они одинаковые, то счётчтик тикает на один вверх
    return count #и возвращает что набежало

def task651(number):
    str_number = str(number) #конвертим в строку
    if str_number[::-1]: #и пробуем её прочесть наоборот
        return True

def task653(number):
    list = []
    str_number = str(number)
    str_number_inv = str_number[::-1]
    for i in str_number_inv:
        list.append(int(i)) #кое как обратили число и превратили в список цифр
    return all(i < j for i, j in zip(list, list[1:])) #можно просчитать два числа разом, одно начав с начала списка, другое со второй позиции
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
        material_a = (a[1] / a[0]) #1
    except ZeroDivisionError:
        material_a = 0

    try:
        material_b = (b[1] / b[0]) #0.5
    except ZeroDivisionError:
        material_b = 0

    if material_a > material_b:
        return a
    else:
        return b


def task416a(a, b):
    circle_dia = (a / 3.14) ** .5 * 2 #3.181808675974975 при 2
    square_side = b ** .5 #0.5 при 4
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
    if (year % 4) != 0: #просто високосный
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
    s_table = a * b #площадь стола
    domino_a = c * d #площадь домино картинкой вверх
    domino_b = c * e  #площадь домино н лежащей на боку
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

def task469a(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start, second_hor_start, second_ver_start):
    first_hor_end = first_hor_start + first_hor_lenght
    first_ver_end = first_ver_start + first_ver_lenght
    second_ver_end = second_ver_start + second_ver_lenght
    second_hor_end = second_hor_start + second_hor_lenght
    if (second_hor_lenght >= first_hor_lenght) and (second_hor_end >= first_hor_end) and (second_ver_lenght >= first_ver_lenght) and (second_ver_end >= first_ver_end): #работает только если фигуры в положительном диапозоне
        return True
    return False

def task469(first_hor_lenght, first_ver_lenght, second_hor_lenght, second_ver_lenght, first_hor_start, first_ver_start, second_hor_start, second_ver_start):
    first_hor_end = first_hor_start + first_hor_lenght
    first_ver_end = first_ver_start + first_ver_lenght
    second_ver_end = second_ver_start + second_ver_lenght
    second_hor_end = second_hor_start + second_hor_lenght
    if first_hor_start > second_hor_end and first_ver_start > second_ver_end:
        return "не пересекаются" #задание В, что не пересекаются вовсе
    if second_hor_start > first_hor_end and second_ver_start > first_ver_end:
        return "не пересекаются" #задание В, что не пересекаются вовсе
    if (second_hor_lenght >= first_hor_lenght) and (second_hor_end >= first_hor_end) and (second_ver_lenght >= first_ver_lenght) and (second_ver_end >= first_ver_end): #работает только если фигуры в положительном диапозоне
        return "второй принадлежит первому" #задание А, что второй вписывается в первый
    if (first_hor_lenght >= second_hor_lenght) and (first_hor_end >= second_hor_end) and (first_ver_lenght >= second_ver_lenght) and (first_ver_end >= second_ver_end): #работает только если фигуры в положительном диапозоне
        return "первый принадлежит второму" #задание Б, покрывает вариант и что первый вписывается во второй
    return "пересекаются частично"

def task4100(first, second, third):
    if first < second and first < third:
        a = first #если первое число - первое наименьшее
        if second < third:
            b = second #если второе число - второе наименьшее
        if third < second:
            b = third #если третье число - второе наименьшее
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
    for i in range(start, end, step): #печать таблицы умножения
        quotient = i * 7
        print(f"{quotient} X 7 = {i}.")
    for i in range(start, end, step): #просчёт результата для сверки
        result.append(i * 7)
    return result
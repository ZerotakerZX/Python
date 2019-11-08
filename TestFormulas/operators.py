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
   if (number // 100) == (number // 10 % 10) or (number // 10 % 10) == (number % 10) or (number // 100) == (number % 10):
        return True
   return False
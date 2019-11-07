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
    material_a = (a[1] / a[0]) #1
    material_b = (b[1] / b[0]) #0.5
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
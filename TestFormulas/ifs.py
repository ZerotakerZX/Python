def solution327a(x, y):
    return x > 2 and y > 3


def solution327b(x, y):
    return x > 1 or y > -2


def solution327b(x, y):
    return x > 1 or y > -2


def solution327z(x):
    return x > 10 and x <= 20


def solution328b(a, b):
    return ((a % 2) == 0) ^ ((b % 2) == 0)


def solution328g(a, b, c):
    return ((a % 3) == 0) and ((b % 3) == 0) and ((c % 3) == 0)


def solution330b(a):
    #    if (a % 3) != 0 and (a % 10) == 0: старый код
    #        return True
    return ((a % 3) != 0) and ((a % 10) == 0)


def solution332a(x, y):
    if x <= -2 and y >= 1:
        return True


def solution332b(x, y):
    if 0 <= x >= 0 and 1.5 >= y > -2:  # не нашёл подходящие регулярное выражение для x
        return True


def solution332c(x, y):
    if 1 <= x <= 2 and 0 <= y <= 4:
        return True


def solution332d(x, y):
    if x >= 1 and 2 <= y <= 4:
        return True


def solution332e(x, y):
    if x >= 1 and y <= -1:
        return True
    if x >= 2 and y >= 1:
        return True


def solution332f(x, y):
    if x >= 2 and y >= 1 or x >= 2 and y >= -1.5: #альтернативная запись через or
        return True


def solution332g(x, y):
    if 1 <= x <= 3 and -2 <= y <= -1:
        return True


def solution332z(x, y):
    if 0 <= x >= 0 and 0.5 <= y <= 1.5:
        return True
    if x >= 2 and 0 <= y >= 0:
        return True

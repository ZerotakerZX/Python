def move (figure, a, b, c, d):
    if not is_valid_grid(a, b, c, d):
        return False

    if figure == 'knight':
        return knightmove(a, b, c, d)

    return False

def is_valid_grid(a, b, c, d):
    if a < 1 or a > 8:
        return False
    if b < 1 or b > 8:
        return False
    if c < 1 or c > 8:
        return False
    if d < 1 or d > 8:
        return False

    return True

def rookmove(a, b, c, d):
    if a == c:
        return True
    if b == d:
        return True
    return False

def bishopmove(a, b, c, d):
    ac = a - c
    bd = b - d
    if abs(ac) == abs(bd):
        return True
    return False

def kingmove(a, b, c, d):
    ac = abs(a - c)
    bd = abs(b - d)
    if ac > 1 or bd > 1:
        return False
    return True

def queenmove(a, b, c, d):
    ac = abs(a - c)
    bd = abs(b - d)
    if a == c:
        return True
    if b == d:
        return True
    if ac == bd:
        return True
    return False

def knightmove(a, b, c, d):
    ac = abs(a - c)
    bd = abs(b - d)
    if ac == 1 and bd == 2:
        return True
    if ac == 2 and bd == 1:
        return True
    return False

def wpawnmove(a, b, c, d):
    if d == b + 1:
        return True
    if d == b + 1 and a == c + 1 or b == d + 1 and a == c - 1:
        return True
    return False

def bpawnmove(a, b, c, d):
    if d == b - 1:
        return True
    if d == b - 1 and a == c + 1 or b == d - 1 and a == c - 1:
        return True
    return False
def sum_all(digit):
    first = str(digit)[:1]
    second = str(digit)[1:2]
    third = str(digit)[2:3]
    fourth = str(digit)[3:]
    sum_all = int(first) + int(second) + int(third) + int(fourth)
    return sum_all

def prod_all(digit):
    first = str(digit)[:1]
    second = str(digit)[1:2]
    third = str(digit)[2:3]
    fourth = str(digit)[3:]
    int(first) * int(second) * int(third) * int(fourth)
    prod_all = int(first) * int(second) * int(third) * int(fourth)
    return prod_all
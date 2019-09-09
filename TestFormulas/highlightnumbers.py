def find_first_digit (digit, first_digit=None):
    first_digit = int(str(digit)[:1])
    return first_digit

def find_second_digit (digit):
    second_digit = digit % 10
    return second_digit

def find_prod (digit):
    first_digit = int(str(digit)[:1])
    second_digit = digit % 10
    digits_prod = first_digit * second_digit
    return digits_prod
def find_first_digit(digit):
    first_digit = digit // 10
    return first_digit

def find_second_digit(digit):
    second_digit = digit % 10
    return second_digit

def find_prod(digit):
    first_digit = int(str(digit)[:1])
    second_digit = digit % 10
    digits_prod = first_digit * second_digit
    return digits_prod

def swap_digits(digit):
    #29
    #9
    first_digit = find_first_digit(digit)
    second_digit = find_second_digit(digit)
    #92=9*10 +2
    swaped = first_digit + second_digit * 10
    return swaped

def swap_digits_alt(digit):
    return int(str(digit)[::-1])

def slice_number_singular(digit):
    return int(str(digit)[-1:])

def arbitrary_shuffle(digit):
    leftover = str(digit)[1:] #=23
    sliced = str(digit)[:1] #=1
    rejoined_string = leftover + sliced #=231
    rejoined_int = int(rejoined_string) #=231
    return rejoined_int

def arbitrary_double_shuffle(digit):
    leftover = str(digit)[1:]#=23
    swaped = leftover[::-1]#32
    first = str(digit)[:1] #=1
    rejoined_string = first + swaped #=132
    rejoined_int = int(rejoined_string) #=132
    return rejoined_int
def add(first, second):
    return first + second

def multiplication(first, second):
    return first * second

def devide(first, second):
    return first / second

def subtract(first, second):
    return first - second

def chain(first, second, third):
    nth = multiplication(second, third)
    sum = add(nth, first)
    return sum
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя! \n'


def expo(a, b):
    try:
        return a ** b
    except ZeroDivisionError:
        print('Нельзя возводить 0 в отрицательную степень! \n')


while True:
    a = int(input('Введите первое число - '))
    b = int(input('Введите второе число - '))
    x = input('Введите действие(+, -, *, /, ^) - ')
    if x == '+':
        print(plus(a, b))
    elif x == '-':
        print(minus(a, b))
    elif x == '*':
        print(mult(a, b))
    elif x == '/':
        print(div(a, b))
    elif x == '^':
        print(expo(a, b))


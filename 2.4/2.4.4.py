class my_exception(Exception):
    pass


def run_except(arg):
    try:
        if arg == 'hello world':
            raise my_exception
    except my_exception:
        print('Exception!')

while True:
    a = input('Введите строку для проверки - ')
    run_except(a)

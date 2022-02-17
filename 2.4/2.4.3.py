class Int_exception(Exception):
    pass


class Str_exception(Exception):
    pass


def has_string_symbols(string, symbols):
    for symbol in symbols:
        if symbol in string:
            return True

    return False


def user_name_check_loop():
    while True:
        user_string = input("Введите имя: ")
        if has_string_symbols(user_string, int_list):
            raise Int_exception('Имя не должно содержать цифры')
        else:
            return user_string

def user_surname_check_loop():
    while True:
        user_string = input("Введите Фамилию: ")
        if has_string_symbols(user_string, int_list):
            raise Int_exception('Фамилия не должна содержать цифры')
        else:
            return user_string

def user_department_check_loop():
    while True:
        user_string = input("Введите отдел: ")
        if has_string_symbols(user_string, int_list):
            raise Int_exception('Отдел не должен содержать цифры')
        else:
            return user_string


def user_year_check_loop():
    while True:
        user_string = input("Введите год: ")
        try:
            user_string = int(user_string)
        except Str_exception('Год не должен содержать буквы'):
            break
        else:
            return user_string


int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


class Worker:
    def __init__(self, name, surname, department, year, workers=[]):
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year
        self.workers = workers

    def check_worker(self, arg):
        if self.year >= arg:
            self.workers.append(self.name)

    def info(self):
        return self.workers


a = Worker(user_name_check_loop(), user_surname_check_loop(),
           user_department_check_loop(), user_year_check_loop())
b = Worker(user_name_check_loop(), user_surname_check_loop(),
            user_department_check_loop(), user_year_check_loop())
c = Worker(user_name_check_loop(), user_surname_check_loop(),
            user_department_check_loop(), user_year_check_loop())
z = int(input('Введите год - '))
a.check_worker(z)
b.check_worker(z)
c.check_worker(z)
print(c.info())

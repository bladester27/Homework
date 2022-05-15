ls = []


def my_decorator(func):
    def wrapper():
        print("До начала")
        func()
        print("конец")
        # for _ in func:
        #     if _ % 2 == 0:
        #         pass
        #     else:
        #         func.pop(_)
    return wrapper()


@my_decorator
def fib(n):
    a, b = 0, 1
    while a < n:
        ls.append(a)
        a, b = b, a + b
    return ls


print(fib(1000))

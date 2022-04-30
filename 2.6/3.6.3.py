def prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def gen(arg):
    i = 1
    n = 3
    while True:
        if i <= arg:
            yield n
            n += 1
            i += 1
        else:
            break


def my_func(arg):
    x = gen(arg)
    a = next(x)
    i = 1
    while i <= arg:
        if prime(a) == True:
            i += 1
            return a

print(my_func(5))




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


def prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def my_func(arg):
    var = gen(arg)
    x = []
    while True:
        try:
            x.append(next(var))
        except StopIteration:
            break
    z = []
    for i in x:
        if prime(i):
            z.append(i)
    return z


print(my_func(1000))

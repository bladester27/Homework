def c1(n, d=None):
    global x
    if d is None:
        d = n - 1
    while d >= 2:
        if n % d == 0:
            break
        else:
            return c1(n, d - 1)
    else:
        x.append(n)
        return


def c2(a, b):
    for i in range(a, b + 1):
        if i <= 1:
            i += 1
        else:
            c1(i)
            i += 1
    return


x = []
c2(1, 50)
print(x)

def rek(a, b, x=[]):
    for i in range(a, b + 1):
        if i >= 1:
            x.append(i)
            i += 1
        else:
            i += 1
    return x

a = int(input('a = '))
b = int(input('b = '))
print(rek(a, b))

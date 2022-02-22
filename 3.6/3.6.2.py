my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def gen(arg):
    for var in arg:
        if var % 2 == 0:
            result = (var ** 2)
            yield result


z = gen(my_list)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
x = []
for i in my_list:
    if i % 2 == 0:
        x.append(i ** 2)
print(x)

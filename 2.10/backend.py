def my_func(c):
    f = open('base.txt', 'a+')
    if c == 1:
        a = input('Введите ссылку: ')
        b = input('Введите название: ')
        f.write(b + ' ')
        f.write(a + '\n')
    elif c == 2:
        z = input('Введите название: ')
        d = {}
        with open("base.txt") as file:
            for line in file:
                key, *value = line.split()
                d[key] = value
        print(d[z])
    else:
        f.close()

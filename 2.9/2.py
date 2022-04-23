c = 1
while True:
    f = open('base.txt', 'a+')
    c = int(input('Если хотите сократить ссылку введите - 1, '
                  'если хотите получить полную ссылку введите - 2, '
                  'если хотите завершить введите - 0 : '))
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
        break




c = 1
var = {}
while True:
    c = int(input('Если хотите сократить ссылку введите - 1, '
                  'если хотите получить полную ссылку введите - 2, '
                  'если хотите завершить введите - 0 : '))
    if c == 1:
        a = input('Введите ссылку: ')
        b = input('Введите название: ')
        var.update({b: a})
    elif c == 2:
        z = input('Введите название: ')
        print(var[z])
    else:
        break




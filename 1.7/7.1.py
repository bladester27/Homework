my_list = [12, 34, 76, 32, 67, 45, 13]
def sort_plus(a, ans=0):
    for x in a:
        if x > ans:
            ans = x
            x += 1
        else:
            x += 1
    return ans


def sort_minus(a, ans=0):
    ans = a[0]
    for x in a:
        if x > ans:
            x += 1
        else:
            ans = x
            x += 1
    return ans


def sum(a, x=0):
    for i in a:
        x += i
        i += 1
    return x


def arif(a):
    return sum(a) / len(a)


print('Наибольшее значение', sort_plus(my_list),
      'Наименьшее значение', sort_minus(my_list),
      'Сумма', sum(my_list),
      'Среднее арифметическое', arif(my_list), sep='\n')

"""Вопрос, каждый из трех вариантов являеться генератором?"""


l = [1, 2, 3, 4, 5]
# a = (l[::-1])
# print(a)

# def gen(ls):
#     index = len(ls) - 1
#     new_ls = []
#     while index >= 0:
#         new_ls.append(ls[index])
#         index -= 1
#     print(new_ls)
#
# gen(l)

def generator(ls):
    index = len(ls) - 1
    while index >= 0:
        yield ls[index]
        index -= 1

a = generator(l)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

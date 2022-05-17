from math import prod as p
from time import time as t
import threading


def fact(arg1, arg2):
    for _ in range(arg1, arg2 + 1):
        result.append(_)


result = []
task1 = threading.Thread(
    target=fact,
    args=(1, 4999))
task2 = threading.Thread(
    target=fact,
    args=(5000, 10000))
started_at = t()

task1.start()
task2.start()

task1.join()
task2.join()

print('Первый результат')
print('Время: {}'.format(t() - started_at))
print('Значение: ', p(result))

result = []

started_at = t()
print('Второй результат')
fact(1, 10000)
print('Значение: ', p(result))
print('Время: {}'.format(t() - started_at))

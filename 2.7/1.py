import random
import statistics

mylist = []
x = 1
y = 5
while len(mylist) < 10:
    mylist.append(random.randint(1, 10))

print(mylist)


def func1(a, b):
    z1 = statistics.mean(mylist[a:b])
    z2 = (mylist[a] + mylist[b]) / 2
    print("Среднее арифметическое от", mylist[a], "до", mylist[b], "=", z1,
          "Среднее арифметическое ", mylist[a], "и", mylist[b], "=", z2)


func1(x, y)


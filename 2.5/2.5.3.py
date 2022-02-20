l = [1, 2, 3, 4, 5]
a = iter(l)
w = []
while True:
    try:
        w.insert(0, next(a))
    except StopIteration:
        print(w)
        break

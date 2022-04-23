def my_format(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

my_format(Alex=22, Anna=23, Vlad=40)


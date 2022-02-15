class English:
    def greeting(self):
        return 'Hello!'


class Spanish:
    def greeting(self):
        return 'Oye!'


def hello_friend(x, y):
    print(x.greeting())
    print(y.greeting())


a = English()
b = Spanish()
hello_friend(a, b)

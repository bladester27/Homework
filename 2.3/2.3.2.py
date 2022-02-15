class English:
    def greeting(self):
        return 'Hello!'


class Spanish:
    def greeting(self):
        return 'Oye!'


def test(x, y):
    print(x.greeting())
    print(y.greeting())


a = English()
b = Spanish()
test(a, b)

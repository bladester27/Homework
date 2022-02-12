class Avt:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.mark}, {self.model}, {self.year}'


class Market:
    marketlist = []
    def __init__(self):
        self.marketlist = []

    def on(self, other):
        self.marketlist.append(other)
        print(f'Добавлен, {other}')

    def off(self, other):
        self.marketlist.remove(other)
        print(f'Продан, {other}')

    def info(self):
        return self.marketlist


car1 = Avt('Toyota', 'RAV4', '2019')
car2 = Avt('Chevrolet', 'Aveo', '2015')
car3 = Avt('Mazda', 'Kai', '2017')
a = Market()
a.on(car1)
a.off(car1)



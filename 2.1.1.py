class Book:
    def __init__(self, avt, name, year, gen):
        self.avt = avt
        self.name = name
        self.year = year
        self.gen = gen

    def __repr__(self):
        return f'{self.name}, {self.gen}, {self.avt}, {self.year}'

    def __str__(self):
        return f'{self.name}, {self.gen}, {self.avt}, {self.year}'

    def print_info(self):
        return f'{self.name}, {self.gen}, {self.avt}, {self.year}'


book1 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
book2 = Book('Стивен Кинг', 'Зеленая миля', 2014, 'Драма')
book3 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
print(book1.__repr__() == book3.__repr__())
print(book1.__repr__() == book2.__repr__())
print(book1.__str__() == book3.__str__())
print(book1.__str__() == book2.__str__())

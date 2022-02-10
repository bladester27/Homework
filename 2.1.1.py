class Book:
    def __init__(self, avt, name, year, gen):
        self.avt = avt
        self.name = name
        self.year = year
        self.gen = gen

    def info(self):
        return self.avt, self.name, self.year, self.gen


book1 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
book2 = Book('Стивен Кинг', 'Зеленая миля', 2014, 'Драма')
book3 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
print(book1.info() == book3.info())
print(book2.info() == book3.info())
print(book1.info())
print(book2.info())
print(book3.info())

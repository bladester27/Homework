class Book:
    def __init__(self, avt, name, year, gen, feedbacks=[]):
        self.avt = avt
        self.name = name
        self.year = year
        self.gen = gen
        self.feedbacks = feedbacks

    def __repr__(self):
        return f'{self.name}, {self.gen}, {self.avt}, {self.year}, {self.feedbacks}'

    def __str__(self):
        return f'{self.name}, {self.gen}, {self.avt}, {self.year}, {self.feedbacks}'


class Feed:
    def __init__(self, feedback=[]):
        self.feedback = feedback


book1 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
book2 = Book('Стивен Кинг', 'Зеленая миля', 2014, 'Драма')
book3 = Book('Джоан роулинг', 'Гарри поттер и узник Азкабана', 2019, 'Фентези')
book1.feedbacks = ('Good', 'Bad')
book2.feedbacks = ('Good', 'Bad', 'Nice')
book3.feedbacks = ('Good', 'Bad', 'not bad')
print(book1)
print(book2)
print(book3)

class Car:
    def __init__(self, Mark, Model, Cost):
        self.Mark = Mark
        self.Model = Model
        self.Cost = Cost

    def __str__(self):
        return f'Mark = {self.Mark}, Model = {self.Model}, Cost = {self.Cost}'


class Racing(Car):
    def __init__(self, Speed, Mark, Model, Cost):
        super().__init__(Mark, Model, Cost)
        self.Speed = Speed

    def __str__(self):
        return f'Speed = {self.Speed}, Mark = {self.Mark}, Model = {self.Model}, Cost = {self.Cost}'


class Cargo(Car):
    def __init__(self, Cargo, Mark, Model, Cost):
        super().__init__(Mark, Model, Cost)
        self.Cargo = Cargo

    def __str__(self):
        return f'Cargo = {self.Cargo}, Mark = {self.Mark}, Model = {self.Model}, Cost = {self.Cost}'


car1 = Car('Toyota', 'Duster', 20000)
car2 = Racing(350, 'Lamborgini', 'Diablo', 100000)
car3 = Cargo(50, 'Tatra', 'C12', 10000)

print(car1, car2, car3, sep='\n')

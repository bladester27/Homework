class Avt:
    def __init__(self, frame, engine, wheels, doors):
        self._frame = frame
        self._engine = engine
        self.wheels = wheels
        self.doors = doors

    def _get_frame(self):
        return self._frame

    def _get_engine(self):
        return self._engine

    def _set_frame(self, arg):
        self._frame = arg

    def _set_engine(self, arg):
        self._engine = arg

    def print_info(self):
        return f'Frame: {self._frame}, Engine: {self._engine}, ' \
               f'Wheels: {self.wheels}, Doors: {self.doors}'


my_car = Avt('Pickup', 'F190', 4, 2)
print(my_car.print_info())
my_car._set_frame('Racing')
my_car._set_engine('R260')
print(my_car.print_info())

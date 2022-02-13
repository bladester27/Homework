import mouse as ms

class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Mouse:
    def click(self):
        while True:
            if ms.on_click == True:
                return True
            else:
                continue

class Button(Rect, Mouse):
    def __init__(self, length, width):
        super().__init__(length, width)
        super().click()

my_button = Button(10, 20)
my_rectangle = Rect()

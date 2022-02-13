import pygame as pg

class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Mouse:
    def __init__(self, mouse):
        self.mouse = mouse

    def mouse(self):
        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    print('нажата кнопка 1')
                elif i.button == 3:
                    print('нажата кнопка 3')
                elif i.button == 2:
                    print('нажата кнопка 2')
class Button:
    pass


Mouse.mouse()

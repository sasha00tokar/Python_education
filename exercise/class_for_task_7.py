'''Модуль содержит классы данных комнаты'''


class WinDoor:
    '''Класс окна, двери.
    Конструктор принимает ширину и длинну окна или двери'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def squareWinDoor(self):
        '''Метод для вычисления площади окна или двери'''
        return self.x * self.y


class Room:
    '''Класс Комната.
    Конструктор принимает ширину, длинну и высоту комнаты'''
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []

    def ollSurface(self):
        '''Метод для вычисления полной площади комнаты'''
        return 2 * self.height * (self.width + self.lenght)

    def addWD(self, w, h):
        '''Метод добавления окон и дверей в список'''
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        '''Метод для вычисления рабочей площади'''
        new_square = self.ollSurface()
        for i in self.wd:
            new_square -= i.squareWinDoor()
        return new_square

    def countRoll(self, w=1, h=10):
        '''Метод для подсчета количества руллонов'''
        self.roll_square = w * h
        return self.workSurface() / self.roll_square

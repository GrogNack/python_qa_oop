import math
import random


class Figure:

    def __init__(self):
        self._name = ''
        self._area = 0
        self._angles = 0
        self._perimeter = 0

    def get_name(self):
        return self._name

    def get_area(self):
        return self._area

    def get_angles(self):
        return self._angles

    def get_perimeter(self):
        return self._perimeter

    def add_area(self, argument):
        if type(argument) not in [Rectangle, Triangle, Square, Circle]:
            raise AttributeError("Переданный элемент не является фигурой")
        return self._area + argument.get_area()


class Triangle(Figure):

    def __init__(self, a, b, c: int):
        super().__init__()
        self._name = 'Треугольник'
        self._angles = 3
        self.p = (a + b + c) / 2
        self._perimeter = a + b + c
        self._area = round(math.sqrt(self.p * (self.p - a) * (self.p - b) * (self.p - c)))


class Rectangle(Figure):

    def __init__(self, a, b: int):
        super().__init__()
        self._angles = 4
        self._name = f'Прямоугольник {a} на {b}'
        self._perimeter = (a + b) * 2
        self._area = (a * b)


class Square(Rectangle):

    def __init__(self, a: int):
        super().__init__(a, a)
        self._angles = 4
        self._name = f'Квадрат {a} на {a}'
        self._perimeter = a * 4
        self._area = a ** 2


class Circle(Figure):

    def __init__(self, r: int):
        super().__init__()
        self._angles = 0
        self._name = f'Круг с радиусом {r}'
        self._perimeter = round(2 * math.pi * r)
        self._area = round(math.pi * r ** 2)


sq = Square(6)
re = Rectangle(4, 5)
cir = Circle(2)
tr = Triangle(3, 4, 5)
print(sq.get_name() + ' | ' + str(sq.get_angles()) + ' | ' + str(sq.get_perimeter()) + ' | ' + str(sq.get_area()))
print(re.get_name() + ' | ' + str(re.get_angles()) + ' | ' + str(re.get_perimeter()) + ' | ' + str(re.get_area()))
print(cir.get_name() + ' | ' + str(cir.get_angles()) + ' | ' + str(cir.get_perimeter()) + ' | ' + str(cir.get_area()))
print(tr.get_name() + ' | ' + str(tr.get_angles()) + ' | ' + str(tr.get_perimeter()) + ' | ' + str(tr.get_area()))
print(tr.add_area(re))

import pytest

from model.classes import Rectangle
from model.classes import Triangle


def test_get_name():
    rect = Rectangle(3, 4)
    assert rect.get_name() == 'Прямоугольник 3 на 4'


@pytest.mark.parametrize("a, b, expect", [(3, 4, 14), (1, 2, 6), (22, 13, 70)])
def test_get_perimeter(a, b, expect):
    rect = Rectangle(a, b)
    assert rect.get_perimeter() == expect


@pytest.mark.parametrize("a, b, expect", [(3, 4, 12), (30, 40, 1200), (15, 20, 300)])
def test_get_area(a, b, expect):
    rect = Rectangle(a, b)
    assert rect.get_area() == expect


def test_get_angles():
    rect = Rectangle(3, 4)
    assert rect.get_angles() == 4


def test_get_add_area():
    tr = Triangle(15, 20, 25)
    rect = Rectangle(3, 4)
    assert type(rect.add_area(tr)) == int
    assert rect.add_area(tr) == 162

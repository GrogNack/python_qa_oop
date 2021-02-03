import pytest

from model.classes import Rectangle
from model.classes import Square


@pytest.mark.parametrize("a", [i for i in range(1, 8, 1)])
def test_get_name(a):
    sq = Square(a)
    assert sq.get_name() == f'Квадрат {a} на {a}'


@pytest.mark.parametrize("a, expect", [(3, 12), (1, 4), (22, 88)])
def test_get_perimeter(a, expect):
    sq = Square(a)
    assert sq.get_perimeter() == expect


@pytest.mark.parametrize("a, expect", [(3, 9), (30, 900), (15, 225)])
def test_get_area(a, expect):
    sq = Square(a)
    assert sq.get_area() == expect


def test_get_angles():
    sq = Square(3)
    assert sq.get_angles() == 4


def test_get_add_area():
    sq = Square(15)
    rect = Rectangle(3, 4)
    assert type(rect.add_area(sq)) == int
    assert rect.add_area(sq) == 237

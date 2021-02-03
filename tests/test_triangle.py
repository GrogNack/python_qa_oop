import pytest

from model.classes import Rectangle
from model.classes import Triangle


def test_get_name():
    tr = Triangle(3, 4, 5)
    assert tr.get_name() == 'Треугольник'


@pytest.mark.parametrize("a, b, c, expect", [(3, 4, 5, 12), (1, 2, 3, 6), (22, 15, 13, 50)])
def test_get_perimeter(a, b, c, expect):
    tr = Triangle(a, b, c)
    assert tr.get_perimeter() == expect


@pytest.mark.parametrize("a, b, c, expect", [(3, 4, 5, 6), (30, 40, 50, 600), (15, 20, 25, 150)])
def test_get_area(a, b, c, expect):
    tr = Triangle(a, b, c)
    assert tr.get_area() == expect


def test_get_angles():
    tr = Triangle(3, 4, 5)
    assert tr.get_angles() == 3


def test_get_add_area():
    tr = Triangle(3, 4, 5)
    re = Rectangle(3, 4)
    assert type(re.add_area(tr)) == int
    assert re.add_area(tr) > 6

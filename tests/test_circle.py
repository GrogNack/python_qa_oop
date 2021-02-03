import pytest

from model.classes import Circle


def test_get_name():
    ci = Circle(3)
    assert ci.get_name() == f'Круг с радиусом {3}'


@pytest.mark.parametrize("a, expect", [(3, 19), (1, 6), (22, 138)])
def test_get_perimeter(a, expect):
    ci = Circle(a)
    assert ci.get_perimeter() == expect


@pytest.mark.parametrize("a, expect", [(3, 28), (30, 2827), (15, 707)])
def test_get_area(a, expect):
    ci = Circle(a)
    assert ci.get_area() == expect


def test_get_angles():
    ci = Circle(4)
    assert ci.get_angles() == 0


def test_get_add_area():
    ci = Circle(15)
    rect = 12
    with pytest.raises(AttributeError):
        ci.add_area(rect)

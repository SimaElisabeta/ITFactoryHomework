import pytest
from sesiunea8.app.geometric_shapes import Square, Rectangle, Circle


class TestSquare:
    @pytest.mark.parametrize('value, expected', [
        (12.5, 156.25),
        (10, 100)
    ])
    def test_area(self, value, expected):
        square = Square(value)
        actual = round(square.area(), 2)
        assert actual == expected

    @pytest.mark.parametrize("value, expected", [
        (12.5, 50),
        (10, 40)
    ])
    def test_perimeter(self, value, expected):
        square = Square(value)
        actual = round(square.perimeter(), 2)
        assert actual == expected


class TestRectangle:
    @pytest.mark.parametrize("length, width, expected", [
        (30, 15, 450),
        (45.50, 10.50, 477.75)
    ])
    def test_area(self, length, width, expected):
        rectangle = Rectangle(length, width)
        actual = round(rectangle.area(), 2)
        assert actual == expected

    @pytest.mark.parametrize("length, width, expected", [
        (30, 15, 90),
        (45.50, 10.10, 111.20)
    ])
    def test_perimeter(self, length, width, expected):
        rectangle = Rectangle(length, width)
        actual = round(rectangle.perimeter(), 2)
        assert actual == expected


class TestCircle:
    @pytest.mark.parametrize("radius, expected", [
        (20, 1256.637),
        (3.5, 38.485)
    ])
    def test_area(self, radius, expected):
        circle = Circle(radius)
        actual = round(circle.area(), 3)
        assert actual == expected

    @pytest.mark.parametrize("radius, expected", [
        (5, 31.416),
        (3.5, 21.991)
    ])
    def test_perimeter(self, radius, expected):
        circle = Circle(radius)
        actual = round(circle.perimeter(), 3)
        assert actual == expected

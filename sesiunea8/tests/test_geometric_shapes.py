import unittest
from parameterized import parameterized
from sesiunea8.app.geometric_shapes import Square, Rectangle, Circle


class TestSquare(unittest.TestCase):
    @parameterized.expand([
        (Square(12.5), 156.25),
        (Square(10), 100)
    ])
    def test_area(self, square, expected):
        actual = round(square.area(), 2)  # use precision of 2 decimal points
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (Square(12.5), 50),
        (Square(10), 40)
    ])
    def test_perimeter(self, square, expected):
        actual = round(square.perimeter(), 2)
        self.assertEqual(actual, expected)


class TestRectangle(unittest.TestCase):
    @parameterized.expand([
        (Rectangle(30, 15), 450),
        (Rectangle(45.50, 10.50), 477.75)
    ])
    def test_area(self, rectangle, expected):
        actual = round(rectangle.area(), 2)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (Rectangle(30, 15), 90),
        (Rectangle(45.50, 10.10), 111.20)
    ])
    def test_perimeter(self, rectangle, expected):
        actual = round(rectangle.perimeter(), 2)
        self.assertEqual(actual, expected)


class TestCircle(unittest.TestCase):
    @parameterized.expand([
        (Circle(20), 1256.637),
        (Circle(3.5), 38.485)
    ])
    def test_area(self, circle, expected):
        actual = round(circle.area(), 3)  # use precision of 3 decimal points
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (Circle(5), 31.416),
        (Circle(3.5), 21.991)
    ])
    def test_perimeter(self, circle, expected):
        actual = round(circle.perimeter(), 3)
        self.assertEqual(actual, expected)

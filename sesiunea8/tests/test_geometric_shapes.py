import unittest
from parameterized import parameterized
from sesiunea8.app.geometric_shapes import Square, Rectangle, Circle


class TestSquare(unittest.TestCase):
    @parameterized.expand([
        (12.5, 156.25),
        (10, 100)
    ])
    def test_area(self, value, expected):
        square = Square(value)
        actual = round(square.area(), 2)  # use precision of 2 decimal points
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (12.5, 50),
        (10, 40)
    ])
    def test_perimeter(self, value, expected):
        square = Square(value)
        actual = round(square.perimeter(), 2)
        self.assertEqual(actual, expected)


class TestRectangle(unittest.TestCase):
    @parameterized.expand([
        (30, 15, 450),
        (45.50, 10.50, 477.75)
    ])
    def test_area(self, length, width, expected):
        rectangle = Rectangle(length, width)
        actual = round(rectangle.area(), 2)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (30, 15, 90),
        (45.50, 10.10, 111.20)
    ])
    def test_perimeter(self, length, width, expected):
        rectangle = Rectangle(length, width)
        actual = round(rectangle.perimeter(), 2)
        self.assertEqual(actual, expected)


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(20)

    @parameterized.expand([
        (20, 1256.637),
        (3.5, 38.485)
    ])
    def test_area(self, radius, expected):
        circle = Circle(radius)
        actual = round(circle.area(), 3)  # use precision of 3 decimal points
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (5, 31.416),
        (3.5, 21.991)
    ])
    def test_perimeter(self, radius, expected):
        circle = Circle(radius)
        actual = round(circle.perimeter(), 3)
        self.assertEqual(actual, expected)

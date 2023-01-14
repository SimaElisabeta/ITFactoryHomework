import unittest
from parameterized import parameterized
from sesiunea8.app.tema8_1 import get_positive_numbers, add_nr_if_unique, get_max_nr


class TestTema8_1(unittest.TestCase):

    @parameterized.expand([
        ([1, 9, -1], [1, 9]),
        ([-10, 3, 13, 0], [3, 13]),
        ([-20, 0, -5], [])
    ])
    def test_get_positive_numbers(self, lst, expected):
        self.assertEqual(get_positive_numbers(lst), expected)

    @parameterized.expand([
        ([0, 2, 3], 1, True),
        ([10, 2, 3], 10, False),
        ([], 10, True)
    ])
    def test_add_nr_if_unique(self, lst, nr, expected):
        self.assertEqual(add_nr_if_unique(nr, lst), expected)

    @parameterized.expand([
        ([0, 27, 14, 45, 15], 45),
        ([0, 0], 0),
        ([-100, 100], 100),
        ([-5, -1], -1),
        ([-5, -1, 0], 0)
    ])
    def test_get_max_nr(self, lst, expected):
        self.assertEqual(get_max_nr(lst), expected)

import unittest
from main import insert_in, count_discount


class TestDiscount(unittest.TestCase):
    def test_1(self):
        insert_in([1, 2, 3, 4, 5, 6, 7], 100)
        self.assertEqual(count_discount(), 15.00)

    def test_2(self):
        insert_in([65, 45, 34, 45, 53, 61, 37.5, 87.6], 45)
        self.assertEqual(count_discount(), 359.43)

    def test_3(self):
        insert_in([1, 1, 1], 33)
        self.assertEqual(count_discount(), 2.67)


if __name__ == '__main__':
    unittest.main()

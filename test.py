import unittest
from electr import Electr


class TestElectr(unittest.TestCase):

    def test_case_1(self):
        e = Electr("electr_in.txt")
        e.form_solutions()
        length_of_lines = e.calculate_length(e.reconstruct_solution())
        self.assertEqual(length_of_lines, 2738.18)


if __name__ == '__main__':
    unittest.main()

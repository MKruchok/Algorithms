import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        text = "ehellowworldlollhelloworldhelloworlhello"
        pattern = "helloworld"
        self.assertEqual(Solution(text, pattern).kmp(), [16])

    def test_2(self):
        text = "abcxabcdababcdabcefabcdabcdabce"
        pattern = "abcdabce"
        self.assertEqual(Solution(text, pattern).kmp(), [10, 23])

    def test_3(self):
        text = "abcabcabcabcabc"
        pattern = "abc"
        self.assertEqual(Solution(text, pattern).kmp(), [0, 3, 6, 9, 12])

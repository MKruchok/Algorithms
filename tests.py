import unittest
from priority_queue import PQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.priorityQ = PQueue()
        self.priorityQ.add(23, 4)
        self.priorityQ.add(11, 3)
        self.priorityQ.add(56, 5)
        self.priorityQ.add(33, 2)
        self.priorityQ.add(44, 5)

    def test_get(self):
        self.assertEqual(self.priorityQ.peek(), 56)

    def test_find(self):
        self.assertEqual(self.priorityQ.find(11), "Value to find: 11, priority: 3, index: 3")

    def test_pop(self):
        self.assertEqual(self.priorityQ.pop(), 56)
        self.assertEqual(len(self.priorityQ), 4)

    def test_add(self):
        self.priorityQ.add(122, 34)
        self.assertEqual(self.priorityQ.peek(), 122)


if __name__ == '__main__':
    unittest.main()

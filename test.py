import unittest
from main import Graph


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(9)
        self.graph.add_line(2, 3, 6)
        self.graph.add_line(1, 6, 12)
        self.graph.add_line(1, 7, 24)
        self.graph.add_line(1, 2, 9)
        self.graph.add_line(0, 4, 1)
        self.graph.add_line(0, 1, 14)
        self.graph.add_line(4, 8, 5)
        self.graph.add_line(3, 5, 5)
        self.graph.add_line(2, 4, 34)
        self.graph.add_line(3, 4, 3)
        self.graph.add_line(4, 5, 9)
        self.graph.add_line(4, 7, 1)
        self.graph.add_line(5, 8, 12)
        self.graph.add_line(7, 8, 3)
        self.graph.add_line(6, 7, 1)

    def test_0(self):
        self.distance_main = self.graph.dijkstra(0)
        self.distance_sum = 0
        for end_vertex in range(len(self.distance_main)):
            print("Distance from", 0, "to", end_vertex, "==", self.distance_main[end_vertex])
            self.distance_sum += self.distance_main[end_vertex]
        result = [0, 14, 10, 4, 1, 9, 3, 2, 5]
        self.middle = self.distance_sum / len(self.distance_main)
        print("Arithmetic mean ==", round(self.middle, 2))
        self.assertEqual(self.distance_main, result)

    def test_1(self):
        result = [14, 0, 9, 15, 14, 20, 12, 13, 16]
        self.assertEqual(self.graph.dijkstra(1), result)

    def test_2(self):
        result = [10, 9, 0, 6, 9, 11, 11, 10, 13]
        self.assertEqual(self.graph.dijkstra(2), result)

    def test_3(self):
        result = [4, 15, 6, 0, 3, 5, 5, 4, 7]
        self.assertEqual(self.graph.dijkstra(3), result)

    def test_4(self):
        result = [1, 14, 9, 3, 0, 8, 2, 1, 4]
        self.assertEqual(self.graph.dijkstra(4), result)

    def test_5(self):
        result = [9, 20, 11, 5, 8, 0, 10, 9, 12]
        self.assertEqual(self.graph.dijkstra(5), result)

    def test_6(self):
        result = [3, 12, 11, 5, 2, 10, 0, 1, 4]
        self.assertEqual(self.graph.dijkstra(6), result)

    def test_7(self):
        result = [2, 13, 10, 4, 1, 9, 1, 0, 3]
        self.assertEqual(self.graph.dijkstra(7), result)

    def test_8(self):
        result = [5, 16, 13, 7, 4, 12, 4, 3, 0]
        self.assertEqual(self.graph.dijkstra(8), result)

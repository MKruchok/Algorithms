import unittest
from main import Graph


class TestTarjan(unittest.TestCase):
    def test_1(self):
        test_graph1 = Graph(9)
        test_graph1.add_vertex(1, 2)
        test_graph1.add_vertex(2, 3)
        test_graph1.add_vertex(3, 1)
        test_graph1.add_vertex(4, 3)
        test_graph1.add_vertex(4, 2)
        test_graph1.add_vertex(4, 5)
        test_graph1.add_vertex(5, 4)
        test_graph1.add_vertex(5, 6)
        test_graph1.add_vertex(6, 3)
        test_graph1.add_vertex(6, 7)
        test_graph1.add_vertex(7, 6)
        test_graph1.add_vertex(8, 5)
        test_graph1.add_vertex(8, 7)

        self.assertEqual(test_graph1.tarjan(), [[0], [3, 2, 1], [7, 6], [5, 4], [8]])

import unittest
from main import Graph


class TestTarjan(unittest.TestCase):
    def test_1(self):
        test_graph1 = Graph()
        test_graph1.add_vertex(0, 1)
        test_graph1.add_vertex(1, 2)
        test_graph1.add_vertex(2, 0)
        test_graph1.add_vertex(3, 4)
        test_graph1.add_vertex(3, 7)
        test_graph1.add_vertex(7, 3)
        test_graph1.add_vertex(4, 5)
        test_graph1.add_vertex(5, 6)
        test_graph1.add_vertex(5, 0)
        test_graph1.add_vertex(6, 2)
        test_graph1.add_vertex(6, 4)
        test_graph1.add_vertex(6, 0)

        self.assertEqual(test_graph1.tarjan(), [[2, 1, 0], [6, 5, 4], [7, 3]])

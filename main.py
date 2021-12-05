from queue import PriorityQueue
from sys import maxsize
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.distance = [maxsize] * self.vertices

    def add_line(self, start_vert, end_vert, weight):
        self.graph[start_vert].append((end_vert, weight))
        self.graph[end_vert].append((start_vert, weight))

    def dijkstra(self, vertex_start):
        self.distance[vertex_start] = 0
        q = PriorityQueue()
        q.put((self.distance[vertex_start], vertex_start))
        while not q.empty():
            dist, vertex = q.get()
            for adj_vertex, weight in self.graph[vertex]:
                if self.distance[vertex] + weight < self.distance[adj_vertex]:
                    self.distance[adj_vertex] = self.distance[vertex] + weight
                    q.put((self.distance[adj_vertex], adj_vertex))
        return self.distance


graph = Graph(9)
graph.add_line(0, 1, 4)
graph.add_line(0, 6, 7)
graph.add_line(1, 6, 11)
graph.add_line(1, 7, 20)
graph.add_line(1, 2, 9)
graph.add_line(2, 3, 6)
graph.add_line(2, 4, 2)
graph.add_line(3, 4, 10)
graph.add_line(3, 5, 5)
graph.add_line(4, 5, 15)
graph.add_line(4, 7, 1)
graph.add_line(4, 8, 5)
graph.add_line(5, 8, 12)
graph.add_line(6, 7, 1)
graph.add_line(7, 8, 3)

D = graph.dijkstra(0)

for end_vertex in range(len(D)):
    print("Distance from 0 to", end_vertex, "==", D[end_vertex])

from queue import PriorityQueue
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.distance = [999] * self.vertices

    def add_line(self, first_vert, second_vert, weight):
        self.graph[first_vert].append((second_vert, weight))
        self.graph[second_vert].append((first_vert, weight))

    def dijkstra(self, main_vertex):
        self.distance[main_vertex] = 0
        q = PriorityQueue()
        q.put((self.distance[main_vertex], main_vertex))
        while not q.empty():
            dist, current_vertex = q.get()
            for adj_vertex, weight in self.graph[current_vertex]:
                if self.distance[current_vertex] + weight < self.distance[adj_vertex]:
                    self.distance[adj_vertex] = self.distance[current_vertex] + weight
                    q.put((self.distance[adj_vertex], adj_vertex))
        return self.distance


def insert_out(result):
    file = open("dijkstra.out", 'w')
    file.write(str(result))

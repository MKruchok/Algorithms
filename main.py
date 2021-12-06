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


graph = Graph(9)
graph.add_line(0, 1, 4)
graph.add_line(0, 4, 1)
graph.add_line(1, 6, 12)
graph.add_line(1, 7, 24)
graph.add_line(1, 2, 9)
graph.add_line(2, 3, 6)
graph.add_line(2, 4, 2)
graph.add_line(3, 4, 3)
graph.add_line(3, 5, 5)
graph.add_line(4, 5, 9)
graph.add_line(4, 7, 1)
graph.add_line(4, 8, 5)
graph.add_line(5, 8, 12)
graph.add_line(6, 7, 1)
graph.add_line(7, 8, 3)

s = 8
distance_main = graph.dijkstra(s)
distance_sum = 0

for end_vertex in range(len(distance_main)):
    print("Distance from", s, "to", end_vertex, "==", distance_main[end_vertex])
    distance_sum += distance_main[end_vertex]

middle = distance_sum / len(distance_main)
insert_out(middle)
print("Arithmetic mean ==", round(middle, 2))

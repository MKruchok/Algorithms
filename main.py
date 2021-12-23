from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertexes = defaultdict(list)
        self.vert_num = vertices
        self.index = 0
        self.indexes = [-1] * self.vert_num
        self.low_index = [-1] * self.vert_num
        self.on_stack = [False] * self.vert_num
        self.stack = []
        self.scc = list()

    def add_vertex(self, vertex, edge_to):
        self.vertexes[vertex].append(edge_to)

    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        self.index += 1
        self.indexes[at] = self.index
        self.low_index[at] = self.index

        for to in self.vertexes[at]:
            if self.indexes[to] == -1:
                self.dfs(to)
                self.low_index[at] = min(self.low_index[at], self.low_index[to])
            elif self.on_stack[to]:
                self.low_index[at] = min(self.low_index[at], self.low_index[to])
        node = -1

        if self.indexes[at] == self.low_index[at]:
            arr = []
            while node != at:
                node = self.stack.pop()
                arr.append(node)
                self.on_stack[node] = False
            self.scc.append(arr)

    def tarjan(self):
        for i in range(self.vert_num):
            if self.indexes[i] == -1:
                self.dfs(i)
        return self.scc


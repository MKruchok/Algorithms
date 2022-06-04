from collections import defaultdict


class Graph:

    def __init__(self):
        self.nodes_dict = defaultdict(list)
        self.low_link_id = []
        self.on_stack = []
        self.stack = []
        self.scc = list()

    def add_vertex(self, vertex, edge_to):
        self.nodes_dict[vertex].append(edge_to)
        self.low_link_id = [-1] * len(self.nodes_dict)
        self.on_stack = [False] * len(self.nodes_dict)

    def dfs(self, current):
        self.stack.append(current)
        self.on_stack[current] = True
        self.low_link_id[current] = current


        for child in self.nodes_dict[current]:
            if self.low_link_id[child] == -1:
                self.dfs(child)
                self.low_link_id[current] = min(self.low_link_id[current], self.low_link_id[child])
            elif self.on_stack[child]:
                self.low_link_id[current] = min(self.low_link_id[current], self.low_link_id[child])

        node = -1
        if current == self.low_link_id[current]:
            new_scc = []
            while node != current:
                node = self.stack.pop()
                new_scc.append(node)
                self.on_stack[node] = False
            self.scc.append(new_scc)

    def tarjan(self):
        for i in range(len(self.nodes_dict)):
            if self.low_link_id[i] == -1:
                self.dfs(i)
        return self.scc

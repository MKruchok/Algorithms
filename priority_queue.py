from node import Node


class PQueue:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def add(self, value, priority):
        self.heap.append(Node(value, priority))
        self.up(len(self.heap) - 1, self.heap[len(self.heap) - 1])

    def pop(self):
        self.heap[len(self.heap) - 1], self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        popped = self.heap.pop()
        self.down(0)
        return popped.value

    def up(self, index, elem):
        while index > 0 and elem.priority > self.heap[int((index - 1) / 2)].priority:
            self.heap[int(index)] = self.heap[int((index - 1) / 2)]
            index -= 1
            index /= 2
        if index <= 0:
            self.heap[0] = elem
        else:
            self.heap[int(index)] = elem

    def down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        big = index
        if right >= len(self.heap):
            return
        if self.heap[big].priority < self.heap[left].priority:
            big = left
        if self.heap[big].priority < self.heap[right].priority:
            big = right
        if big is not index:
            self.heap[index], self.heap[big] = self.heap[big], self.heap[index]

    def peek(self):
        return self.heap[0].value

    def find(self, value):
        for i in range(len(self.heap)):
            if self.heap[i].value is value:
                return 'Value to find: {value}, priority: {priority}, index: {index}'.format \
                    (value=self.heap[i].value, priority=self.heap[i].priority, index=i)
        return 'Nothing found.'

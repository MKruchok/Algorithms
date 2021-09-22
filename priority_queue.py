class Node:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return 'Value: {value}, priority: {priority}'.format(value=self.value, priority=self.priority)


class PQueue:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def add(self, value, priority):
        self.heap.append(Node(value, priority))
        self.upwards(len(self.heap) - 1)

    def pop(self):
        self.heap[len(self.heap) - 1], self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        popped = self.heap.pop()
        self.downwards(0)
        return popped.value

    def upwards(self, index):
        prev_index = index - 1
        if prev_index < 0:
            return
        if self.heap[index].priority > self.heap[prev_index].priority:
            self.heap[index], self.heap[prev_index] = self.heap[prev_index], self.heap[index]
        self.upwards(prev_index)

    def downwards(self, index):
        next_index = index + 1
        if next_index is len(self.heap):
            return
        if self.heap[next_index].priority > self.heap[index].priority:
            self.heap[next_index], self.heap[index] = self.heap[index], self.heap[next_index]
        self.downwards(next_index)

    def peek(self):
        return self.heap[0].value

    def find(self, value):
        for i in range(len(self.heap) - 1):
            if self.heap[i].value is value:
                return 'Value to find: {value}, priority: {priority}, index: {index}'.format \
                    (value=self.heap[i].value, priority=self.heap[i].priority, index=i)
        return 'Nothing found.'


if __name__ == '__main__':
    queue = PQueue()
    queue.add(23, 4)
    queue.add(11, 3)
    queue.add(56, 5)
    queue.add(33, 2)
    queue.add(44, 5)
    print(queue.pop())
    print(queue.pop())
    print(queue.find(11))

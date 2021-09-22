class Node:

    def __init__(self, value, priority: int = 0):
        self.value = value
        self.priority = priority

    def __str__(self):
        return 'Value: {value}, priority: {priority}'.format(value=self.value, priority=self.priority)


class PQueue:

    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def push(self, value, priority):
        self._heap.append(Node(value, priority))
        self.bottom_up(len(self._heap) - 1)

    def pop(self):
        self._heap[len(self._heap) - 1], self._heap[0] = self._heap[0], self._heap[len(self._heap) - 1]
        popped = self._heap.pop()
        self.top_down(0)
        return popped.value

    def bottom_up(self, index):
        prev_index = index - 1
        if prev_index < 0:
            return
        if self._heap[index].priority > self._heap[prev_index].priority:
            self._heap[index], self._heap[prev_index] = self._heap[prev_index], self._heap[index]
        self.bottom_up(prev_index)

    def top_down(self, index):
        next_index = index + 1
        if next_index is len(self._heap):
            return
        if self._heap[next_index].priority > self._heap[index].priority:
            self._heap[next_index], self._heap[index] = self._heap[index], self._heap[next_index]
        self.top_down(next_index)

    def peek(self):
        return self._heap[0].value

    def find(self, value):
        for i in range(len(self._heap) - 1):
            if self._heap[i].value is value:
                return 'Value to find: {value}, priority: {priority}, index: {index}'.format \
                    (value=self._heap[i].value, priority=self._heap[i].priority, index=i)
        return 'Nothing found.'


if __name__ == '__main__':
    queue = PQueue()
    queue.push(23, 4)
    queue.push(11, 3)
    queue.push(56, 5)
    queue.push(33, 2)
    queue.push(44, 5)
    print(queue.pop())
    print(queue.pop())
    print(queue.find(11))

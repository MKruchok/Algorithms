class Node:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return 'Value: {value}, priority: {priority}'.format(value=self.value, priority=self.priority)

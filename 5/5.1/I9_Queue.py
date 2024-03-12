class Queue:

    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return not self.queue


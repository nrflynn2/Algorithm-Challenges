'''
Array implementation of queue
enqueue is O(n)
dequeue is O(1)
'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

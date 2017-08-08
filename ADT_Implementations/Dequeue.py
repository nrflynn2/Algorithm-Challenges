'''
Array-based implementation of Dequeue ADT
Adding and removing from the front is O(n)
Adding and removing from the rear is O(1)
'''

class Deque:
    def __init__(self):
        self.deq = []

    def addFront(self, item):
        return self.deq.insert(0, item)

    def addRear(self, item):
        return self.deq.append(item)

    def removeFront(self):
        return self.deq.pop(0)

    def removeRear(self):
        return self.deq.pop() 

    def isEmpty(self):
        return self.deq == []

    def size(self):
        return len(self.deq)

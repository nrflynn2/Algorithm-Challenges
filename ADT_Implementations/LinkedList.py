from random import randint

class Node:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode
        
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)
            
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if value == None: return 
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_front(self, value):
        if value == None: return
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)

    def find(self, value):
        if value is None: return None
        for node in self:
            if node.value == value:
                return True
        return False

    def delete(self, value):
        if value is None or self.head is None: return
        elif self.head.value == value:
            self.head = self.head.next
            return
        prevNode = self.head
        currNode = self.head.next
        while currNode:
            if currNode.value == value:
                prevNode.next = currNode.next
                return
            prevNode = currNode
            currNode = currNode.next

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def toArray(self):
        arr = []
        for node in self:
            arr.append(node.value)
        '''currrent = self.head
        while current is not None:
            arr.append(current.value)
            current = current.next'''
        return arr

class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value, None, self.tail)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self


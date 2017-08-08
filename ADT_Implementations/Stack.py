class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def isEmpty(self):
        return self.stack == []
    
    def pop(self):
        if self.isEmpty():
            print("Error: Trying to pop an attempt stack")
            return self.stack
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

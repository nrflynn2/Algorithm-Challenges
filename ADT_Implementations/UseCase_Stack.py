from Stack import *

'''Algorithm to read a string of parantheses ({[, left to right, and decide 
whether they are correctly balanced and matching'''
def parChecker(string):
    s = Stack()
    balanced = True
    idx = 0
    while idx < len(string) and balanced:
        symbol = string[idx]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            elif not matches(s.peek(), symbol):
                return False
            s.pop()
        idx += 1

    if s.isEmpty() and balanced:
        return True
    else: return False

def matches(start, end):
    starts = '([{'
    ends = ')]}'
    return starts.index(start) == ends.index(end)

print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

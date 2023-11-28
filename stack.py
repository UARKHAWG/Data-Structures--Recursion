'''
stack assignment using a deque 
'''
from collections import deque

class Stack:
    '''simple stack'''
    def __init__(self):
        self.data = deque()

    def push(self, value):
        '''append: add an element to the right side'''
        self.data.append(value)

    def push_left(self, value):
        '''appendleft: add an element from the left side'''
        self.data.appendleft(value)

    def pop(self):
        '''pop: add an element to the right side'''
        return self.data.pop()

    def pop_left(self):
        '''popleft: add an element from the left side'''
        return self.data.popleft()



# Test cases:
# myStack = Stack()
# myStack.push(3)
# myStack.push(6)
# myStack.push(9)
# print(myStack.pop()) # 9
# print(myStack.pop()) # 6
# print(myStack.pop()) # 3

# Using Python's deque module, implement a stack.
# Hint: push/pop operations in a stack happen on the same side. 
# Picture a stack of pancakes
# adding and removing of flapjacks always happens from the "top" of the stack.
# With deque, we can use visualize either the "left" or "right" side of the double-ended queue
# as the "top" of the stack, so there are two ways to implement this.


# myStack2 = Stack()
# myStack2.push(1)
# myStack2.push(2)
# myStack2.push(3)
# myStack2.push_left(4)
# print(myStack2.pop()) # 3
# print(myStack2.pop()) # 2
# print(myStack2.pop()) # 1
# print(myStack2.pop()) # 4

myStack3 = Stack()
myStack3.push(1)
myStack3.push(2)
myStack3.push(3)
myStack3.push_left(4)
print(myStack3.pop_left()) # 4
print(myStack3.pop_left()) # 1
print(myStack3.pop_left()) # 2
print(myStack3.pop_left()) # 3

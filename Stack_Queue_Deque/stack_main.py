from collections import deque
import math


# stack = []
# stack.append(10)
# stack.append(8)
# stack.append(12)
# stack.append(3)

# print(stack.pop())
# peek = stack[-1]
# print(peek)
# size = len(stack)
# print(size)


# ## stack implementation using deque
# stack = deque()
# stack.append(10)
# stack.append(8)
# stack.append(12)
# stack.append(3)

# print(stack.pop())
# peek = stack[-1]
# print(peek)
# size = len(stack)
# print(size)

class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class MyStack:
    
    def __init__(self) -> None:
        self.head = None
        self.sz = 0
    
    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz += 1
    
    def pop(self):
        if self.head == None:
            return -math.inf
        
        res = self.head.data
        temp = self.head.next
        self.head = temp
        self.sz -= 1
        return res
    
    def peek(self):
        if self.head == None:
            print('stack is empty!')
            return 
        else:
            res = self.head.data 
            print(res)
            return 
    
    def size(self):
        return self.sz
    
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

# End of MyStack class, Time complexity of
# all these operations is O(1).
    
# stack = MyStack()
# print(stack.size())
# stack.peek()
# stack.push(2)
# stack.push(5)
# stack.push(9)
# stack.push(16)
# stack.peek()
# print(stack.pop())
# stack.peek()
# print(stack.size())
# stack.display()
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

class Stack:
    
    def __init__(self) -> None:
        self.main_stack = []
        self.aux_stack = []
    
    def push(self, x):
        if self.main_stack == []:
            self.main_stack.append(x)
            self.aux_stack.append(x)
        else:
            self.main_stack.append(x)
            
        if self.main_stack[-1] <= self.aux_stack[-1]:
            self.aux_stack.append(x)
    
    def pop(self):
        if self.main_stack == []:
            print('stack is empty!')
            return
        
        top = self.main_stack.pop()
        
        if top == self.aux_stack[-1]:
            self.aux_stack.pop()
        
        return top
    
    def peek(self):
        return self.main_stack[-1]
    
    def getmin(self):
        return self.aux_stack[-1]
    
        
        


stack = Stack()
stack.push(5)
stack.push(7)
stack.push(1)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.getmin())
stack.push(2)
print(stack.peek())
stack.push(9)
print(stack.getmin())
print(stack.peek())



        
            

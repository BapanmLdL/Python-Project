import math


class Stack:
    
    def __init__(self) -> None:
        self.main_stack = []
        self.min = None
    
    def push(self, x):
        if self.main_stack == []:
            self.min = x
            self.main_stack.append(x)
        
        if x <= self.min:
            self.main_stack.append((x - self.min))
            self.min = x
        else:   
            self.main_stack.append(x)
        
    def pop(self):
        if self.main_stack == []:
            print('stack is empty!')
            return 
        
        peek = self.main_stack.pop()
        if peek <= 0:
            res = self.min
            self.min = self.min - peek
            return res
        
        else:
            return peek
        
        
    def peek(self):
        if self.main_stack[-1] <= 0:
            return self.min
        else:
            return self.main_stack[-1]
        
        
    def getmin(self):
        return self.min


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

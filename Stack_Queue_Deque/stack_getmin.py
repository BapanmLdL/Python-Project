class Stack:
    
    def __init__(self) -> None:
        self.main_stack = []
        self.min = None 
    
    def push(self, x):
        if self.main_stack == []:
            self.min = x
            self.main_stack.append(x)
        
        if x <= self.min:
            res = 2*x - self.min
            self.main_stack.append(res)
            self.min = x
        else:
            self.main_stack.append(x)
    
    def pop(self):
        if self.main_stack == []:
            print('stack is empty!')
            return 
        
        top = self.main_stack.pop()
        if top <= self.min:
            res = self.min
            self.min = 2*self.min - top
            return res
        else:
            return top
    
    def peek(self):
        top = self.main_stack[-1]
        if top <= self.min:
            return self.min
        else:
            return top
    
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

        
    
    
class TwoStack:
    
    def __init__(self, n) -> None:
        self.size = n
        self.arr = [None] * n
        self.top1 = - 1
        self.top2 = n
    
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x 
            return True
        else:
            return False
    
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
            return True
        else:
            return False
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        return None
    
    def pop2(self):
        if self.top2 < self.size :
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return x
        return None
    
    def peek1(self):
        if self.top1 >= 0:
            return self.arr[self.top1]
        return None
    
    def peek2(self):
        if self.top2 < self.size:
            return self.arr[self.top2]
        return None
    
    def size1(self):
        return self.top1 + 1
    
    def size2(self):
        return self.size - self.top2
    

class KStack:
    
    def __init__(self, n, k) -> None:
        self.capacity = n
        self.arr = [None] * n
        self.top = [-1] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.freespace = 0
        self.size_arr = [0] * k
    
    def push(self, x, k):
        
        # check for stack overflow
        if self.freespace == -1:
            return False
        
        # find index 
        index = self.freespace
        
        # update freespace
        self.freespace = self.next[index]
        
        # insert the value
        self.arr[index] = x
        
        # increment the size
        self.size_arr[k-1] += 1
        
        # update next
        self.next[index] = self.top[k-1]
        
        # update top
        self.top[k-1] = index
        
        return True
    
    def pop(self, k):
        # check for stack underflow
        if self.top[k-1] == -1:
            return -1
        
        index = self.top[k-1]
        
        self.top[k-1] = self.next[index]
        
        self.next[index] = self.freespace
        
        self.freespace = index
        
        self.size_arr[k-1] -= 1
        
        return self.arr[index]
    
    def peek(self, k):
        if self.top[k-1] == -1:
            return f"stack {k} is empty!"
        else:
            return self.arr[self.top[k-1]]
    
    def is_empty(self, k):
        return self.top[k-1] == -1
    
    def size(self, k):
        return self.size_arr[k-1]
        
            
        
stack = KStack(10, 3)
stack.push(5, 1)
stack.push(2, 1)
stack.push(3, 1)
print(stack.pop(1))
stack.push(10, 3)
stack.push(12, 2)
print(stack.pop(1))
stack.push(7, 2)
stack.push(24, 1)
print(stack.pop(2))
stack.push(0, 1)
print(stack.pop(3))
# print(stack.pop(3))
print(stack.peek(1))
print(stack.peek(2))
print(stack.peek(3))
print(stack.is_empty(1))
print(stack.is_empty(2))
print(stack.is_empty(3))
print(stack.size(1))
print(stack.size(2))
print(stack.size(3))


# stack = TwoStack(10)
# stack.push1(1)
# stack.push1(3)
# stack.push2(9)
# stack.push2(6)
# stack.push2(0)
# print(stack.peek1())
# print(stack.peek2())
# print(stack.pop1())
# print(stack.pop2())
# print(stack.size1())
# print(stack.size2())
# # print(stack.arr)
    
    
class Queue:
    
    def __init__(self, n) -> None:
        self.capacity = n
        self.q = [None] * n
        self.size = 0
    
    def enque(self, x):
        if self.isfull():
            return False
        
        self.size += 1
        self.q[self.size - 1] = x
        return True
    
    def isfull(self):
        return self.capacity == self.size
    
    def isempty(self):
        return self.size == 0
    
    def deque(self):
        if self.isempty():
            return None
        
        res = self.q[0]
        
        for i in range(self.size-1):
            self.q[i] = self.q[i+1]
        
        self.q[self.size-1] = None
        self.size -= 1
        
        return res
    
    def return_queue(self):
        return self.q


class EfficientQueue:
    
    def __init__(self, n) -> None:
        self.capacity = n
        self.q = [None] * n
        self.size = 0
        self.front = 0
        self.rear = 0
    
    def isempty(self):
        return self.size == 0
    
    def isfull(self):
        return self.size == self.capacity
    
    def enque(self, x):
        if self.isfull():
            return False
        
        self.rear = -1 if self.size == 0 else self.rear
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = x
        self.size += 1
        
        return True 
    
    def deque(self):
        if self.isempty():
            return False
    
        self.q[self.front] = None
        self.size -= 1
        self.front = 0 if self.size == 0 else (self.front + 1) % self.capacity
        
        return True
    
    def return_queue(self):
        return self.q
    
    def getFront(self):
        if self.isempty():
            return -1
        return self.q[self.front]
    
    def getRear(self):
        if self.isempty():
            return -1
        return self.q[self.rear]



q = EfficientQueue(81)
print(q.enque(69))
# print(q.deque())
# print(q.enque(92))
# print(q.enque(12))
# print(q.deque())
# print(q.isfull())
# print(q.isfull())
print(q.getFront())
print(q.getRear())
# print(q.deque())
# print(q.deque())
# print(q.return_queue())   
class MyDeque:

    def __init__(self, n: int):
        self.capacity = n
        self.dq = [None] * n
        self.size = 0
        self.front = 0
        self.rear = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = 0 if self.size == 0 else (self.front - 1) % self.capacity
        
        self.dq[self.front] = value
        self.size += 1
        
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = -1 if self.size == 0 else (self.rear + 1) % self.capacity
        
        self.dq[self.rear] = value
        self.size += 1
        
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.dq[self.front] = None
        self.size -= 1
        
        self.front = 0 if self.size == 0 else (self.front + 1) % self.capacity
        
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.dq[self.rear] = None
        self.size -= 1
        
        self.rear = 0 if self.size == 0 else (self.rear - 1) % self.capacity
        
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.dq[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.dq[self.rear]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
    

class Deque:
    
    def __init__(self, n: int) -> None:
        self.capacity = n
        self.dq = [None] * n
        self.size = 0
        self.front = 0
    
    def insertFront(self, x):
        if self.isFull():
            return False
        
        self.front = (self.front - 1) % self.capacity
        self.dq[self.front] = x
        self.size += 1
        
        return True
    
    def insertRear(self, x):
        if self.isFull():
            return False
        
        rear = (self.front + self.size - 1) % self.capacity
        rear = (rear + 1) % self.capacity
        self.dq[rear] = x
        self.size += 1
        
        return True
    
    def deleteFront(self):
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
        
    
    def deleteRear(self):
        if self.isEmpty():
            return False
        
        self.size -= 1
        return True
    
    def getFront(self):
        if self.isEmpty():
            return -1
        
        return self.dq[self.front]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        
        return self.dq[(self.front + self.size - 1) % self.capacity]
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
        
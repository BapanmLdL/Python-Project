class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
class Deque:
    
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def insertFront(self, x):
        newNode = Node(x)
        
        if self.front == None:
            self.rear = newNode
        else:
            self.front.prev = newNode
            newNode.next = self.front
        
        self.front = newNode
        self.size += 1
        return True
    
    def insertRear(self, x):
        newNode = Node(x)
        
        if self.rear == None:
            self.front = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
        
        self.rear = newNode
        self.size += 1
        return True
    
    def isEmpty(self):
        return self.size == 0
    
    def deleteFront(self):
        if self.isEmpty():
            return False
        
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
            
        self.size -= 1
        return True
    
    def deleteRear(self):
        if self.isEmpty():
            return False
        
        self.rear = self.rear.prev
        if self.rear == None:
            self.front = None
        else:
            self.rear.next = None
        
        self.size -= 1
        return True
    
    def getFront(self):
        if self.isEmpty():
            return -1
        
        return self.front.data
    
    def getRear(self):
        if self.isEmpty():
            return -1
        
        return self.rear.data


dq = Deque()
dq.insertRear(10)   
dq.insertRear(20) 
dq.insertFront(30)  
dq.deleteRear()
print(dq.getRear())
print(dq.getFront())
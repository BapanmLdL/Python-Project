class Node:
    
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    

class Queue:
    
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def isempty(self):
        return self.size == 0
    
    def getFront(self):
        if self.front == None:
            return -1
        
        return self.front.val 
    
    def getRear(self):
        if self.rear == None:
            return -1
        
        return self.rear.val
    
    def enque(self, x):
        newNode = Node(x)
        if self.rear == None:
            self.front = newNode
        else:
            self.rear.next = newNode
            
        self.rear = newNode
        self.size += 1
        
        return 
    
    def deque(self):
        if self.front == None:
            return -1
        
        res = self.front.val
        self.front = self.front.next
        
        if self.front == None:
            self.rear = None
            
        self.size -= 1
        
        return res


q = Queue()
q.enque(69)
print(q.deque())
q.enque(92)
q.enque(12)
print(q.deque())
print(q.getFront())
print(q.getRear())           
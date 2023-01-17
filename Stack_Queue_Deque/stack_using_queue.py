from collections import deque

class Stack:
    
    def __init__(self) -> None:
        self.main_q = deque()
        self.aux_q = deque()
    
    def push(self, x):
        self.aux_q.append(x)
        
        while self.main_q:
            self.aux_q.append(self.main_q.popleft())
        
        self.main_q, self.aux_q = self.aux_q, self.main_q
        return
    
    def empty(self):
        return len(self.main_q) == 0
    
    def pop(self):
        if not self.empty():
            return self.main_q.popleft()
    
    def top(self):
        if not self.empty():
            return self.main_q[0]
        

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) 

# q2 = deque([3])
# q1 = deque([2, 1])
# q2.extend(q1)
# print(q2) 
# print(q2[0])  
from collections import deque
class MyDS:
    def __init__(self):
        self.dq = deque()
    def insert_min(self, x):
        return self.dq.appendleft(x)
    def insert_max(self, x):
        return self.dq.append(x)
    def extract_min(self):
        return self.dq.popleft()
    def extract_max(self):
        return self.dq.pop()
    def get_min(self):
        return self.dq[0]
    def get_max(self):
        return self.dq[-1]
# q = MyDS()
# q.insert_min(5)
# q.insert_max(10)
# q.insert_min(3)
# q.insert_max(15)
# q.insert_min(2)
# print(q.get_min())
# print(q.get_max())
# q.insert_min(1)
# print(q.get_min())
# q.insert_max(20)
# print(q.get_max())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    def insertRear(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz += 1
    def insertFront(self, x):
        temp = Node(x)
        if self.front == None:
            self.rear = temp
        else:
            self.front.prev = temp
            temp.next = self.front
        self.front = temp
        self.sz += 1
    def deleteRear(self):
        if self.rear == None:
            return None
        else:
            res = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            self.sz -= 1
            return res
    def deleteFront(self):
        if self.front == None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res
    def getFront(self):
        if self.front == None:
            return None
        else:
            return self.front.data
    def getRear(self):
        if self.rear == None:
            return None
        else:
            return self.rear.data
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
# dq = MyDeque()
# dq.insertFront(10)
# dq.insertFront(20)
# dq.insertRear(30)
# print(dq.getRear())
# print(dq.getFront())
# print(dq.size())
class myDeque:
    def __init__(self, C):
        self.l = [None]*C
        self.cap = C
        self.sz = 0
        self.front = 0
    def insertRear(self, x):
        if self.sz == self.cap:
            return
        else:
            rear = (self.front + self.sz - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.l[rear] = x
            self.sz += 1
    def insertFront(self, x):
        if self.sz == self.cap:
            return
        else:
            self.front = (self.front - 1) % self.cap
            self.l[self.front] = x
            self.sz += 1
    def deleteFront(self):
        if self.sz == 0:
            return None
        else:
            res = self.l[self.front]
            self.l[self.front] = None
            self.front = (self.front + 1) % self.cap
            self.sz -= 1
            return res
    def deleteRear(self):
        if self.sz == 0:
            return None
        else:
            rear = (self.front + self.sz - 1) % self.cap
            res = self.l[rear]
            self.l[rear] = None
            rear = (rear - 1) % self.cap
            self.sz -= 1
            return res
    def getFront(self):
        if self.sz == 0:
            return None
        else:
            return self.l[self.front]
    def getRear(self):
        if self.sz == 0:
            return None
        else:
            rear = (self.sz + self.front - 1) % self.cap
            return self.l[rear]
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
    def get_l(self):
        return self.l
d = myDeque(10)
d.insertFront(2)
d.insertRear(100)
d.insertFront(3)
d.insertRear(200)
# d.insertFront(30)
# d.insertRear(2)
print(d.getFront())
print(d.getRear())
# print(d.deleteRear())
# print(d.deleteFront())
print(d.get_l())
print(d.size())






import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueueSLL:
    def __init__(self):
        self.head = None
        self.sz = 0
    def enque(self, x):
        temp = Node(x)
        if self.head == None:
            self.head = temp
            self.sz += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = temp
            self.sz += 1
    def deque(self):
        if self.head == None:
            return 'Queue is empty --> Error'
        res = self.head.data
        self.head = self.head.next
        self.sz -= 1
        return res
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
    def getFront(self):
        if self.head == None:
            return 'Queue is Empty'
        return self.head.data
    def getRear(self):
        if self.head == None:
            return 'Queue is Empty'
        if self.head.next == None:
            return self.head.data
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr.data

class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    def enque(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz += 1
    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
    def getFront(self):
        return self.front.data
    def getRear(self):
        return self.rear.data
    def Display(self):
        curr = self.front
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next
        print()
    def reverse(self):
        curr = self.front
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while prev is not None:
            print(prev.data, end = " ")
            prev = prev.next
        print()
# q = myQueue() # head = None
# q.enque(10)    # 10->None
# q.enque(20)    # 10->20->None
# q.enque(30)    # 10->20->30->None
# print(q.deque())  # 20->30->None
# print(q.size())
# q.Display()
# q.enque(40)        # 20->30->40->None
# print(q.getFront())
# print(q.getRear())
# q.Display()
# q.reverse()
# print(q.getFront())
# print(q.getRear())
# q.Display()
# # print(q.isEmpty())


class MYQUEUE:
    def __init__(self, C):
        self.l = [None]*C
        self.cap = C
        self.size = 0
        self.front = 0
    def enque(self, x):
        if self.size == self.cap:
            return
        else:
            rear = (self.front + self.size - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.l[rear] = x
            self.size += 1
    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.l[self.front] = None
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return res
    def getFront(self):
        if self.size == 0:
            return None
        else:
            return self.l[self.front]
    def getRear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.size + self.front - 1) % self.cap
            return self.l[rear]
    def isEmpty(self):
        return self.size == 0
    def print_l(self):
        return self.l
    def find_y(self, y):
        rear = (self.size + self.front - 1) % self.cap
        for i in range(self.front, rear+1):
            if self.l[i] == y:
                return True
        else:
            return False
    def display(self):
        rear = (self.size + self.front - 1) % self.cap
        for i in range(self.front, rear+1):
            print(self.l[i], end = " ")
        print()
# q = MYQUEUE(10)
# q.enque(10)
# q.enque(20)
# q.enque(30)
# q.enque(40)
# # print(q.deque())
# # print(q.deque())
# # print(q.deque())
# # print(q.deque())
# print(q.print_l())
# q.enque(50)
# # print(q.deque())
# print(q.print_l())
# print(q.getFront())
# print(q.getRear())
# # print(q.isEmpty())
# print(q.find_y(30))
# q.display()

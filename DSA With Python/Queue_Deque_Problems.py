class MyQueue:
    def __init__(self, c):
        self.queue = []
        self.cap = c
        self.sz = 0
        self.head = 0
        self.tail = 0
    def push(self, x):
        if self.sz == self.cap:
            return
        self.queue.append(x)
        self.tail += 1
        self.sz += 1
    def pop(self):
        if self.sz == 0:
            return
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        self.sz -= 1
        return res
    def getFront(self):
        if self.sz == 0:
            return None
        else:
            return self.queue[self.head]
    def getRear(self):
        if self.sz == 0:
            return None
        else:
            return self.queue[self.tail - 1]
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
    def get_queue(self):
        return self.queue
    def find_y(self, y):
        for i in range(self.head, self.tail):
            if self.queue[i] == y:
                return True
        else:
            return False
# q = MyQueue(10)
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# q.push(6)
# q.push(7)
# q.push(8)
# q.push(9)
# q.push(10)
# print(q.pop())
# print(q.pop())
# q.push(11)
# q.push(12)
# # q.push(13)
# print(q.getFront())
# print(q.getRear())
# print(q.size())
# print(q.get_queue())
# print(q.find_y(1))

from collections import deque
class QueueOperations:
    def __init__(self):
        self.q = deque()
    def enque(self, x):
        self.q.append(x)
    def deque(self):
        res = self.q.popleft()
        return res
    def front(self):
        return self.q[0]
    def rear(self):
        return self.q[-1]
    def get_queue(self):
        return self.q
    def find(self, y):
        for e in self.q:
            if e == y:
                return True
        else:
            return False

# Q = QueueOperations()
# Q.enque(10)
# Q.enque(20)
# Q.enque(30)
# Q.enque(40)
# Q.enque(50)
# print(Q.deque())
# print(Q.front())
# print(Q.rear())
# print(Q.find(500))
# print(Q.get_queue())

class StackImplementUsingArray:
    def __init__(self):
        self.stack = []
    def push(self, x):
        if len(self.stack) <= 100000:
            self.stack.append(x)
        else:
            print("Stack Full")
            return
    def pop(self):
        if self.stack != []:
            res = self.stack.pop()
        else:
            print("Stack Empty")
            return
        return res
    def display(self):
        if self.stack == []:
            print(-1)
            return
        else:
            for e in reversed(self.stack):
                print(e, end = " ")
        print()
    def find_y(self, y):
        for e in reversed(self.stack):
            if e == y:
                print('YES')
                return
        else:
            print('NO')
            return
    def middle_stack(self):
        n = len(self.stack)
        if n == 0:
            return 'Stack Empty'
        elif n % 2 != 0:
            return self.stack[n//2]
        else:
            return self.stack[(n//2 - 1)]

# method 1: TC: enQueue operation
# O(n) and TC: deQueue O(1)
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.sz = 0
    def enQueue(self, x):
        while self.s1 != []:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2 != []:
            self.s1.append(self.s2.pop())
    def size(self):
        return len(self.s1)
    def deQueue(self):
        if self.s1 == []:
            return "Queue is empty"
        else:
            return self.s1.pop()

# method 2: TC: enQueue O(1)
# deQueue TC: O(n)
class QUEUEUSINGSTACKS:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.sz = 0
    def enQueue(self, x):
        self.s1.append(x)
        self.sz += 1
    def deQueue(self):
        if self.s1 == [] and self.s2 == []:
            return -1
        if self.s2 == []:
            while self.s1 != []:
                self.s2.append(self.s1.pop())
        res = self.s2.pop()
        self.sz -= 1
        return res
    def size(self):
        return self.sz
# q = QueueUsingStacks()
# q.enQueue(10)
# q.enQueue(20)
# q.enQueue(30)
# q.enQueue(40)
# print(q.size())
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())
# print(q.size())
# # print(q.deQueue())

from collections import deque
class MyDeque:
    def __init__(self):
        self.dq = deque()
    def insert_Front(self, x):
        self.dq.appendleft(x)
    def insert_Rear(self, x):
        self.dq.append(x)
    def del_Front(self):
        if not self.dq:
            return -1
        return self.dq.popleft()
    def del_Rear(self):
        if not self.dq:
            return -1
        return self.dq.pop()
    def get_Front(self):
        if not self.dq:
            return "Deque is empty"
        return self.dq[0]
    def get_Rear(self):
        if not self.dq:
            return "Deque is empty"
        return self.dq[-1]
# dq = MyDeque()
# # dq.insert_Front(1)
# # dq.insert_Rear(2)
# print(dq.get_Front())
# print(dq.get_Rear())
class Del_In_Deque:
    def __init__(self):
        self.dq = deque([1,2,3,4,5,6,7,8,9,10,11,12])
    def eraseAt(self,x):
        del self.dq[x]
        return self.dq
    def eraseInRange(self, s, e):
        sz = e - s
        while sz != 0:
            del self.dq[s]
            sz -= 1
        return self.dq
    def eraseAll(self):
        return self.dq.clear()
# dq = Del_In_Deque()
# print(dq.eraseAt(0))
# print(dq.eraseInRange(2, 7))
# print(dq.eraseAll())



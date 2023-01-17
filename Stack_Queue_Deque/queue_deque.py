from collections import deque

def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    
    while stack:
        q.append(stack.pop())
    
    return q

def revQ(q):
    if len(q) == 0:
        return
    
    x = q.popleft()
    revQ(q)
    q.append(x)
    return q

def revStack(stack):
    if len(stack) == 0:
        return 
    
    x = stack.pop()
    revStack(stack)
    stack.insert(0, x)
    return stack

# class Queue:
    
#     def __init__(self) -> None:
#         self.q = deque()
    
#     def enque(self, x):
#         self.q.append(x)
#         return 
    
#     def deque(self):
#         if not len(self.q) == 0:
#             return self.q.popleft()
    

# q = Queue()
# q.enque(20)
# q.enque(10)
# q.enque(15)
# q.enque(30)
# q = deque([20, 10, 15, 30])
# rev_q = revQ(q)
# print(rev_q)
# stack = [20, 10, 15, 30]
# rev_stack = revStack(stack)
# print(rev_stack)

def generates_numbers(n: int):
    q = deque()
    q.append("5")
    q.append("6")
    
    for i in range(n):
        front = q.popleft()
        print(front, end=" ")
        q.append(front + "5")
        q.append(front + "6")
    
    return

# generates_numbers(10)
# print('\n')


def printmaxK_naive(k, arr):
    n = len(arr)
     
    for i in range(n-k+1):
        res = arr[i]
        for j in range(i+1, i+k):
            res = max(res, arr[j])
        print(res, end=" ")
    
    return

def printmaxK(k, arr):
    n = len(arr)
    dq = deque()
    for i in range(k):
        while dq and arr[dq[0]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
    print(arr[dq[0]], end=" ")
    
    for i in range(k, n):
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and arr[dq[0]] <= arr[i]:
            dq.pop()
            
        dq.append(i)
        print(arr[dq[0]], end=" ")
    
    return
        

# printmaxK(3, arr=[10, 8, 5, 12, 15, 7, 6, 11, 2, 27, 13, 15])    


class MyDS:
    
    def __init__(self) -> None:
        self.dq = deque()
    
    def insert_min(self, x):
        if self.empty():
            self.dq.appendleft(x)
        else:
            if x < self.dq[0]:
                self.dq.appendleft(x)
                return
            else:
                return
    
    def insert_max(self, x):
        if self.empty():
            self.dq.append(x)
        else:
            if x > self.dq[-1]:
                self.dq.append(x)
                return
            else:
                return 
    
    def get_min(self):
        if not self.empty():
            return self.dq[0]
        
    
    def get_max(self):
        if not self.empty():
            return self.dq[-1]
    
    def extract_min(self):
        if not self.empty():
            return self.dq.popleft()
    
    def extract_max(self):
        if not self.empty():
            return self.dq.pop()
    
    def empty(self):
        return len(self.dq) == 0
    
# my_ds = MyDS()
# my_ds.insert_min(5)
# my_ds.insert_max(10)
# my_ds.insert_min(3)
# my_ds.insert_max(15)
# my_ds.insert_min(2)
# print(my_ds.get_min())
# print(my_ds.get_max())
# my_ds.insert_min(11)
# print(my_ds.get_min())
# my_ds.insert_max(10)
# print(my_ds.get_max())

def first_circular_tour_naive(petrol, dist):
    n = len(petrol)
    
    for start in range(n):
        curr_petrol = 0
        end = start
        while True:
            curr_petrol += (petrol[end] - dist[end])
            if curr_petrol < 0:
                break
            end = (end + 1) % n
            if end == start:
                return start + 1
    return -1

# def circular_tour_better(petrol, dist):
#     n = len(petrol)
#     dq = deque()
#     curr_petrol = 0
#     i = 0
#     while i < n:
#         while curr_petrol >= 0:
#             dq.append(i)
#             curr_petrol += (petrol[i] - dist[i])
#             i += 1
#         while dq:
#             x = dq.popleft()
#             curr_petrol -= (petrol[x] - dist[x])
#             break
        
#         i += 1
    
#     return -1 if len(dq) == 0 else dq[0]

def first_circular_tour(petrol, dist):
    start = 0
    curr_petrol = 0
    prev_petrol = 0
    n = len(petrol)
    for i in range(n):
        curr_petrol += (petrol[i] - dist[i])
        if curr_petrol < 0:
            start = i + 1
            prev_petrol += curr_petrol
            curr_petrol = 0
    
    return start + 1 if (curr_petrol + prev_petrol) >= 0 else -1

        
# petrol = [4, 8, 7, 4, 8, 4, 12, 3, 5, 7, 10]
# dist = [6, 5, 3, 5, 8, 5, 12, 16, 2, 1, 3]
# print(first_circular_tour(petrol, dist))
from numpy import loadtxt
import time
import math

def insert_at_bottom(stack, e):
    if len(stack) == 0:
        stack.append(e)
        return stack
    
    topEle = stack.pop()
    insert_at_bottom(stack, e)
    stack.append(topEle)

def reverse_a_stack(stack):
    if len(stack) == 0 or len(stack) == 1:
        return stack
    
    topEle = stack.pop()
    reverse_a_stack(stack)
    insert_at_bottom(stack, topEle)
    
def reverse_stack(stack):
    res = []
    for _ in range(len(stack)):
        res.append(stack.pop())
    
    return res


def solve(stack, k):
    if k == 1:
        stack.pop()
        return stack
    
    topEle = stack.pop()
    solve(stack, k-1)
    stack.append(topEle)

def delete_middle(stack):
    if len(stack) == 0:
        return stack
    
    mid = len(stack) // 2 + 1
    solve(stack, mid)
    
    return stack
    

class TwoStacks:
    
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
        else:
            return None
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.pop2 += 1
            return x
        else:
            return None
        
def celebrity_problem_naive(M, n):
            
    In = [0] * n
    Out = [0] * n
        
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                In[j] += 1
                Out[i] += 1
                    
    for i in range(n):
        if In[i] == n-1 and Out[i] == 0:
            return i
        
    return -1

def celebrity_problem(M, n):
    
    Celebrity = 0
    for i in range(n):
        if M[Celebrity][i] == 1:
            Celebrity = i
        
    for i in range(n):
        if i != Celebrity and (M[Celebrity][i] == 1 or M[i][Celebrity] == 0):
            return -1
    
    return Celebrity


def max_of_min_for_everywindow_naive(arr):
    
    result = [-math.inf] * len(arr)
    
    for i in range(len(arr)):
        
        for j in range(i, len(arr)):
            
            length = j - i + 1
            temp = math.inf
            
            for k in range(i, j+1):
                
                temp = min(temp, arr[k])
                
            result[length-1] = max(result[length-1], temp)
            
    return result

arr = [1, 2, 3, 4]
print(max_of_min_for_everywindow_naive(arr))
                
                 
    
        
    
    
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


















# stack = [1, 2, 3, 5]
# delete_middle(stack)
# print(stack)

# n = 900
# stack = []
# for i in range(n):
#     stack.append(i)
    
# # # record start time
# start = time.time()   

# delete_middle(stack)

# end = time.time() 

# t = (end - start)
# print(t)

# print("Done!")






# stack_nparray = loadtxt(r"D:\Vs Code Python Files\DSA with Python\Stack_Queue_Deque\fileInput_stack.txt")

# stack = stack_nparray.tolist()

# # record start time
# start = time.time()

# revsed_stack = reverse_stack(stack)

# del revsed_stack
# del stack_nparray
# del stack
# # record end time
# end = time.time()
# t = (end - start) * (10**3)
# print(t)
# print("Done!")


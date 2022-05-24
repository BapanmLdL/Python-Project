from collections import deque
import math
# stack = deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# peek = stack[-1]
# print(peek)
# size = len(stack)
# print(size)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0
    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz += 1
    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.data
        temp = self.head.next
        self.head = temp
        self.sz -= 1
        return res
    def size(self):
        return self.sz
    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next
        print()
    def find_element(self, y):
        curr = self.head
        while curr is not None:
            if curr.data == y:
                print('YES')
                return
            curr = curr.next
        print('NO')
        return
    def middle_of_stack(self):
        n = 1
        curr = self.head
        while curr.next is not None:
            n += 1
            curr = curr.next
        c = 1
        temp = self.head
        while c <= n:
            if c == (n//2 + 1):
                res = temp.data
                break
            else:
                c += 1
                temp = temp.next
        return res

# End of MyStack Class, Time Complexity of
# Push, Pop, Peek operations is O(1) const time
s = MyStack() # head = None
s.push(10)   # 10->None
s.push(20)   # 20->10->None
s.push(30)   # 30->20->10->None
s.push(40)   # 40->30->20->10->None
s.push(50)   # 50->40->30->20->10->None
s.display()
s.find_element(30)
print(s.middle_of_stack())
# print(s.pop())  # 40->30->20->10->None
# print(s.peek())
# print(s.size())
def ismatching(a, b):
    if (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']'):
        return True
    else:
        return False

def isBalanced(expression):
    stack = []
    for x in expression:
        if x in ('(', '{', '['):
            stack.append(x)
        else:
            if not stack:
                return False
            elif ismatching(stack[-1], x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


def InfixtoPostfix(exp):
    pre = {}
    pre['^'] = 4
    pre['*'] = 3
    pre['/'] = 3
    pre['+'] = 2
    pre['-'] = 2
    pre['('] = 1
    stack = []
    l = []
    result = ""
    for x in exp:
        l.append(x)
    for i in range(len(l)):
        if (l[i] >= 'a' and l[i] <= 'z') or (l[i] >= 'A' and l[i] <= 'Z'):
            result += l[i]
        elif l[i] == "(":
            stack.append(l[i])
        elif l[i] == ")":
            while stack[-1] != "(":
                result = result + stack.pop()
            stack.pop()
        else:
            if stack == [] or pre[l[i]] > pre[stack[-1]]:
                stack.append(l[i])
            elif pre[l[i]] <= pre[stack[-1]] and l[i] != "^":
                while stack != [] and stack[-1] != "(":
                    result = result + stack.pop()
                stack.append(l[i])
            elif l[i] == "^" and pre[l[i]] == pre[stack[-1]]:
                stack.append(l[i])
    while stack != []:
        result = result + stack.pop()
    return result

def Evaluation_Of_Postfix(exp):
    stack = []
    operators = ['*', '+', '-', '^', '/']
    for x in exp:
        if x not in operators:
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if x == '^':
                result = int(op2) ** int(op1)
                stack.append(result)
            else:
                result = eval(f'{op2} {x} {op1}')
                stack.append(result)
    return stack[-1]
# exp = list(map(str,input().rstrip().split()))
# print(Evaluation_Of_Postfix(exp))

def InfixtoPrefix(exp):
    pre = {}
    pre['^'] = 4
    pre['*'] = 3
    pre['/'] = 3
    pre['+'] = 2
    pre['-'] = 2
    pre[')'] = 1
    stack = []
    l = []
    prefix = ""
    for x in exp[::-1]:
        l.append(x)
    for i in range(len(l)):
        if (l[i] >= 'a' and l[i] <= 'z') or (l[i] >= 'A' and l[i] <= 'Z'):
            prefix += l[i]
        elif l[i] == ')':
            stack.append(l[i])
        elif l[i] == '(':
            while stack[-1] != ')':
                prefix += stack.pop()
            stack.pop()
        else:
            if stack == []:
                stack.append(l[i])
            else:
                if pre[l[i]] > pre[stack[-1]]:
                    stack.append(l[i])
                elif pre[l[i]] <= pre[stack[-1]]:    # and l[i] != '^':
                    while stack != [] and stack[-1] != ')':
                        prefix += stack.pop()
                    stack.append(l[i])
                elif l[i] == '^' and pre[l[i]] == pre[stack[-1]]:
                    stack.append([l[i]])
    while stack != []:
        prefix += stack.pop()
    return prefix[::-1]

def Evaluation_Of_Prefix(exp):
    stack = []
    operators = ['*', '+', '-', '^', '/']
    for e in reversed(exp):
        if e not in operators:
            stack.append(e)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if e == '^':
                res = int(op1) ** int(op2)
                stack.append(res)
            else:
                res = eval(f'{op1} {e} {op2}')
                stack.append(res)
    return stack[-1]
# exp = list(map(str,input().rstrip().split()))
# print(Evaluation_Of_Prefix(exp))
def InsertInStack(n,arr):
    res = []
    for i in range(n):
        res.append(arr.pop())
    return res
# arr = list(map(int,input().rstrip().split()))
# n = len(arr)
# print(InsertInStack(n, arr))
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

# s = StackImplementUsingArray()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.display()
# s.find_y(40)
# print(s.middle_stack())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# s.find_y(40)
# # s.pop()
# # s.pop()
# # s.pop()
# s.display()

# class StackImplementUsingLinkedList:
#     def __init__(self):
#         self.head = None
#         self.sz = 0
#     def push(self, x):
#         temp = Node(x)
#         temp.next = self.head
#         self.head = temp
#         self.sz += 1
#     def pop(self):
#         if self.head == None:
#             return 'Stack Empty'
#         res = self.head.data
#         self.head = self.head.next
#         self.sz -= 1
#         return res
#     def display(self):
#         curr = self.head
#         while curr.next is not None:
#             print(curr.data, end = " ")
#             curr = curr.next
#     def size(self):
#         return self.sz

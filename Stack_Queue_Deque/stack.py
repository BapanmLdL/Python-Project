from collections import deque


def check_balance(a, b):
    return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')

def check_balanced_parenthese(str):
    stack = []
    for e in str:
        if e in ('(', '{', '['):
            stack.append(e)
        elif not stack:
            return False
        else:
            if not check_balance(stack[-1], e):
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

# s = "((())"
# print(check_balanced_parenthese(s))

def stock_span_naive(arr):
    for i in range(len(arr)):
        span = 1
        j = i - 1
        while j >= 0 and arr[i] >= arr[j]:
            span += 1
            j -= 1
        print(span, end=" ")


def stock_span(arr):
    stack = []
    stack.append(0)
    print(1, end=" ")
    
    for i in range(1, len(arr)):
        
        while (len(stack) > 0 and arr[stack[-1]] <= arr[i]):
            stack.pop()
        
        span = (i + 1) if len(stack) == 0 else i - stack[-1]
        print(span, end= " ")
        stack.append(i)


def previous_greater(arr):
    stack = []
    print(-1, end=" ")
    stack.append(arr[0])
    
    for i in range(1, len(arr)):
        
        while (len(stack) > 0 and stack[-1] <= arr[i]):
            stack.pop()
        
        prev_greater = -1 if len(stack) == 0 else stack[-1]
        print(prev_greater, end=" ")
        stack.append(arr[i])
        
def next_greater_naive(arr):
    for i in range(len(arr)):
        ng = -1
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                ng = arr[j]
                break
        print(ng, end=" ")

def next_greater(arr):
    stack = []
    res = [None] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        
        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(arr[i])
    
    for x in res:
        print(x, end=" ")

def getmax_hist_area_naive(arr):
    res = 0
    for i in range(len(arr)):
        curr = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                curr += arr[i]
            else:
                break
        for j in range(i+1, len(arr), 1):
            if arr[j] >= arr[i]:
                curr += arr[i]
            else:
                break
        
        res = max(res, curr)
    return res


# def get_prev_smaller(arr):
#     res = [None] * len(arr)
#     stack = []
#     res[0] = -1
#     stack.append(arr[0])
    
#     for i in range(1, len(arr)):
#         while len(stack) > 0 and stack[-1] > arr[i]:
#             stack.pop()
        
#         res[i] = -1 if len(stack) == 0 else stack[-1]
#         stack.append(arr[i])
    
#     return res


# def get_next_smaller(arr):
#     res = [None] * len(arr)
#     stack = []
    
#     for i in range(len(arr)-1, -1, -1):
#         while len(stack) > 0 and stack[-1] > arr[i]:
#             stack.pop()
        
#         res[i] = len(arr) if len(stack) == 0 else stack[-1]
#         stack.append(arr[i])
    
#     return res

# def getmax_area_hist(arr):
#     ps = get_prev_smaller(arr)
#     ns = get_next_smaller(arr)
    
#     res = 0
#     for i in range(len(arr)):
#         curr = arr[i]
#         curr += (i - ps[i] - 1) * arr[i]
#         curr += (ns[i] - i - 1) * arr[i]
#         res = max(res, curr)
    
#     return res


# lst = get_next_smaller([6, 2, 5, 4, 1, 5, 6])
# lst1 = get_prev_smaller([6, 2, 5, 4, 1, 5, 6])
# print(lst)
# print(lst1)

# area = getmax_area_hist([6, 2, 5, 4, 1, 5, 6])
# print(area)
    
# next_greater([13, 15, 12, 14, 16, 8, 16, 4, 10, 30])
# print('\n')
# next_greater([10, 20, 30, 40])
# print('\n')
# next_greater([40, 30, 20, 10])
# arr = [1, 3, 5, 9, 2]
# print(arr.pop(-2))

def next_smaller(arr):
    ns = [None] * len(arr)
    stack = []
    
    for i in range(len(arr)-1, -1, -1):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        ns[i] = len(arr) if len(stack) == 0 else stack[-1]
        
        stack.append(i)
    
    return ns


def prev_smaller(arr):
    ps = [None] * len(arr)
    stack = []
    
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        ps[i] = -1 if len(stack) == 0 else stack[-1]
        
        stack.append(i)
    
    return ps

def getmax_area_hist(arr):
    
    ns = next_smaller(arr)
    ps = prev_smaller(arr)
    
    area = 0
    for i in range(len(arr)):
            
        h = arr[i]
        w = ns[i] - ps[i] - 1
        
        newArea = h * w
        area = max(area, newArea)
    
    return area

heights = [[0, 1], [1, 0]]
area = []

for height in heights:
    area.append(getmax_area_hist(height))

print('Areas:', area)

# area = getmax_area_hist(heights)
# print("Area:", area)


def largest_area_rectangle_1s(matrix):
    if len(matrix) == 0:
        return 0
    
    firstRow = matrix[0]
    maxArea = getmax_area_hist(firstRow)
    
    # a = [0]*len(matrix[0])
    # maxArea = 0
    
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] == 1:
                firstRow[j] += 1
                
            elif matrix[i][j] == 0:
                firstRow[j] = 0
        
        newArea = getmax_area_hist(firstRow)
        
        maxArea = max(maxArea, newArea)
    
    return maxArea

# matrix = [
#     [1, 1, 1, 1, 1, 0], 
#     [1, 1, 1, 1, 0, 1], 
#     [1, 1, 0, 1, 1, 1], 
#     [1, 1, 1, 1, 1, 1]
#     ]

m = [[0, 1], [1, 0]]

area = largest_area_rectangle_1s(m)
print(area)

def insert_at_bottom(stack, ele):
    
    if len(stack) == 0:
        stack.append(ele)
        return
    
    topEle = stack.pop()
    insert_at_bottom(stack, ele)
    
    stack.append(topEle)


def reverse_stack(stack):
    if len(stack) == 1:
        return stack
    
    topEle = stack.pop()
    
    reverse_stack(stack)
    
    insert_at_bottom(stack, topEle)

def solve(stack, k):
    if k == 1:
        stack.pop()
        return stack
    
    topEle = stack.pop()
    
    solve(stack, k-1)
    
    stack.append(topEle)
    

def delete_middle_of_stack(stack, size):
    
    if len(stack) == 0:
        return stack
    
    mid = size // 2 + 1
    solve(stack, mid)
    
    return stack
 

# stack = deque([0, 5, 3, 2, 1, 7])
# delete_middle_of_stack(stack, len(stack))
# print(stack)



class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        maxArea = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    dp[c] += 1
                else:
                    dp[c] = 0
            maxArea = max(maxArea, self.maxRectangleInHistogram(dp))
        return maxArea

    def maxRectangleInHistogram(self, heights):  # O(N)
        n = len(heights)
        st = [-1]
        maxArea = 0
        for i in range(n):
            while st[-1] != -1 and heights[st[-1]] >= heights[i]:
                currentHeight = heights[st.pop()]
                currentWidth = i - st[-1] - 1
                maxArea = max(maxArea, currentWidth * currentHeight)
            st.append(i)
        while st[-1] != -1:
            currentHeight = heights[st.pop()]
            currentWidth = n - st[-1] - 1
            maxArea = max(maxArea, currentWidth * currentHeight)
        return maxArea
    
    def largest_area_rectangle_1s(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        firstRow = [int(e) for e in matrix[0]]
        print(firstRow)
        maxArea = self.maxRectangleInHistogram(firstRow)
        print(maxArea)
        # a = [0]*len(matrix[0])
        # maxArea = 0
    
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    firstRow[j] += 1
                
                elif int(matrix[i][j]) == 0:
                    firstRow[j] = 0
                    
            print(firstRow)
            newArea = self.maxRectangleInHistogram(firstRow)
            print(newArea)
            maxArea = max(maxArea, newArea)
        # print(maxArea)
        return maxArea
    
s = Solution()
area = s.largest_area_rectangle_1s(matrix = [["0", "1"], ["1", "0"]])
print('....', area)


    
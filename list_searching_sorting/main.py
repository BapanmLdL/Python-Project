# arr = [-5, 4, 6, -3, 4, -1]
# arr_2d = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         dummy = []
#         for k in range(i, j):
#             dummy.append(arr[k])
#         arr_2d.append(dummy)

# s = 0
# for e in arr_2d:
#     s = max(s, sum(e))

# print(s)


# Kadane's Algorithm
def max_Sum_Subarray(arr):
    maxSum = 0
    currSum = 0
    
    for i in range(len(arr)):
        
        currSum += arr[i]
        
        if currSum > maxSum:
            maxSum = currSum
        
        if currSum < 0:
            currSum = 0
    
    return maxSum


# Kadane's Algorithm
def longest_even_odd_subarray(arr):
    res = 1
    curr = 1
    
    for i in range(1, len(arr)):
        
        if (arr[i] % 2 == 0 and arr[i-1] % 2 == 0) or (arr[i] % 2 != 0 and arr[i-1] % 2 != 0):
            curr += 1
            res = max(curr, res)
        
        else:
            curr = 1
    
    return res


def findMajority(arr):
    n = len(arr)
    candi = 0
    cnt = 1
    
    for i in range(1, n):
        if arr[candi] == arr[i]:
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            candi = i
            cnt = 1
    
    count = 0
    for i in range(n):
        if arr[candi] == arr[i]:
            count += 1
    
    return -1 if count <= n//2 else candi


def window_sliding(arr, k):
    n = len(arr)
    curr = 0
    
    for i in range(k):
        curr += arr[i]
    
    import math
    res = - math.inf
    for i in range(k, n):
        curr = curr + arr[i] - arr[i-k]
        res = max(res, curr)
    
    return res  


def subArray_givenSum(arr, Sum):
    s, curr = 0, 0
    
    for e in range(len(arr)):
        curr += arr[e]
        
        while curr > Sum:
            curr -= arr[s]
            s += 1
        
        if curr == Sum:
            return True
    
    return False  


def get_sum(arr, l, r):
    pSum = [0]*len(arr)
    pSum[0] = arr[0]
    for i in range(1, len(arr)):
        pSum[i] = pSum[i-1] + arr[i]    
    
    return pSum[r] if l == 0 else pSum[r] - pSum[l-1]


def ePoint(arr):
    rs = sum(arr)
    ls = 0
    
    for i in range(len(arr)):
        rs -= arr[i]
        
        if rs == ls:
            return True
        
        ls += arr[i]
    
    return False

# arr = [-5, 4, 6, -3, 4, -1]
# arr = [5, 10, 20, 6, 3, 8]
# arr = [8, 3, 4, 8, 8, 9]
# arr = [1, 8, 30, 5, 20, 7]
# arr = [2, 8, 3, 9, 6, 5, 4]
arr = [3, 4, 8, -9, 9, 7]
# print(max_Sum_Subarray(arr))
# print(longest_even_odd_subarray(arr))
# majority = findMajority(arr)
# print(majority)
# s = window_sliding(arr, 4)
# print(s)
# print(subArray_givenSum(arr, 32))
# Sum = get_sum(arr, 1, 3)
# print(Sum)
print(ePoint(arr))
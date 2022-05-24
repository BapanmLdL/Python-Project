import sys
import random
def closestNumbers(arr):
    mn_diff = sys.maxsize
    pairs = []
    arr.sort()
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) < mn_diff:
            mn_diff = abs(arr[i] - arr[i-1])
            pairs = [arr[i-1], arr[i]]
        elif abs(arr[i] - arr[i-1]) == mn_diff:
            pairs.extend([arr[i-1], arr[i]])
    return pairs
# arr = list(map(int,input().rstrip().split()))
# print(closestNumbers(arr))
def minimumAbsoluteDifference(arr):
    mn = sys.maxsize
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff <= mn:
                mn = diff
    return mn
# arr = list(map(int,input().rstrip().split()))
# print(minimumAbsoluteDifference(arr))

def minimumAbsoluteDifference_nlogn(arr):
    arr.sort()
    mn = sys.maxsize
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if diff <= mn:
            mn = diff
    return mn
# arr = list(map(int,input().rstrip().split()))
# print(minimumAbsoluteDifference_nlogn(arr))
def maxMin(k, arr):
    arr.sort()
    mn = sys.maxsize
    j = k-1
    i = 0
    subarray = []
    while j <= (len(arr) - 1):
        unfairness = arr[j] - arr[i]
        if unfairness <= mn:
            mn = unfairness
            subarray = arr[i:(j+1)]
        j += 1
        i += 1
    return mn, subarray
# arr = list(map(int,input().rstrip().split()))
# print(maxMin(12, arr))
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    lc,uc,d,sp = 0,0,0,0
    for s in password:
        if s in numbers:
            d += 1
        elif s in lower_case:
            lc += 1
        elif s in upper_case:
            uc += 1
        elif s in special_characters:
            sp += 1
    if d >= 1:
        d = 1
    else:
        d = 0
    if lc >= 1:
        lc = 1
    else:
        lc = 0
    if uc >= 1:
        uc = 1
    else:
        uc = 0
    if sp >= 1:
        sp = 1
    else:
        sp = 0
    mandatory_char = (4 - (d+lc+uc+sp))
    mandatory_len = (6 - len(password))
    return max(mandatory_len, mandatory_char)
# pw = '2bbbb'
# n = 5
# print(minimumNumber(n, pw))
def dynamicArray(n, queries):
    Seqlist = [[] for _ in range(n)]
    LastAnswer = 0
    result = []
    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ LastAnswer) % n
            Seqlist[idx].append(q[2])
        else:
            idx = (q[1] ^ LastAnswer) % n
            v = q[2] % len(Seqlist[idx])
            LastAnswer = Seqlist[idx][v]
            result.append(LastAnswer)
    return result

# def missingNumbers(arr, brr):
#     res = []
#     for i in range(len(brr)):
#         for j in range(len(arr)):
#             if arr[j] == brr[i]:
#                 arr[j] = - sys.maxsize
#                 break
#         else:
#             res.append(brr[i])
#     return sorted(res)

def missingNumbers(arr, brr):
    freq = [0]*(max(brr) + 1)
    for e in brr:
        freq[e] += 1
    for f in arr:
        freq[f] -= 1
    res = []
    idx = 0
    for fr in freq:
        if fr > 0:
            res.append(idx)
            idx += 1
        else:
            idx += 1
    return res
# arr = [7,2,5,3,5,3]
# brr = [7,2,5,4,6,3,5,3,1,1]
# print(missingNumbers(arr, brr))
def COUNTINGSORT(arr, k):
    n = len(arr)
    count = [0]*k
    for e in arr:
        count[e] += 1
    for i in range(1, k):
        count[i] = count[i-1] + count[i]
    output = [0]*n
    i = n-1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr
# arr = [1,4,4,1,0,1]
# k = 5
# print(COUNTINGSORT(arr, k))

def gridChallenge(grid):
    M = [list(row) for row in grid]
    n = len(M)
    m = len(M[0])
    for i in range(n):
        M[i].sort()
    for j in range(m):
        for i in range(1, n):
            if M[i-1][j] > M[i][j]:
                return 'No'
    return 'Yes'
# grid = ['abc', 'ade', 'efg']
# print(gridChallenge(grid))
def sansaXor(arr):
    n = len(arr)
    if n % 2 == 0:
        return 0
    else:
        result = 0
        for i in range(0, n, 2):
            result ^= arr[i]
        return result
def balancedSums(arr):
    Sum = sum(arr)
    x = 0
    for i in range(len(arr)):
        y = arr[i]
        if (2*x) == (Sum - y):
            return "YES"
        else:
            x += arr[i]
    return "NO"
# arr = [2,0,0,0]
# print(balancedSums(arr))
def gamingArray(arr):
    cnt = 0
    mx = -999999
    for e in arr:
        if e > mx:
            mx = e
            cnt += 1
    return "ANDY" if(cnt % 2) else "BOB"
# arr = [3,5,4]
# print(gamingArray(arr))
def formingMagicSquare(s):
    n = len(s)
    m = len(s[0])
    cost = 0
    for i in range(n):
        for j in range(1):
            # print(s[i][j] + s[i][j+1] + s[i][j+2])
            Sum = s[i][j] + s[i][j+1] + s[i][j+2]
            # print(Sum)
            if Sum != 15:
                cost += abs(15 - Sum)
    # for j in range(m):
    #     for i in range(1):
    #         if s[i][j] + s[i+1][j] + s[i+2][j] != 15:
    #             cnt += 1
    return cost
# s = [[2,5,4], [4,6,9], [4,5,2]]
# print(formingMagicSquare(s))
def R(n):
    # n = int(n)
    if n >= 0 and n < 10:
        return n
    sm = R(n//10)
    ans = (n % 10) + sm
    return ans
def superDigit(n, k):
    num = int(n)
    while len(str(num)) != 1:
        num = R(num)
    no = num*k
    while len(str(no)) != 1:
        no = R(no)
    return no
# n = '999999999999999999999999'
# k = 99999999
# print(superDigit(n, k))

def firstindex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    isPresentinSmallPart = firstindex(arr[1:], x)
    if isPresentinSmallPart == -1:
        return -1
    else:
        return isPresentinSmallPart + 1
def firstindexBetter(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    else:
        return firstindexBetter(arr, x, si+1)
def lastindex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    isPresentinSmallerPart = lastindex(arr[1:], x)
    if isPresentinSmallerPart != -1:
        return isPresentinSmallerPart + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
def lastindexBetter(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    isPresentinSmallerPart = lastindexBetter(arr, x, si+1)
    if isPresentinSmallerPart != -1:
        return isPresentinSmallerPart
    else:
        if arr[si] == x:
            return si
        else:
            return -1
# arr = [1,2,9,4,9,7,11]
# print(lastindexBetter(arr, 9, 0))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

# def mergeLists(head1, head2):
#     curr1 = head1
#     curr2 = head2
#     while curr1 != None and curr2 != None:
#         if curr1.data >= curr2.data:
#             temp = curr2
#             temp.next = curr1
#             curr1 = temp.next
#             curr2 = curr2.next
#         else:
#             curr1 = curr1.next
#     return head1
# head1 = Node(4)
# head1.next = Node(5)
# head1.next.next = Node(6)
# head2 = Node(1)
# head2.next = Node(2)
# head2.next.next = Node(10)
# out = mergeLists(head1, head2)
# PrintLinkedList(out)










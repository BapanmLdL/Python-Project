import sys
import random
import math

def Time_Conversion(String):
    if String[-2:] == 'PM' and String[:2] != '12':
        String = str(12 + int(String[:2])) + String[2:]
    elif String[-2:] == 'AM' and String[:2] == '12':
        String = '00' + String[2:]
    return String[:-2]
# s = input()
# out = Time_Conversion(s)
# print(out)

def Breaking_Record(scores):
    n = len(scores)
    min, max = scores[0], scores[0]
    min_c, max_c = 0, 0
    for i in range(1, n):
        if scores[i] > max:
            max = scores[i]
            max_c += 1
        elif scores[i] < min:
            min = scores[i]
            min_c += 1
    return max_c, min_c
# arr = list(map(int,input().rstrip().split()))
# out = Breaking_Record(arr)
# print(out)

def Camel_Case(s):
    c = 0
    for e in s:
        if (e >= 'A') and (e <= 'Z'):
            c += 1
    return c+1
# s = input()
# out = Camel_Case(s)
# print(out)

def Sparse_Array(Strings, Queries):
    result = []
    for e in Queries:
        c = 0
        for f in Strings:
            if e == f :
                c +=1
        result.append(c)
    return result
# Strings = list(map(str,input().rstrip().split()))
# Queries = list(map(str,input().rstrip().split()))
# out = Sparse_Array(Strings, Queries)
# print(out)

def gradingStudents(grades):
    n = len(grades)
    for i in range(n):
        for j in range(40, 101, 5):
            if ((j - grades[i]) < 3) and ((j - grades[i]) > 0):
                grades[i] = j
    return grades
# arr = list(map(int,input().rstrip().split()))
# out = gradingStudents(arr)
# print(out)

def Flipping_bits(n):
    ans = 0
    multiplication = 1
    Db = 2
    Sb = 10
    while n > 0 :
        rem = (n % Db)
        ans = ans + (rem * multiplication)
        multiplication *= Sb
        n = n // Db

    ans_list = [int(x) for x in str(ans)]
    d = len(ans_list)
    d_list = [0]*(32 - d)
    binary_list = d_list + ans_list

    flip_binary_list = binary_list
    for i in range(len(flip_binary_list)):
        if flip_binary_list[i] == 0:
            flip_binary_list[i] = 1
        else:
            flip_binary_list[i] = 0

    string = [str(e) for e in flip_binary_list]
    string_ = "".join(string)

    m = int(string_)
    sB = 2
    dB = 10
    mul = 1
    convert = 0
    while m > 0:
        r = (m % dB)
        convert = convert + (r * mul)
        mul *= sB
        m = m // dB
    return convert
# n = int(input())
# out = Flipping_bits(n)
# print(out)

def Counting_Sort_1(arr):
    result = [0]*100
    for i in range(len(arr)):
        for j in range(len(result) + 1):
            if arr[i] == j :
                result[j] += 1
    return result
# arr = list(map(int,input().rstrip().split()))
# out = Counting_Sort_1(arr)
# print(out)

def countingValleys(steps, path):
    valley_count = level = 0
    d = {'U': 1, 'D': -1}
    for step in path:
        level = level + d[step]
        if (level == 0) and (step == 'U'):
            valley_count += 1
    return valley_count
# path = input()
# steps = 8
# out = countingValleys(steps, path)
# print(out)

def pangrams(s):
    UC = set(s.lower()) - set(' ')
    if len(UC) == 26:
        return 'pangram'
    else:
        return 'not pangram'
# s = input()
# out = pangrams(s)
# print(out)

def marsExploration(s):
    count = 0
    n = len(s)
    i = 0
    while i < n :
        if s[i] != 'S':
            count += 1
        if s[i+1] != 'O':
            count += 1
        if s[i+2] != 'S':
            count += 1
        i += 3
    return count
# s = input()
# out = marsExploration(s)
# print(out)

def Permuting_Two_arrays(A, B, k):
    Ap = sorted(A)
    Bp = sorted(B, reverse = True)
    for i in range(len(A)):
        if Ap[i] + Bp[i] < k :
            return 'NO'
    return 'YES'
# A = list(map(int,input().rstrip().split()))
# B = list(map(int,input().rstrip().split()))
# k = 10
# out = Permuting_Two_arrays(A, B, k)
# print(out)

def birthday(s, d, m):
    c = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:(m+i)]) == d :
            c += 1
    return c
# A = list(map(int,input().rstrip().split()))
# d, m = 4, 2
# out = birthday(A, d, m)
# print(out)

def sockMerchant(n, ar):
    pair = 0
    for i in range(n):
        for j in range(i+1, n):
            if ar[i] == ar[j] :
                pair += 1
                ar[i] = - sys.maxsize + i
                ar[j] = sys.maxsize + j
                break
    return pair
# n = int(input())
# ar = list(map(int,input().rstrip().split()))
# out = sockMerchant(n, ar)
# print(out)

def sockMerchant_Better(n, ar):
    pair = 0
    d = {}
    for e in ar:
        d[e] = d.get(e, 0) + 1
    for f in d.keys():
        pair += d[f] // 2
    return pair
# n = int(input())
# ar = list(map(int,input().rstrip().split()))
# out = sockMerchant_Better(n, ar)
# print(out)

def migratoryBirds(arr):
    count = [0]*len(arr)
    for i in range(len(arr)):
        count[arr[i]] += 1
    return count.index(max(count))
# arr = list(map(int,input().rstrip().split()))
# print(migratoryBirds(arr))

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse = True)
    for i in range(len(sticks) - 2):
        if sticks[i] < (sticks[i+1] + sticks[i+2]) :
            return [sticks[i+2], sticks[i+1], sticks[i]]
    else:
        return [-1]
# arr = list(map(int,input().rstrip().split()))
# print(maximumPerimeterTriangle(arr))

def findZigZagSequence(a):
    a.sort()
    n = len(a)
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    return a
# arr = list(map(int,input().rstrip().split()))
# print(findZigZagSequence(arr))

def pageCount(n,p):
    if n % 2 != 0 :       # odd n
        c1 = p // 2    # from left
        c2 = (n - p) // 2    # from right
    else:                # even n
        c1 = p // 2
        c2 = (n - p + 1) // 2
    return min(c1, c2)
# n = int(input())
# p = int(input())
# print(pageCount(n,p))

def pickingNumbers(a):
    count = [0]*100
    for e in a:
        count[e] += 1
    c = -1
    for i in range(len(count) - 1):
        c = max(c, (count[i] + count[i+1]))
    return c
# arr = list(map(int,input().rstrip().split()))
# print(pickingNumbers(arr))

def rotateLeft(d, arr):
    temp = [None]*(len(arr) - d)
    j = 0
    for i in range(d, len(arr)):
        temp[j] = arr[i]
        j += 1
    return temp + arr[0:d]
# arr = list(map(int,input().rstrip().split()))
# d = 2
# print(rotateLeft(d, arr))

def kangaroo(x1, v1, x2, v2):
    # epsilon = 1e-8
    if v1 == v2:
        return 'NO'
    j = (x2 - x1) / (v1 - v2)
    if (j > 0) and ((x2 - x1) % (v1 - v2) == 0):
        return 'YES'
    else:
        return 'NO'
x1, v1, x2, v2 = 1, 8, 3, 12
print(kangaroo(x1, v1, x2, v2))




















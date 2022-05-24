import math
def power(x, n):
    if n == 0:
        return 1
    if (n == 0) and (x == 0):
        return 1
    sm = power(x, (n-1))
    output = x * sm
    return output
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end = " ")
    print_n_to_1(n-1)
def fib(n):
    if n == 1 or n == 2:
        return 1
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    return fib_n_1 + fib_n_2
def fact(n):
    if n == 0:
        return 1
    smalloutput = fact(n-1)
    output = n * smalloutput
    return output
def isSorted(arr):
    l = len(arr)
    if l == 0 or l == 1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        return isSorted(arr[1:])
def IsSorted(arr):
    l = len(arr)
    if l == 0 or l == 1:
        return True
    if arr[0] > arr[1]:
        return False
    smallerarr = arr[1:]
    isSmallerarrSorted = IsSorted(smallerarr)
    # return isSmallerarrSorted
    if isSmallerarrSorted:
        return True
    else:
        return False
def SUM(arr):
    if len(arr) == 0:
        return 0
    SumOnSmallerArr = SUM(arr[1:])
    output = arr[0] + SumOnSmallerArr
    return output
def find_x(arr, x):
    if len(arr) == 0:
        return False
    if arr[0] == x:
        return True
    else:
        return find_x(arr[1:], x)
def isSortedUsingIndex(arr, si):
    l = len(arr)
    if si == l or si == (l-1):
        return True
    if arr[si] > arr[si+1]:
        return False
    else:
        return isSortedUsingIndex(arr, si+1)
def firstIndexBetter(arr, x=None, si=None):
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    else:
        return firstIndexBetter(arr, x, si+1)
def firstIndex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    isPresent = firstIndex(arr[1:], x)
    if isPresent == -1:
        return -1
    else:
        return isPresent + 1
def LastIndex(arr, x, ei):
    l = len(arr)
    if ei == -1:
        return -1
    if arr[ei] == x:
        return ei
    else:
        return LastIndex(arr, x, ei - 1)
def lastindex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    smalloutput = lastindex(arr[1:], x)
    if smalloutput != -1:
        return smalloutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
def lastindexBetter(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    smalloutput = lastindexBetter(arr, x, si+1)
    if smalloutput != -1:
        return smalloutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1
# arr = [1,2,3,2,40,5,6,3,7]
# # x = 70
# print(lastindexBetter(arr, -2, 0))
# n = int(input())
# print(fact(n))
# print(fib(n))
# # x = int(input())
# n = int(input())
# print_n_to_1(n)
# # print(power(x, n))
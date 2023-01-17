import math


def BinarySearch(arr, x):
    
    def wrapper(arr, x, si=0, ei=len(arr)-1):
        if si > ei:
            return -1
        
        mid = (si + ei) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return wrapper(arr, x, si, mid-1)
        else:
            return wrapper(arr, x, mid+1, ei)
    
    return wrapper(arr, x)


def search(arr, x):
    
    def wrapper(arr, x, si=0, ei=len(arr)-1):
        if si > ei:
            return -1
        
        mid = (si + ei) // 2
        
        if arr[mid] == x:
            return mid
        
        if si == mid:
            if arr[si] == x:
                return si
            else:
                return wrapper(arr, x, mid+1, ei)
        
        if ei == mid:
            if arr[ei] == x:
                return ei
            else:
                return wrapper(arr, x, si, mid-1)
        
        if arr[si] < arr[mid]:
            if arr[si] <= x < arr[mid]:
                return wrapper(arr, x, si, mid-1)
            else:
                return wrapper(arr, x, mid+1, ei)
        
        else:
            if arr[mid] < x <= arr[ei]:
                return wrapper(arr, x, mid+1, ei)
            else:
                return wrapper(arr, x, si, mid-1)
    
    return wrapper(arr, x)


def firstOccurance(arr, x):
    
    def solver(arr, x, si=0, ei=len(arr)-1):
        if si > ei:
            return -1
        
        mid = (si + ei) // 2
        
        if x > arr[mid]:
            return solver(arr, x, mid+1, ei)
        elif x < arr[mid]:
            return solver(arr, x, si, mid-1)
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                return solver(arr, x, si, mid-1)
    
    return solver(arr, x)


def lastOccurance(arr, x):
    
    def solver(arr, x, si=0, ei=len(arr)-1):
        
        if si > ei:
            return -1
        
        mid = (si + ei) // 2
        
        if x > arr[mid]:
            return solver(arr, x, mid+1, ei)
        elif x < arr[mid]:
            return solver(arr, x, si, mid-1)
        else:
            if mid == len(arr)-1 or arr[mid+1] != arr[mid]:
                return mid
            else:
                return solver(arr, x, mid+1, ei)
    
    return solver(arr, x)


def countOccurance(arr, x):
    first = firstOccurance(arr, x)
    
    if first == -1:
        return 0
    else:
        return lastOccurance(arr, x) - first + 1
    
    
def pairSum(arr, Sum, si=0):
    i = si
    j = len(arr)-1
    
    while j > i:
        x = arr[i] + arr[j]
        if x > Sum:
            j -= 1
        elif x < Sum:
            i += 1
        else:
            return True
    
    return False


def tripletSum(arr, Sum):
    for i in range(len(arr)):
        if pairSum(arr, Sum-arr[i], i):
            return True
    
    return False

# arr = [1, 5, 9, 20, 27, 30, 41, 57]
# print(BinarySearch(arr, 41))

# print(search([3, 1], 1))

# indx = lastOccurance([1, 10, 10, 10, 20, 20, 20, 40], 200)
# print(indx)
# arr = [1, 10, 10, 10, 10, 20, 20, 20, 40]
# occ = countOccurance(arr, x=400)
# print(occ)
# ispair = pairSum([2, 5, 8, 12, 30], 39)
# print(ispair)
istriplet = tripletSum([2, 3, 4, 8, 9, 20, 40], 34)
print(istriplet)
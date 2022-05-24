def ReplaceChar(s, x, y):
    if len(s) == 0:
        return s
    smalloutput = ReplaceChar(s[1:], x, y)
    if s[0] == x:
        return y + smalloutput
    else:
        return s[0] + smalloutput
# print(ReplaceChar('as', 'a', 'i'))
def RemoveX(string):
    if len(string) == 0:
        return string
    smalloutput = RemoveX(string[1:])
    if string[0] == 'x':
        return smalloutput
    else:
        return string[0] + smalloutput
# print(RemoveX('pxxp'))
def RemoveDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == s[1]:
        smalloutput = RemoveDuplicates(s[1:])
        return smalloutput
    else:
        smalloutput = RemoveDuplicates(s[1:])
        return s[0] + smalloutput
# print(RemoveDuplicates("aabccba"))
def RemovePi(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == 'p' and s[1] == 'i':
        smalloutput = RemovePi(s[2:])
        return '3.14' + smalloutput
    else:
        smalloutput = RemovePi(s[1:])
        return s[0] + smalloutput
# print(RemovePi("ppiabcpippipi"))
def BinarySearch(arr, x, si, ei):
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return BinarySearch(arr, x, mid+1, ei)
    elif arr[mid] > x:
        return BinarySearch(arr, x, si, mid-1)

# arr = [2,3,5,9,11,15,20,21]
# print(BinarySearch(arr, 2, 0, len(arr)-1))
def Merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i += 1
            k += 1
        else:
            arr[k] = a2[j]
            j += 1
            k += 1
    while i < len(a1):
        arr[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        arr[k] = a2[j]
        j += 1
        k += 1


def MergeSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return
    mid = len(arr) // 2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    MergeSort(a1)
    MergeSort(a2)
    Merge(a1, a2, arr)
# a = ['s', 'X', '@','a', '#', 'y', 'Q', 'q', '0']
# MergeSort(a)
# print(a)
def partition(arr, s, e):
    pivot = arr[s]
    cnt = 0
    for i in range(s, e+1):
        if arr[i] < pivot:
            cnt += 1
    arr[s+cnt], arr[s] = arr[s], arr[s+cnt]
    pivot_index = s + cnt
    i, j = s, e
    while i < j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] >= pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return pivot_index

def QuickSort(arr, s, e):
    if s >= e:
        return
    pivot_index = partition(arr, s, e)
    QuickSort(arr, s, pivot_index-1)
    QuickSort(arr, pivot_index+1, e)

# a = list(map(int,input().rstrip().split()))
# QuickSort(a, 0, len(a)-1)
# print(a)

def TowerOfHanoi(n, S, H, D):
    if n == 1:
        print("Move the 1st disc from", S, "to", D)
        return
    TowerOfHanoi((n-1), S, D, H)
    print("Move", n, "th disc from", S, "to", D)
    TowerOfHanoi((n-1), H, S, D)
# TowerOfHanoi(3, 'S', 'H', 'D')

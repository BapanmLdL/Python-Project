def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
# arr = [1,2,3,0,5]
# v = swap(arr, 1, 4)
# print(v)

def bubble_sort(arr):
    count = 0
    l = len(arr)
    while count < l-1:
        for i in range(l-1-count):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        count += 1
    return arr
# arr = [8,0,5,4,9,3,2,1,6]
# out = bubble_sort(arr)
# print(out)

def selection_sort(arr):
    counter = 0

    while counter < len(arr) - 1:
        min = counter
        for j in range(counter + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[counter]
        arr[counter] = arr[min]
        arr[min] = temp

        counter += 1
    return arr



def miniMaxSum(arr):
    mn_number = 9999999999999
    mx_number = -999999999999
    l = len(arr)
    s = 0

    for i in range(l):
        s += arr[i]
        mn_number = min(mn_number, arr[i])
        mx_number = max(mx_number, arr[i])
    print((s - mx_number), (s - mn_number))

# arr = list(map(int, input().rstrip().split()))
# miniMaxSum(arr)1

def divisible_sum_pair(arr, k):
    l = len(arr)
    count = 0

    for i in range(l):
        for j in range(i+1, l):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count
# arr = list(map(int, input().rstrip().split()))
# k = 3
# out = divisible_sum_pair(arr, k)
# print(out)

def lonely_integer(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        while j < n:
            if j != i:
                if arr[i] == arr[j]:
                    break
            j += 1
        if j == n:
            return arr[i]
# arr = list(map(int, input().rstrip().split()))
# out = lonely_integer(arr)
# print(out)

def swap_alternate(arr):
    n = len(arr)

    if n % 2 == 0:
        for i in range(0, n, 2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    else:
        for i in range(0, (n-1), 2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    return arr
# arr = list(map(int, input().rstrip().split()))
# out = swap_alternate(arr)
# print(out)

def duplicates(arr):
    n = len(arr)

    for i in range(n):
        j = 0
        while j < n :
            if j != i :
                if arr[i] == arr[j]:
                    return arr[i]
            j += 1
    return -1
# arr = list(map(int, input().rstrip().split()))
# out = duplicates(arr)
# print(out)
import sys
def array_intersection(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    l = []

    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j]:
                l.append(arr1[i])
                arr2[j] = - sys.maxsize
                break
    return l
# arr1 = list(map(int, input().rstrip().split()))
# arr2 = list(map(int, input().rstrip().split()))
# out = array_intersection(arr1, arr2)
# print(out)

def pair_sum(arr, x):
    c = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == x:
                c += 1
    return c
# arr = list(map(int,input().rstrip().split()))
# x = 7
# out = pair_sum(arr, x)
# print(out)

def triplet_sum(arr, x):
    c = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k]) == x:
                    c = c+1
    # for i in range(n-2):
    #     if (arr[i] + arr[i+1] + arr[i+2]) == x:
    #         c += 1
    return c
# arr = list(map(int,input().rstrip().split()))
# x = 10
# out = triplet_sum(arr, x)
# print(out)

def sort_0_1(arr):
    n = len(arr)
    i = 0
    j = n-1

    while j > i :
        if arr[i] == 0:
            i += 1
        elif arr[j] == 1:
            j -= 1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    return arr
# arr = list(map(int,input().rstrip().split()))
# out = sort_0_1(arr)
# print(out)

def push_zeros_to_end(arr):
    n = len(arr)
    k = 0
    l = 0
    temp1 = []
    temp2 = []
    for i in range(n):
        if arr[i] != 0:
            temp1.insert(k, arr[i])
            k += 1
        else:
            temp2.insert(l, arr[i])
            l += 1
    return temp1 + temp2
# arr = list(map(int,input().rstrip().split()))
# out = push_zeros_to_end(arr)
# print(out)

def rotate_array(arr, d):
    n = len(arr)
    for _ in range(d):
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
    return arr
# arr = list(map(int,input().rstrip().split()))
# d = 2
# out = rotate_array(arr, d)
# print(out)

def rotate_array_approach2(arr, d):
    n = len(arr)
    temp = []

    for i in range(d):
        temp.insert(i, arr[i])
    temp2 = []
    for j in range(n-d):
        temp2.insert(j, arr[j+d])
        # arr[j] = arr[j+d]

    result = temp2 + temp
    return result
# arr = list(map(int,input().rstrip().split()))
# d = 2
# out = rotate_array_approach2(arr, d)
# print(out)

# def rotate_array_approach3(arr, d):
#     n = len(arr)
#     arr.reverse()
#     temp1 = arr[0 : (n-d)]
#     temp2 = arr[(n-d) : n]
#     return temp1 + temp2
# arr = list(map(int,input().rstrip().split()))
# d = 2
# out = rotate_array_approach3(arr, d)
# print(out)

def second_largest(arr):
    n = len(arr)
    largest = - sys.maxsize

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    s_largest = - sys.maxsize
    for j in range(n):
        if (arr[j] > s_largest) and (arr[j] < largest):
            s_largest = arr[j]

    return s_largest
# arr = list(map(int,input().rstrip().split()))
# out = second_largest(arr)
# print(out)

# def second_largest_approach2(arr):
#     n = len(arr)
#     L = - sys.maxsize
#     SL = - sys.maxsize
#
#     for i in range(n):
#         if arr[i] > L:
#             SL = L
#             if arr[i] > SL:
#                 L = arr[i]
#     return SL
# arr = list(map(int,input().rstrip().split()))
# out = second_largest_approach2(arr)
# print(out)

def check_array_rotation(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1] :
            return i+1
# arr = list(map(int,input().rstrip().split()))
# out = check_array_rotation(arr)
# if out is None:
#     print(0)
# else:
#     print(out)

def sort_0_1_2(arr):
    n = len(arr)
    temp1 = []
    temp2 = []
    temp3 = []

    for i in range(n):
        # print(i)
        if arr[i] == 0:
            temp1.append(arr[i])
        elif arr[i] == 1:
            temp2.append(arr[i])
        else:
            temp3.append(arr[i])
    return temp1 + temp2 + temp3
# arr = list(map(int,input().rstrip().split()))
# out = sort_0_1_2(arr)
# print(out)

def sort_0_1_2_approach2(arr):
    n = len(arr)
    temp = [1]*n
    nZ = 0
    nT = n-1

    for i in range(n):
        if arr[i] == 0:
            temp[nZ] = arr[i]
            nZ += 1
        elif arr[i] == 2:
            temp[nT] = arr[i]
            nT -= 1
    arr = temp
    return arr
# arr = list(map(int,input().rstrip().split()))
# out = sort_0_1_2_approach2(arr)
# print(out)




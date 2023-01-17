import math

def replace_char(s, a, b):
    if len(s) == 0:
        return s
    
    smalloutput = replace_char(s[1:], a, b)

    if s[0] == a:
        return b + smalloutput 
    else:
        return s[0] + smalloutput 


def remove_x(s):
    if len(s) == 0:
        return s 
    
    smallouput = remove_x(s[1:])

    if s[0] == 'x':
        return '' + smallouput
    else:
        return s[0] + smallouput 

def replace_pi(s):
    if len(s) == 0 or len(s) == 1:
        return s 
    
    if s[0] == 'p' and s[1] == 'i':
        smalloutput = replace_pi(s[2:])
        return '3.14' + smalloutput 
    else:
        smalloutput = replace_pi(s[1:]) 
        return s[0] + smalloutput 

# print(replace_pi('pipipipipipipipipipippi'))

class Node:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None 
    
    def printLL(self):
        curr = self 
        while curr is not None:
            print(curr.data, end = ' ')
            curr = curr.next
        print()
    
    def reverse(self):
        if self is None:
            return None 
        
        if self.next is None:
            return self 
        
        small_head = self.next.reverse()
        small_tail = self.next 
        small_tail.next = self 
        self.next = None 
        return small_head


def remove_consecutive_duplicates(s):
    if len(s) == 1:
        return s
    
    if s[0] == s[1]:
        smalloutput = remove_consecutive_duplicates(s[1:])
        return smalloutput
    else:
        smalloutput = remove_consecutive_duplicates(s[1:])
        return [s[0]] + smalloutput

def binary_search(lst, x, si, ei):
    if si > ei:
        return -1
    
    mid = (si + ei) // 2
    if lst[mid] == x:
        return mid 
    elif lst[mid] < x:
        return binary_search(lst, x, mid+1, ei)
    else:
        return binary_search(lst, x, si, mid-1)

def merge(l1, l2, lst):
    i = 0
    j = 0 
    k = 0 
    while j < len(l1) and k < len(l2):
        if l1[j] <= l2[k]:
            lst[i] = l1[j]
            i += 1 
            j += 1 
        else:
            lst[i] = l2[k]
            i += 1
            k += 1 
    while j < len(l1):
        lst[i] = l1[j] 
        i += 1 
        j += 1 
    while k < len(l2):
        lst[i] = l2[k]
        i += 1 
        k += 1 


def merge_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return 
    mid = len(lst) // 2
    l1 = lst[0:mid]
    l2 = lst[mid:]
    merge_sort(l1)
    merge_sort(l2)
    merge(l1, l2, lst)


    
def tower_of_hanoi(n, S, H, D):
    if n == 1:
        print(f"move the 1st disc from {S} to {D}")
        return 
    tower_of_hanoi((n-1), S, D, H)
    print(f"move {n}th disc from {S} to {D}")
    tower_of_hanoi((n-1), H, S, D)

def nos_of_move_tower_of_hanoi(n, S, H, D):
    if n == 1:
        return 1 
    first_n_1_move = nos_of_move_tower_of_hanoi((n-1), S, D, H)
    second_n_1_move = nos_of_move_tower_of_hanoi((n-1), H, S, D)
    return first_n_1_move + 1 + second_n_1_move

def partition(lst, s, e):
    pivot_ele = lst[s]
    cnt = 0 
    for i in range(s, e+1):
        if lst[i] < pivot_ele:
            cnt += 1 

    lst[s], lst[s+cnt] = lst[s+cnt], lst[s]
    pivot_index = s + cnt 

    i, j = s, e 
    while i < j:
        if lst[i] < lst[pivot_index]:
            i += 1 
        elif lst[j] >= lst[pivot_index]:
            j -= 1 
        else:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1 
    return pivot_index

def quick_sort(lst, s, e):
    if s >= e:
        return 
    i = partition(lst, s, e)
    
    quick_sort(lst, s, i-1)
    quick_sort(lst, i+1, e)

# lst = [3, 5, 9, 1, 2, 0, 8]
# merge_sort(lst)
# print(lst)

def subsequence_of_string(s):
    if len(s) == 0:
        output = []
        output.append("")
        return output
    
    smalloutput = subsequence_of_string(s[1:])

    output = []
    for sub in smalloutput:
        output.append(sub)
    for sub in smalloutput:
        output.append(s[0] + sub)

    return output 


def factorial_print(n, ans=1):
    if n == 0:
        print(ans)
        return 
    ans = ans * n 
    factorial_print((n-1), ans)

def keypad_combination(n):
    keypad_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 
                   6: 'mno',7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    if n == 0:
        output = [] 
        output.append("")
        return output
    
    small_int = n // 10
    rem_int = n % 10 
    smalloutput = keypad_combination(small_int)
    
    output = []
    for sub_comb in smalloutput:
        for e in keypad_dict[rem_int]:
            output.append(sub_comb + e)
    
    return output 
# output = keypad_combination(297)
# print(output)

def minimum_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    
    smalloutput = minimum_of_array(arr[1:])
    if arr[0] <= smalloutput:
        return arr[0]
    else:
        return smalloutput
    
def print_minimum(arr, min_so_far=math.inf):
    if len(arr) == 0:
        print(min_so_far)
        return 
    min_so_far = min(arr[0], min_so_far)
    print_minimum(arr[1:], min_so_far)

# lst = [3, 8, 0, 1, 6, 5, 1, 0, 7, 2]
# print_minimum(lst)

def print_subsequence_string(s, output=""):
    if len(s) == 0:
        print(output)
        return 
    print_subsequence_string(s[1:], output)
    print_subsequence_string(s[1:], output+s[0])

# print_subsequence_string('ab')

def print_keypad_combination(n, output=''):
    keypad_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 
                   6: 'mno',7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    
    if n == 0:
        print(output)
        return 
    
    small_int = n // 10
    rem_int = n % 10 
    
    for e in keypad_dict[rem_int]:
        print_keypad_combination(small_int, e + output)
    
# print_keypad_combination(234)

def subset_sum_to_k(arr, k, si=0):
    if si == len(arr):
        if k == 0:
            return [[]]
        else:
            return []
    sm1 = subset_sum_to_k(arr, k-arr[si], si+1)
    sm2 = subset_sum_to_k(arr, k, si+1)
    
    output = []
    for e in sm1:
        # e.append(arr[si])
        e = [arr[si]] + e 
        output.append(e)
    for f in sm2:
        output.append(f)
    
    return output

def subset_of_an_array(arr):
    if len(arr) == 0:
        return [[]]
    
    smalloutput = subset_of_an_array(arr[1:])
    
    output = []
    for e in smalloutput:
        output.append(e)
    for e in smalloutput:
        e = [arr[0]] + e
        output.append(e)
    
    return output

def print_subset_of_an_array(arr, output=[]):
    if len(arr) == 0:
        print(output)
        return 
    
    print_subset_of_an_array(arr[1:], output)
    print_subset_of_an_array(arr[1:], output + [arr[0]])
    
def print_subset_sum_to_k(arr, k, si=0, output=[]):
    if si == len(arr):
        if k == 0:
            print(output)
            return 
        else:
            return 
    
    print_subset_sum_to_k(arr, k - arr[si], si+1, [arr[si]] + output)
    print_subset_sum_to_k(arr, k, si+1, output)
    
# lst = [14,17, 17, 2, 20, 3, 16, 14, 2, 14, 15, 4, 13, 8, 15]   
# k = 2
# print_subset_sum_to_k(lst, k)    
# n = int(input('Enter size of arrray: '))
# arr = [int(x) for x in input().split()]
# print_subset_of_an_array(arr)

# lst = [1, 2, 3, 2, 4, 0, -8, -6, 7, -2]
# print_subset_sum_to_k(lst, 4)

# def permutation_of_string(s, si=0):
#     if si == len(s):
#         output = []
#         output.append("")
#         return output
#     # si += 1
#     smalloutput = permutation_of_string(s[:si-1] + s[si+1:], si+1)
    
#     output = []
#     for e in smalloutput:
#         e = s[si] + e 
#         output.append(e) 
#     return output
# print(permutation_of_string('adg'))    

def permutation_of_string(str):
    if len(str) == 0:
        output = []
        output.append("")
        return output

    smalloutput = permutation_of_string(str[1:])
    output = []
    for e in smalloutput:
        for i in range(len(e) + 1):
            output.append(e[:i] + str[0] + e[i:])
    return output

# def permutation_of_string2(str, si=-1):
#     if si == len(str):
#         output = []
#         output.append("")
#         return output
#     si += 1 
#     smalloutput = permutation_of_string2(str[:si] + str[(si+1):], si)
    
#     output = []
#     for e in smalloutput:
#         e = str[si] + e 
#         output.append(e)
#     return output

def print_permutations_of_string(str, output=''):
    if len(str) == 0:
        print(output)
        return 
    
    for i in range(len(str)):
        print_permutations_of_string(str[:i] + str[i+1:], str[i] + output)

# data = input("Enter the string: ")
# print(permutation_of_string(data))
# s = 'abcd'
# print_permutations_of_string(s)

def josephus(n, k):
    if n == 1:
        return 0
    
    return (josephus((n-1), k) + k) % n


def max_Pieces(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    
    result = max(
        max_Pieces((n-a), a, b, c), 
        max_Pieces((n-b), a, b, c),
        max_Pieces((n-c), a, b, c)
    )
    
    if result == -1:
        return -1
    
    return result + 1

# print(max_Pieces(23, 11, 9, 12))


            
    
    


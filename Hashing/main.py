from collections import Counter

def intersection(a, b):
    s_a = set(a)
    s_b = set(b)
    
    z = s_a.intersection(s_b)
    
    return len(list(z))

def intersectionBetter(a, b):
    cnt = 0
    s_a = set(a)
    
    for e in b:
        if e in s_a:
            cnt += 1
            s_a.remove(e)
    
    return cnt


def pairSum(nums, X):
    us = set()
    for e in nums:
        if X-e in us:
            return True
        us.add(e)
    
    return False


def subArray_Sum0(nums):
    prefix_sum = 0
    h = set() # {}
    
    for i in range(len(nums)):
        
        prefix_sum += nums[i]
        if prefix_sum in h:
            return True
        h.add(prefix_sum)
    
    return False


def PalindromePermutation(s):
    cnter = Counter(s)
    odd = 0
    
    for freq in cnter.values():
        if freq % 2 == 1:
            odd += 1
        
        if odd > 1:
            return False
        
    return True 
    

# a = [10, 15, 20, 5, 30]
# b = [30, 5, 30, 80]
# print(intersectionBetter(a, b))
# nums = [3, 2, 8, 15, -8]
# print(pairSum(nums, X=10))
# nums = [-3, 4, -3, -3, 1]
# print(subArray_Sum0(nums))
print(PalindromePermutation('aaaabbbbbbdddeee'))
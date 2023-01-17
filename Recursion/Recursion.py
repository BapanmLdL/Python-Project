# import sys 
# sys.setrecursionlimit(10000)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def sumnn(n):
    if n == 1:
        return 1
    
    sm_output = sumnn(n-1)
    output = sm_output + n 
    return output 

def power_x(x, n):
    """_summary_

    Args:
        x (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if x == 0:
        return 'Invalid input!.'

    if n == 0:   # base case
        return 1 
    sm_output = power_x(x, (n-1))
    output = x * sm_output
    return output

def printnn(n):
    if n == 0:
        return 
    
    printnn(n-1)
    print(n, end=" ")

def print_n_1(n):
    if n == 0:
        return 
    print(n, end = " ")
    print_n_1(n-1)

def fib(n):
    if n == 1 or n == 2 :
        return 1
    return fib(n-1) + fib(n-2)

def is_sorted(lst):
    if len(lst) == 0 or len(lst) == 1:
        return True
    
    if lst[0] > lst[1]:
        return False
    else:
        return is_sorted(lst[1:])

def is_sorted_better(lst, si=0):
    if si == len(lst) - 1 or si == len(lst):
        return True
    
    if lst[si] > lst[si + 1]:
        return False
    else:
        return is_sorted_better(lst, si+1)

def sum_recursively(lst):
    if len(lst) == 1:
        return lst[0]
    
    sumfromsmallerlst = sum_recursively(lst[1:])
    Sum = lst[0] + sumfromsmallerlst
    
    return Sum

def sum_recursively_better(lst, si=0):
    if si == len(lst) - 1:
        return lst[si]
    
    sumfromsmallerlst = sum_recursively_better(lst, si+1)
    Sum = lst[si] + sumfromsmallerlst

    return Sum 

def find_x(lst, x, si=0):
    if si == len(lst):
        return False
    
    if x == lst[si]:
        return True
    else:
        return find_x(lst, x, si+1)

def first_index(lst, x):
    if len(lst) == 0:
        return -1
    
    if lst[0] == x:
        return 0
    
    smalloutput = first_index(lst[1:], x)
    if smalloutput == 0:
        return smalloutput + 1 
    else:
        return -1

def first_index_better(lst, x, si=0):
    if si == len(lst):
        return -1 
    
    if lst[si] == x:
        return si
    else:
        return first_index_better(lst, x, si+1)
    
def last_index(lst, x):
    if len(lst) == 0:
        return -1
    
    smalloutput = last_index(lst[1:], x)
    if smalloutput == -1:
        if lst[0] == x:
            return 0
        else:
            return -1 
    else:
        return smalloutput + 1
    
def last_index_Better(lst, x, si=0):
    """_summary_

    Args:
        lst (_type_): _description_
        x (_type_): _description_
        si (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    if si == len(lst):
        return -1 
    
    smalloutput = last_index_Better(lst, x, si+1)
    if smalloutput == -1:
        if lst[si] == x:
            return si
        else:
            return -1 
    else:
        return smalloutput 
# n = int(input('please enter n:'))
# x = int(input('please enter x:'))
# print(power_x(x, n))
lst = [9, 8, 0, 1, 8, 3, 5, 9, 0]
x = -1
print(last_index_Better(lst, x))
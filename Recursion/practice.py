def return_substring(s):
    if len(s) == 0:
        output = []
        output.append("")
        return output
    
    smalloutput = return_substring(s[1:])
    
    output = []
    for e in smalloutput:
        output.append(e)
    for e in smalloutput:
        e = s[0] + e
        output.append(e)
    
    return output

def print_substrings(s, output=""):
    if len(s) == 0:
        print(output)
        return
    
    print_substrings(s[1:], output)
    print_substrings(s[1:],  output + s[0])
    
def return_subset_sum_to_k(arr, k):
    if len(arr) == 0:
        if k == 0:
            return [[]]
        else:
            return []
    
    sm1 = return_subset_sum_to_k(arr[1:], k-arr[0])
    sm2 = return_subset_sum_to_k(arr[1:], k)
    
    output = []
    
    for e in sm1:
        e = [arr[0]] + e
        output.append(e)
    
    for f in sm2:
        output.append(f)
    
    return output

def print_subset_sum_to_k(arr, k, output=[]):
    if len(arr) == 0:
        if k == 0:
            print(output)
            return
        else:
            return 
    
    print_subset_sum_to_k(arr[1:], k-arr[0], [arr[0]] + output)
    print_subset_sum_to_k(arr[1:], k, output)
    
def return_permutation_of_string(s):
    if len(s) == 0:
        output = []
        output.append("")
        return output
    
    output = []
    for i in range(len(s)):
        smalloutput = return_permutation_of_string(s[:i] + s[i+1:])
        for e in smalloutput:
            e = s[i] + e
            output.append(e)
    
    return output
    
def print_permutation_of_string(s, output=""):
    if len(s) == 0:
        print(output)
        return
    
    for i in range(len(s)):
        print_permutation_of_string(s[:i] + s[i+1:], s[i] + output)
        

def tower_of_hanoi(n, S='S', H='H', D='D'):
    if n == 1:
        print(f"put 1st disc from {S} to {D}")
        return
        
    tower_of_hanoi((n-1), S, D, H)
    print(f"put {n}th disc from {S} to {D}")
    tower_of_hanoi((n-1), H, S, D)   
    
def number_of_moves_in_tower_of_hanoi(n, S='S', H='H', D='D'):
    if n == 1:
        return 1
    
    first_n_1_move = number_of_moves_in_tower_of_hanoi((n-1), S, D, H)
    second_n_1_move = number_of_moves_in_tower_of_hanoi((n-1), H, S, D)
    
    return first_n_1_move + 1 + second_n_1_move
    
# moves = number_of_moves_in_tower_of_hanoi(10) 
# print(moves)
        
        
        
        

# print_permutation_of_string('agi')
# permutations = return_permutation_of_string("bapan")
# print(permutations)
# print(len(permutations))

        
# arr = [1, 2, 2, 3]
# k = 4
# print_subset_sum_to_k(arr, k)
# print(return_subset_sum_to_k(arr, k))

# substrings = return_substring("abcd")
# print(substrings)
# print_substrings('abc')



def subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print()

arr = [10, 20, 30, 40]
subarray(arr)
    
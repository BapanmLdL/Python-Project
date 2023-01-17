from collections import OrderedDict


class Node:
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def print_ll(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    
    
def add_two_numbers(h1, h2):
    dummy = Node()
    curr = dummy
    
    carry = 0
    while h1 or h2 or carry:
        v1 = h1.val if h1 else 0
        v2 = h2.val if h2 else 0
        
        
        val = v1 + v2 + carry
        
        carry = val // 10
        val = val % 10
        
        curr.next = Node(val)
        curr = curr.next
        
        h1 = h1.next if h1 else None
        h2 = h2.next if h2 else None
    
    return dummy.next

def rotate_ll(head, k):
    if head == None or k == 0:
        return head
    
    curr = head 
    n = 0
    while curr.next:
        curr = curr.next
        n += 1
    
    curr.next = head
    
    k = k % (n+1)
    curr = head
    for _ in range(n-k):
        curr = curr.next
    
    temp = curr.next
    curr.next = None
    return temp

def partition_list(head, x):
    ss, se, ls, le = None, None, None, None
    curr = head
    while curr:
        if curr.val < x:
            if ss==None:
                ss = curr
                se = ss
            else:
                se.next = curr
                se = se.next
        else:
            if ls == None:
                ls = curr
                le = ls
            else:
                le.next = curr
                le = le.next
                
        curr = curr.next
    
    if ss == None or ls == None:
        return head
    
    se.next = ls
    le.next = None
    return ss

def reverse(head):
    if head == None or head.next == None:
        return head
    
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev

def reverse_list_II(head, left, right):
    if left == right:
        return head
    
    curr = head 
    cnt = 1 
    prev = None
    while cnt != left:
        prev = curr
        curr = curr.next
        cnt += 1
    
    start = curr
    while cnt != right:
        curr = curr.next
        cnt += 1
    
    
    rest = curr.next
    curr.next = None
    rev_head = reverse(start)
    
    start.next = rest
    if left != 1:
        prev.next = rev_head
        return head
    else:
        return rev_head
    

def merge_two_sorted_list(a, b):
    if b == None:
        return a 
    if a == None:
        return b
    
    head, tail = None, None
    if a.val <= b.val:
        head = a
        tail = a
        a = a.next
    else:
        head = b
        tail = b
        b = b.next
    
    while a and b:
        if a.val <= b.val:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    
    if a:
        tail.next = a
    
    else:
        tail.next = b
    
    return head

def sort_list(head):
    if head == None or head.next == None:
        return head
    
    prev = None
    slow, fast = head, head
    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = None
    
    LL1 = sort_list(head)
    LL2 = sort_list(slow)
    return merge_two_sorted_list(LL1, LL2) 


def remove_duplicates_II(head):
    
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    
    while head and head.next:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
                
            prev.next = head.next
        
        else:
            prev = prev.next
        
        head = head.next
    
    return dummy.next
        
            
    


    
# head = remove_duplicates_II(h)    
# print_ll(head)





# h1 = Node(1)
# h1.next = Node(7)
# h1.next.next = Node(12)
# h1.next.next.next = Node(16)
# h1.next.next.next.next = Node(20)
# h1.next.next.next.next.next = Node(24)
# h2 = Node(2)
# h2.next = Node(6)
# h2.next.next = Node(10)
# h2.next.next.next = Node(14)
# h2.next.next.next.next = Node(36)
# h1 = Node(6)
# h1.next = Node(5)
# h1.next.next = Node(0)
# h1.next.next.next = Node(2)
# h1.next.next.next.next = Node(12)
# h1.next.next.next.next.next = Node(7)
# h = sort_list(h1)
# print_ll(h)


def clone_list(head):
    Head = Node(head.val)
    h = Head
    
    while head.next:
        Head.next = Node(head.next.val)
        Head = Head.next
        head = head.next
    
    return h

lst = [1, 2, 3]
head = Node(lst[0])
h = head
for e in lst[1:]:
    head.next = Node(e)
    head = head.next

# clone_head = clone_list(h)
# print_ll(clone_head)

# if clone_head != h and clone_head.next != h.next and clone_head.next != h.next:
#     print("List cloned.")

# temp = clone_head.next
# clone_head.next = Node(100)
# clone_head.next.next = temp
# print_ll(clone_head)
# print()
# print_ll(h)


class RandomNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.rnd = None

def print_random_pointer_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        print(None, end=" ") if curr.next == None else print(curr.next.data, end=" ") 
        print(curr.rnd.data, end=" ")
        curr = curr.next
    
    print()
    

lst = [1, 2, 3, 4, 5]
head = RandomNode(lst[0])
h = head
for e in lst[1:]:
    head.next = RandomNode(e)
    head = head.next
    
h.rnd = h.next.next
h.next.rnd = h
h.next.next.rnd = h.next.next.next.next
h.next.next.next.rnd = h.next.next
h.next.next.next.next.rnd = h.next

print_random_pointer_list(h)

def copy_list(head):
    d = {None : None}
    
    curr = head
    while curr:
        d[curr] = RandomNode(curr.val)
        curr = curr.next
    
    curr = head
    while curr:
        d[curr].next = d[curr.next]
        d[curr].rnd = d[curr.rnd]
        curr = curr.next
    
    return d[head]  

# d = copy_list(h)
# print(d)


def clone_list_with_random_pointer(head):
    
    curr = head
    while curr:
        temp = curr.next
        curr.next = RandomNode(curr.data)
        curr.next.next = temp
        curr = curr.next.next
    
    curr = head
    while curr:
        curr.next.rnd = None if curr.rnd == None else curr.rnd.next
        curr = curr.next.next
    
    h2 = head.next
    clone = h2
    curr = head
    while curr:
        curr.next = curr.next.next
        clone.next = None if clone.next == None else clone.next.next
        curr = curr.next
        clone = clone.next
    
    return h2

cloned_head = clone_list_with_random_pointer(h)

# print("List cloned!") if cloned_head != h else print("Error")
# print_random_pointer_list(cloned_head)


class LRUCache:
    
    def __init__(self, n) -> None:
        self.capacity = n
        self.cache = OrderedDict()
    
    def get(self, key):
        pass
    
    def put(self, key, value):
        pass



def next_greater_element_II(nums):  
    stack = []
    ng = [None] * len(nums)
    
    for i in range(len(nums)-2, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        
        stack.append(nums[i])
    
    
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        
        ng[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i])
    
    return ng

arr = [3, 8, 4, 1, 2]
print(next_greater_element_II(arr))
    
    
    
    
    

    
    
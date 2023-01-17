class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def printll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next

def insert_at_begin(head, x):
    temp = Node(x)
    temp.next = head 
    return temp 

def insert_at_end(head, x):
    curr = head
    temp = Node(x)
    while curr.next != None:
        curr = curr.next
    curr.next = temp 
    return head 

def insert_at_pos(head, pos, x):
    temp = Node(x)
    
    if pos == 1:
        temp.next = head 
        return temp 
    
    curr = head 
    for _ in range(pos-2):
        curr = curr.next
        if curr == None:
            return head

   
    hold = curr.next
    curr.next = temp 
    temp.next = hold
    return head 

def delete_first_node(head):
    return head.next 

def delete_last_node(head):
    if head.next == None:
        return None 
    
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None 
    return head

def sorted_insert(head, x):
    temp = Node(x)
    if temp.data <= head.data:
        temp.next = head 
        return temp
    
    curr = head
    while curr.next != None:
        if curr.next.data <= x:
            curr = curr.next
        else:
            hold = curr.next
            curr.next = temp 
            temp.next = hold 
            return head 
    
    curr.next = temp 
    return head 

def print_middle_ll(head):
    fast, slow = head, head
    while fast != None and fast.next != None:
        fast = fast.next.next 
        slow = slow.next
    print(slow.data)
    return 

def len(head):
    cnt = 0
    curr = head
    while curr != None:
        cnt += 1 
        curr = curr.next
    return cnt

def nth_node_from_end(head, n):
    l = len(head)
    
    if n > l:
        return None 
    
    curr = head
    for _ in range(l-n):
        curr = curr.next
    print(curr.data)
    return 

def reverse(head):
    if head.next == None:
        return head
    
    small_head = reverse(head.next)
    small_tail = head.next 
    small_tail.next = head
    head.next = None
    return small_head

def merge_two_sorted_ll(a, b):
    if b == None:
        return a 
    
    head, tail = None, None
    if a.data <= b.data:
        head = a 
        tail = b
        a = a.next
    else:
        head = b 
        tail = b
        b = b.next 
    
    while a != None and b != None:
        if a.data <= b.data:
            tail.next = a 
            tail = tail.next 
            a = a.next 
        else:
            tail.next = b 
            tail = tail.next 
            b = b.next 
    if a == None:
        tail.next = b
    else:
        tail.next = a
    
    return head

def is_palindrom(head):
    if head == None:
        return True
    
    slow, fast = head, head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next 
    
    rev = reverse(slow.next)
    
    curr = head 
    while rev != None:
        if rev.data != curr.data:
            return False
        curr = curr.next
        rev = rev.next
        
    return True

def intersection_point(h1, h2):
    l1 = len(h1)
    l2 = len(h2)
    
    if l2 > l1:
        print(h1.data)
        return  
    
    for _ in range(l1-l2):
        h1 = h1.next 
    
    while h1 is not None:
        if h1 == h2:
            print(h1.data)
            return 
        h1 = h1.next
        h2 = h2.next

def remove_duplicates_ll(head):
    curr = head 
    while curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next 
        else:
            curr = curr.next
            
    return head 

def detect_loop(head):
    fast, slow = head, head
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            print('yes')
            return 

    print('no')
    return 

def break_loop(head):
    fast, slow = head, head
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            break 
    
    if fast != slow:
        return 
    
    slow = head
    while slow.next != fast.next:
        slow = slow.next 
        fast = fast.next 
        
    fast.next = None 
    

def even_odd_segregate(head):
    es, ee, os, oe = None, None, None, None
    curr = head
    while curr != None:
        x = curr.data 
        if x % 2 == 0:
            if es == None:
                es = curr 
                ee = es 
            else:
                ee.next = curr
                ee = ee.next
        else:
            if os == None:
                os = curr 
                oe = os 
            else:
                oe.next = curr
                oe = oe.next
        curr = curr.next
    
    if es == None or os == None:
        return head 
    ee.next = os 
    oe.next = None
    return es

def reverse_first_k_elements(head, k):
    l = len(head)
    if k > l:
        return
    
    curr = head 
    prev, nxt = None, None
    for _ in range(k):
        nxt = curr.next
        curr.next = prev 
        prev = curr
        curr = nxt 
        
    head.next = curr
    return prev

def reverse_in_group_k(head, k):
    cnt = 0
    curr = head
    prev, nxt = None, None 
    while curr != None and cnt < k :
        nxt = curr.next
        curr.next = prev 
        prev = curr
        curr = nxt
        cnt += 1
    
    if nxt != None:
        rev = reverse_in_group_k(curr, k)
        head.next = rev 
    return prev

def pairwise_swap(head):
    if head == None and head.next == None:
        return head 
    
    curr = head.next.next
    prev = head
    head = head.next 
    head.next = prev 
    while curr != None and curr.next != None:
        prev.next = curr.next
        nxt = curr.next.next
        curr.next.next = curr 
        prev = curr
        curr = nxt
            
    prev.next = curr
    
    return head

class CircularLinkedList:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def print_cll(head):
    if head == None:
        return 
        
    curr = head
    print(curr.data, end=" ")
        
    curr = curr.next 
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


def insert_at_begin_cll(head, x):
    temp = CircularLinkedList(x)
    if head == None:
        temp.next = temp
        return temp
        
    curr = head 
    while curr.next != head:
        curr = curr.next
        
    hold = curr.next
    curr.next = temp
    temp.next = head
    return temp 
# h = Node(2)
# h.next = Node(4)
# print(h.data)
# print(h.next)
# print(h.next.data)
# print(h.next.next) 
h = None
H = insert_at_begin_cll(h, 2)
print(H)
print(H.next)
print_cll(H)
print(H.next.data)
        
# h1 = Node(17)
# h1.next = Node(15)
# h1.next.next = Node(8)
# h1.next.next.next = Node(12)
# h1.next.next.next.next = Node(5)
# h1.next.next.next.next.next = Node(24)
# h1 = Node(1)
# h1.next = Node(7)
# h1.next.next = Node(6)
# h1.next.next.next = Node(9)
# h1.next.next.next.next = Node(12)
# # h1.next.next.next.next.next = Node(2)
# h = pairwise_swap(h1)
# printll(h)





# h1 = Node(5)
# h1.next = Node(10)
# h1.next.next = Node(10)
# h1.next.next.next = Node(20)
# h1.next.next.next.next = Node(20)
# h1.next.next.next.next.next = Node(20)
# h1.next.next.next.next.next.next = h1.next.next.next.next

# break_loop(h1)
# printll(h1)

# detect_loop(h1)

# h2 = Node(2)
# h2.next = h1.next.next.next.next.next
# intersection_point(h1, h2)

# h = remove_duplicates_ll(h1)
# printll(h)





# h1 = Node('R')
# h1.next = Node('A')
# h1.next.next = Node('D')
# h1.next.next.next = Node('A')
# h1.next.next.next.next = Node('R')
# print(is_palindrom(h1))

# h2 = None

# h2 = Node(5)
# h2.next = Node(15)
# h2.next.next = Node(17)
# h2.next.next.next = Node(18)
# h2.next.next.next.next = Node(35)

# h = merge_two_sorted_ll(h1, h2)

# h = insert_at_begin(head, 2)
# h = insert_at_end(head, 5)
# h = insert_at_pos(head, pos=5, x=-1)
# h = delete_last_node(head)
# h = sorted_insert(head, 35)
# print_middle_ll(head)
# nth_node_from_end(head, 5)
# h = reverse(head)


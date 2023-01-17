class SinglyLinkedList:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
    
    def printLL(self):
        curr = self 
        while curr is not None:
            print(curr.data, end = ' ')
            curr = curr.next
        print()
    
    def search(self, x):
        cnt = 1
        curr = self 
        while curr is not None:
            if curr.data == x:
                return cnt
            else:
                cnt += 1
                curr = curr.next 
        return -1
    
    def insert_at_beginning(self, key):
        temp = SinglyLinkedList(key)
        temp.next = self
        return temp 
    
    def insert_at_end(self, key):
        temp = SinglyLinkedList(key)

        if self is None:
            return temp 

        curr = self

        while curr.next is not None:
            curr = curr.next 
        
        curr.next = temp 
        return self 
    
    def insert_at_POS(self, key, pos):
        curr = self
        temp = SinglyLinkedList(key)

        if pos == 1:
            temp.next = self
            return temp 

        for _ in range(pos-2):
            curr = curr.next 
            if curr is None:
                return self 
        
        temp.next = curr.next
        curr.next = temp 
        return self 

    def del_first_node(self):
        if self is None:
            return None
        
        return self.next 
    
    def del_last_node(self):
        if self is None:
            return None 
        
        if self.next is None:
            return None 

        curr = self

        while curr.next.next is not None:
            curr = curr.next
        
        curr.next = None
        return self 
    
    def sorted_insert(self, x):
        temp = SinglyLinkedList(x)

        if self is None:
            return temp
        
        if self.data > x :
            temp.next = curr
            return temp
        
        else:
            curr = self 
            while curr.next is not None and curr.next.data <= x:
                curr = curr.next 
            temp.next = curr.next
            curr.next = temp 
            return self 
        
    def reverse(self):
        curr = self
        prev = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        
        return prev 
    
    def reverse_recursively(self):
        if self is None:
            return None
        if self.next is None:
            return self 
        
        rest_head = self.next.reverse_recursively()
        rest_tail = self.next 
        rest_tail.next = self 
        self.next = None 
        return rest_head 
    
    def reverse_naive(self):
        stack = []

        curr = self 
        while curr is not None:
            stack.append(curr.data)
            curr = curr.next
        
        curr = self 
        while curr is not None:
            curr.data = stack.pop()
            curr = curr.next 
        
        return self 
    
    def reverse_first_k_elements(self, k):
        curr = self 
        prev = None 
        count = 0
        while curr is not None and count < k:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
            count += 1
        
        self.next = curr 
        return prev 
    
    def reverse_group_of_k(self, k):

        if self.next is None or self is None:
            return self 

        curr = self 
        prev, nxt = None, None 
        count = 0
        while curr is not None and count < k:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
            count += 1

        if nxt is not None:
            rem_head = curr.reverse_group_of_k(k)
            self.next = rem_head
        return prev 
    
    def segregate_even_odd(self):
        es, ee, os, oe = None, None, None, None 
        curr = self 
        while curr is not None :
            x = curr.data 
            if x % 2 == 0:
                if es is None:
                    es = curr 
                    ee = es 
                else:
                    ee.next = curr 
                    ee = ee.next 
            else:
                if os is None:
                    os = curr 
                    oe = os 
                else:
                    oe.next = curr 
                    oe = oe.next 
            curr = curr.next 
        
        if es is None or os is None:
            return self 
        
        ee.next = os 
        oe.next = None 
        return es 
    
    def pairwise_swap_naive(self):
        curr = self 
        while curr is not None and curr.next is not None:
            curr.data, curr.next.data = curr.next.data, curr.data
            curr = curr.next.next  
        return self 
    
    def pairwise_swap(self):
        if self is None or self.next is None:
            return self 
        
        curr = self.next.next 
        prev = self 
        self = self.next 
        self.next = prev 

        while curr is not None and curr.next is not None:
            prev.next = curr.next 
            prev = curr 
            nxt = curr.next.next 
            curr.next.next = curr 
            curr = nxt 

        prev.next = curr 
        
        return self 
    
    def find_nth_node_from_end(self, n):
        curr = self
        l = 0
        while curr is not None:
            curr = curr.next 
            l += 1
        if n > l:
            return None 
        curr = self 
        for _ in range(1, l-n+1):
            curr = curr.next 
        print(curr.data)
    
    def merge_two_sorted_linkedlist(self, other):
        if self is None:
            return other  
        if other is None:
            return self 
        
        head, tail = None, None
        if self.data <= other.data:
            head = tail = self 
            self = self.next 
        else:
            head = tail = other 
            other = other.next 
        
        while self is not None and other is not None:
            if self.data <= other.data:
                tail.next = self 
                tail = tail.next
                self = self.next 
            else:
                tail.next = other 
                tail = tail.next 
                other = other.next 
                
        if self is None:
            tail.next = other 
        else:
            tail.next = self 
            
        return head
    
    def palindrom_naive(self):
        stack = []
        curr = self 
        while curr is not None:
            stack.append(curr.data)
            curr = curr.next 
        
        curr = self 
        while curr is not None:
            if stack.pop().lower() != curr.data.lower():
                return False 
            curr = curr.next
        return True 
    
    def middle_ele_naive(self):
        if self is None:
            return 
        if self.next is None:
            print(self.data)
            return 
        curr = self 
        cnt = 0 
        while curr:
            cnt += 1 
            curr = curr.next
        
        curr = self
        for _ in range(cnt // 2):
            curr = curr.next 
        print(curr.data)
        return 
    
    def middle_element(self):
        if self is None:
            return 
        
        fast = self 
        slow = self 
        while fast != None and fast.next != None:
            fast = fast.next.next 
            slow = slow.next
        print(slow.data)
        return 
    
    def is_palindrom(self):
        if self is None:
            return True 
        
        fast, slow = self, self 
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next 
            slow = slow.next
            
        rev = slow.next.reverse()
        curr = self
        while rev is not None:
            if rev.data != curr.data:
                return False 
            curr = curr.next
            rev = rev.next
        return True
    
    def length(self):
        curr = self
        cnt = 0 
        while curr is not None:
            cnt += 1 
            curr = curr.next
        return cnt 
    
    def intersection_point(self, other):
        cnt1 = self.length()
        cnt2 = other.length()
        
        if cnt2 > cnt1:
            return self.data 
        
        curr1 = self
        for _ in range(cnt1 - cnt2):
            if curr1 == None:
                return -1
            curr1 = curr1.next
            
        curr2 = other 
        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1.data
            curr1 = curr1.next 
            curr2 = curr2.next 
        return -1
    
    def remove_duplicates_from_sorted_ll(self):
        curr = self 
        while curr != None and curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        
        
    
    # def pairwise_swap_recursion_soln(self):
    #     if self is None or self.next is None:
    #         return self 
        
    #     temp = self.next 
    #     self.next = temp.next.pairwise_swap_recursion_soln()
    #     temp.next = self
    #     return temp 

def del_with_given_pointer(head, pointer):
    temp = pointer.next
    pointer.data = temp.data 
    pointer.next = temp.next 
    return head 

def intersection_point(h1, h2):
    s = set()
    curr = h1
    while curr is not None:
        s.add(curr)
        curr = curr.next 
    curr = h2 
    while curr is not None:
        if curr in s:
            return curr.data 
        curr = curr.next 
    return -1 

def is_loop(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next 
        slow = slow.next 
        if fast == slow:
            return True 
    return False

def break_loop(head):
    fast, slow = head, head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break 
        
    if fast != slow:
        return 
    
    slow = head 
    while slow.next != fast.next:
        slow = slow.next 
        fast = fast.next 
    fast.next = None 

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next 
    
# head = SinglyLinkedList(10)
# # head.next = SinglyLinkedList(20)
# # head.next.next = SinglyLinkedList(30)
# # head.next.next.next = SinglyLinkedList(40)
# # head.next.next.next.next = SinglyLinkedList(60)
# # head.next.next.next.next.next = head.next
# head.next = head
# print(is_loop(head))
# break_loop(head)
# print_linked_list(head)

            
            

# head = SinglyLinkedList(10)
# head.next = SinglyLinkedList(15)
# head.next.next = SinglyLinkedList(20)
# head.next.next.next = SinglyLinkedList(25)
# head.next.next.next.next = SinglyLinkedList(28)

# h = head.reverse_group_of_k(3)

# head.remove_duplicates_from_sorted_ll()

# h1 = SinglyLinkedList(5)
# h1.next = SinglyLinkedList(8)
# h1.next.next = SinglyLinkedList(7)
# h1.next.next.next = SinglyLinkedList(10)
# h1.next.next.next.next = SinglyLinkedList(12)
# h1.next.next.next.next.next = SinglyLinkedList(15)
# h2 = SinglyLinkedList(9)
# h2.next = h1.next.next.next.next.next 
# h2.printLL()
# h1.printLL()
# print(intersection_point(h1, h2))
# print(h1.intersection_point(h2))
# print(h1.length())
# print(h2.length())



# head = SinglyLinkedList(10)
# head.next = SinglyLinkedList(20)
# head.next.next = SinglyLinkedList(30)
# head.next.next.next = SinglyLinkedList(40)
# head1 = SinglyLinkedList(5)
# head1.next = SinglyLinkedList(15)
# head1.next.next = SinglyLinkedList(17)
# head1.next.next.next = SinglyLinkedList(18)
# head1.next.next.next.next = SinglyLinkedList(35)
# h = head.merge_two_sorted_linkedlist(head1)
# head = SinglyLinkedList('R')
# head.next = SinglyLinkedList('A')
# head.next.next = SinglyLinkedList('D')
# head.next.next.next = SinglyLinkedList('A')
# head.next.next.next.next = SinglyLinkedList('R')
# # print(head.palindrom_naive())
# # # head.middle_element()
# print(head.is_palindrom())
# h.printLL()
# head = SinglyLinkedList(17)
# head.next = SinglyLinkedList(15)
# head.next.next = SinglyLinkedList(8)
# head.next.next.next = SinglyLinkedList(12)
# head.next.next.next.next = SinglyLinkedList(5)
# head.next.next.next.next.next = SinglyLinkedList(7)
# head.next.next.next.next.next.next = SinglyLinkedList(16)
# head.next.next.next.next.next.next.next = SinglyLinkedList(120)
# h = head.insert_at_beginning(0)
# h = head.sorted_insert(80)
# if h is not None:
#     h.printLL()
# else:
#     print(h)
# head.find_nth_node_from_end(6)
# h.printLL()
# h = del_with_given_pointer(head, head.next.next.next.next.next.next)
# h.printLL()
        

lst = [1, 2, 3, 4, 5, 6]
head = SinglyLinkedList(lst[0])
h = head
for e in lst[1:]:
    head.next = SinglyLinkedList(e)
    head = head.next

h.printLL()
print(id(h))
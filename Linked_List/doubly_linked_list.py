# from audioop import reverse


class DoublyLinkedList:
    
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
    def print_dll(self):
        curr = self
        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
    
    def insert_at_begin(self, x):
        temp = DoublyLinkedList(x)
        if self != None:
            self.prev = temp
            
        temp.next = self 
        return temp
    
    def insert_at_end(self, x):
        temp = DoublyLinkedList(x)
        if self == None:
            temp.next = self
            return temp
        
        curr = self
        while curr.next != None:
            curr = curr.next
        
        curr.next = temp
        temp.prev = curr
        return self
    
    def delete_head(self):
        if self.next == None:
            return None
        
        curr = self.next 
        curr.prev = None
        return curr
    
    def delete_last_node(self):
        if self.next is None:
            return None
        
        curr = self
        while curr.next.next != None:
            curr = curr.next
        
        curr.next = None 
        return self
    
    def reverse(self):
        if self.next == None:
            return self 
        
        small_head = self.next.reverse()
        small_tail = self.next
        small_tail.next = self
        self.prev = small_tail
        self.next = None
        return small_head


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()
    

def printList(node):
    temp = node
    print ("Forward Traversal using next pointer")
    while(node is not None):
        print (node.data,end=" ")
        temp = node
        node = node.next
    print ("\nBackward Traversal using prev pointer")
    while(temp):
        print (temp.data,end=" ")
        temp = temp.prev
    print()
            

head = Node(20)
n1 = Node(5)
n2 = Node(9)
head.next = n1
n1.prev = head
n1.next = n2
n2.prev = n1
# h = head.insert_at_begin(10)
# h1 = h.insert_at_begin(15)
# h2 = h1.insert_at_begin(12)
# h3 = h2.insert_at_begin(16)
# h = head.insert_at_end(1)
# h1 = h.insert_at_end(7)
# h2 = h1.insert_at_end(13)
# h = head.delete_last_node()
# h = head.reverse()

# h.print_dll()

# head = DoublyLinkedList(2)
# head.next = DoublyLinkedList(5)
# head.next.prev = head
# head.next.next = DoublyLinkedList(9)
# head.next.next.prev = head.next

def merge(h1, h2):
    
    if h1 == None:
        return h2
    
    if h2 == None:
        return h1
        
    head, tail = None, None
    if h1.data <= h2.data:
        head = h1
        tail = h1
        h1 = h1.next
    else:
        head = h2
        tail = h2
        h2 = h2.next
    
    while h1 and h2:
        if h1.data <= h2.data:
            tail.next = h1
            tail.prev = tail
            tail = tail.next
            h1 = h1.next
        else:
            tail.next = h2
            tail.prev = tail
            tail = tail.next
            h2 = h2.next
    
    if h1:
        tail.next = h1
    else:
        tail.next = h2
    
    return head

def reverse(head):
    if head.next == None:
        return head
    
    sm_head = reverse(head.next)
    sm_tail = head.next
    sm_tail.next = head
    head.prev = sm_tail
    head.next = None
    
    return sm_head
            
#Function to sort the given doubly linked list using Merge Sort.
def sortDoubly(head):
    if head == None or head.next == None:
        return head
    
    previous = None
    fast, slow = head, head
    
    while fast and fast.next:
        previous = slow
        slow = slow.next
        fast = fast.next.next
    
    slow.prev = None
    previous.next = None
    
    ll1 = sortDoubly(head)
    ll2 = sortDoubly(slow)
    
    sorted_list = merge(ll1, ll2)
    
    return sorted_list

sorted = sortDoubly(head)
rev = reverse(sorted)

printList(sorted)
PrintLinkedList(rev)

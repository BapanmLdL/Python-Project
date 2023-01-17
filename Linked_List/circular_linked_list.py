class CircularLinkedList:
    
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
    
    def print_cll(self):
        if self == None:
            return 
        
        curr = self
        print(curr.data, end=" ")
        
        curr = curr.next 
        while curr != self:
            print(curr.data, end=" ")
            curr = curr.next
    
    def insert_at_begin(self, x):
        temp = CircularLinkedList(x)
        if self == None:
            temp.next = temp
            return temp
        
        curr = self 
        while curr.next != self:
            curr = curr.next
        
        # hold = curr.next
        curr.next = temp
        temp.next = self
        return temp 
    
    def insert_at_end(self, x):
        temp = CircularLinkedList(x)
        
        curr = self
        while curr.next != self:
            curr = curr.next
        
        # hold = curr.next
        curr.next = temp 
        temp.next = self 
        return self
    
    def delete_head(self):
        if self.next == self:
            return 
        
        curr = self
        while curr.next != self:
            curr = curr.next
        curr.next = curr.next.next
        curr = curr.next
        return curr
    
    def delete_kth_node(self, k):
        if self == None:
            return self
        
        if k == 1:
            return self.delete_head()
        else:
            curr = self
            for _ in range(k-2):
                curr = curr.next
            
            curr.next = curr.next.next
            return self
        
    

        
h1 = CircularLinkedList(17)
h1.next = CircularLinkedList(15)
h1.next.next = CircularLinkedList(8)
h1.next.next.next = CircularLinkedList(12)
h1.next.next.next.next = CircularLinkedList(5)
h1.next.next.next.next.next = CircularLinkedList(24)
h1.next.next.next.next.next.next = h1
# h1.next = h1
# h1 = None
h = h1.delete_kth_node(1)

h.print_cll()

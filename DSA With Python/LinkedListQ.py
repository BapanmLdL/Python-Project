class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

def NthNodeBegin(head, N):
    curr = head
    for i in range(N-1):
        curr = curr.next
    return curr.value

def NthNodeEnd(head, N):
    c = 1
    curr = head
    while curr.next != None:
        c += 1
        curr = curr.next
    if N > c:
        return -1
    else:
        curr = head
        while c > N:
            curr = curr.next
            c -= 1
        return curr.value

def areIdentical(h1, h2):
    curr1 = h1
    c1 = 1
    while curr1.next != None:
        c1 += 1
        curr1 = curr1.next
    curr2 = h2
    c2 = 1
    while curr2.next != None:
        c2 += 1
        curr2 = curr2.next
    if c1 != c2:
        return False
    else:
        curr1 = h1
        curr2 = h2
        while curr1 is not None:
            if curr1.value != curr2.value:
                return False
            curr2 = curr2.next
            curr1 = curr1.next
        return True
def removeDuplicates(head):
    if (head == None) or (head.next == None):
        return head
    curr = head
    nxt = head.next
    while nxt is not None:
        if curr.value != nxt.value:
            curr = curr.next
            nxt = nxt.next
        elif curr.value == nxt.value:
            temp = nxt.next
            curr.next = temp
            nxt = temp
    return head
def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.value, end = " ")
        curr = curr.next

def joinTheLists(head1, head2):
    curr = head1
    while curr.next is not None:
        curr = curr.next
    curr.next = head2
    curr = curr.next
    while curr.next is not None:
        curr = curr.next
    return head1
def isSorted(head):
    prev = head
    curr = prev.next
    nxt = curr.next
    while nxt is not None:
        if (prev.value >= curr.value) and (curr.value >= nxt.value):
            prev = curr
            curr = nxt
            nxt = nxt.next
        elif (prev.value <= curr.value) and (curr.value <= nxt.value):
            prev = curr
            curr = nxt
            nxt = nxt.next
        else:
            return 0
    return 1
def IsSorted(head):
   #code here
   cur = head
   inc = 1
   dec = 1
   while cur.next !=  None:
       if cur.next.value > cur.value:
           dec = 0
       if cur.next.value < cur.value:
           inc = 0
       cur = cur.next
   return inc or dec
def deleteAtPosition(head, pos=None):
    if pos == 1:
        return head.next
    curr = head
    c = 1
    while curr is not None:
        if c == (pos-1):
            curr.next = curr.next.next
            curr = curr.next
            c += 1
        else:
            c += 1
            curr = curr.next
    return head
def deleteHead(head):
    if head == None:
        return None
    temp = head.next
    head.next = None
    head = temp
    return head
def deleteTail(head):
    if (head == None) or (head.next == None):
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head
def insertInSorted(head,data):
    temp = Node(data)
    if head == None:
        return temp
    elif data < head.value:
        temp.next = head
        return temp
    else:
        curr = head
        while (curr.next is not None) and (curr.next.value < data):
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head
def insertAtPosition(head,pos=None,data=None):
    n = 1
    dummy = head
    while dummy.next is not None:
        n += 1
        dummy = dummy.next
    if pos > n:
        return head
    c = 1
    curr = head
    temp = Node(data)
    while curr is not None:
        if c == pos:
            temp.next = curr.next
            curr.next = temp
            return head
        else:
            c += 1
            curr = curr.next

def insertInMid(head,node=None):
    n = 1
    dummy = head
    while dummy.next is not None:
        n += 1
        dummy = dummy.next
    temp = Node(node)
    if n % 2 == 0:
        c = 1
        curr = head
        while curr is not None:
            if c == n//2:
                temp.next = curr.next
                curr.next = temp
                return head
            else:
                c += 1
                curr = curr.next
    else:
        c = 1
        curr = head
        while curr is not None:
            if c == n//2 + 1:
                temp.next = curr.next
                curr.next = temp
                return head
            else:
                c += 1
                curr = curr.next
def insertAtBegining(head,x):
    temp = Node(x)
    temp.next = head
    return temp
def insertAtEnd(head,x):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = temp
    curr = curr.next
    return head
# head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(40)
head.next.next.next = Node(50)
head.next.next.next.next = Node(99)
head.next.next.next.next.next = Node(100)
# head2 = Node(1)
# head2.next = Node(4)
# head2.next.next = Node(6)
# head2.next.next.next = Node(9)
# head2.next.next.next.next = Node(10)
# head2.next.next.next.next.next = Node(16)
# print(removeDuplicates(head))
# out = removeDuplicates(head)
out = insertAtEnd(head,0)
PrintLinkedList(out)
# print(IsSorted(head))
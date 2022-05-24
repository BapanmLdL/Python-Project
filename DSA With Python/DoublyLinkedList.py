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
def insert_beginning(head, x=None):
    temp = Node(x)
    if head == None:
        temp.next = head
        return temp
    temp.next = head
    head.prev = temp
    return temp
def insert_End(head, x=None):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head
def DeleteHeadDLL(head):
    if head == None:
        return None
    elif head.next == None:
        return head.next
    else:
        head = head.next
        head.prev = None
        return head
def DelLastNodeDLL(head):
    if (head == None) or (head.next == None):
        return None
    else:
        curr = head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        return head
def ReverseDDL(head):
    if head == None:
        return None
    if head.next == None:
        return head
    curr = head
    prev = None
    while curr is not None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev
def addNode(head, p=None, data=None):
    temp = Node(data)
    curr = head
    for _ in range(p):
        curr = curr.next
    temp2 = curr.next
    curr.next = temp
    temp.prev = curr
    temp.next = temp2
    return head
def sortedInsert(head, x=None):
    temp = Node(x)
    curr = head
    if head == None:
        temp.next = None
        return temp
    elif x <= curr.data:
        temp.next = curr
        curr.prev = temp
        return temp
    else:
        while (curr.next is not None) and (curr.next.data <= x):
            curr = curr.next
        temp2 = curr.next
        curr.next = temp
        temp.prev = curr
        temp.next = temp2
        return head
def deleteNode(head, x=None):
    if (head == None) or (head.next == None):
        return None
    if x == 1:
        head = head.next
        head.prev = None
        return head
    curr = head
    for _ in range(x-2):
        curr = curr.next
    temp = curr
    curr.next = curr.next.next
    curr.prev = temp
    curr = curr.next
    return head
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
# head = None
# head = insert_End(head, x=1)
# head = insert_End(head, x=5)
# head = insert_End(head, x=2)
# head = insert_End(head, x=9)
# head = insert_End(head, x=78)
# head = insert_End(head, x=78)
PrintLinkedList(head)
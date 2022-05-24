class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printCircular(head):
    if head == None:
        return
    print(head.data, end = " ")
    curr = head.next
    while curr is not head:
        print(curr.data, end = " ")
        curr = curr.next

def getLength(head):
    c = 2
    curr = head.next
    while curr.next is not head:
        c += 1
        curr = curr.next
    return c
def isCircular(head):
    curr = head.next
    if curr is None:
        return 0
    if head == None:
        return 1
    while curr:
        if curr.next == head:
            return 1
        elif curr.next is None:
            return 0
        else:
            curr = curr.next
def insertInHead(head,x=None):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    if head.next == head:
        temp.next = head
        head.next = temp
        return temp
    temp2 = head.next
    head.next = temp
    temp.next = temp2
    head.data, temp.data = temp.data, head.data
    return head
def insertAtPosition(head,pos=None,data=None):
    temp = Node(data)
    curr = head
    for _ in range(pos-1):
        curr = curr.next
        if curr == head:
            return head
    temp2 = curr.next
    curr.next = temp
    temp.next = temp2
    return head
def deleteTail(head):
    if (head == None) or (head.next == head):
        return None
    curr = head
    while curr.next.next is not head:
        curr = curr.next
    curr.next = head
    return head
# head = None
head = Node(10)
# head.next = head
head.next = Node(15)
# head.next.next = head
head.next.next = Node(20)
head.next.next.next = Node(50)
head.next.next.next.next = Node(99)
head.next.next.next.next.next = Node(100)
head.next.next.next.next.next.next = head
out = deleteTail(head)
printCircular(out)

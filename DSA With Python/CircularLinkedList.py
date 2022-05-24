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
def InsertBeginningLinearT(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next is not head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp
def InsertBeginningConstantT(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data
        return head
def InsertEndLinearT(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next is not head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return head
def InsertEndConstantT(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data
        return temp
def DeleteHead(head):
    if (head == None) or (head.next == head):
        return None
    curr = head
    while curr.next is not head:
        curr = curr.next
    temp = head.next
    curr.next = temp
    return curr.next
def DeleteHeadEfficientSoln(head):
    if (head == None) or (head.next == head):
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head
def DeleteKthNode(head, k=None):
    if head == None:
        return None
    if k == 1:
        if (head == None) or (head.next == head):
            return None
        else:
            head.data = head.next.data
            head.next = head.next.next
            return head
    else:
        curr = head
        for _ in range(k-2):
            curr = curr.next
        curr.next = curr.next.next
        curr = curr.next
        return head

# head = None
head = Node(10)
head.next = head
# head.next.next = head
# head.next.next = Node(40)
# head.next.next.next = Node(50)
# head.next.next.next.next = Node(99)
# head.next.next.next.next.next = Node(100)
# head.next.next.next.next.next.next = head
out = DeleteKthNode(head, k=1)
printCircular(out)
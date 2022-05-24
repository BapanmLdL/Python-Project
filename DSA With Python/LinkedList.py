import sys
import random
import math

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next
def SearchLL(head, x):
    pos = 1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# PrintLinkedList(head)
# print(SearchLL(head, 50))
def InsertBegin(head, key):
    temp = Node(key)
    temp.next = head
    return temp
# head = None
# head = InsertBegin(head, 5)
# head = InsertBegin(head, 10)
# head = InsertBegin(head, 20)
# head = InsertBegin(head, 30)
# head = InsertBegin(head, 40)
# print(InsertBegin(head, 5))
# PrintLinkedList(head)
def InsertEnd(head, key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head
# head = None
# head = InsertEnd(head, 5)
# head = InsertEnd(head, 10)
# head = InsertEnd(head, 20)
# head = InsertEnd(head, 30)
# head = InsertEnd(head, 40)
# # print(InsertBegin(head, 5))
# # PrintLinkedList(head)
def InsertPOS(head, data, pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for _ in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head
def DelFirstNode(head):
    if head == None:
        return None
    else:
        return head.next
def DelLastNode(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head


def SortedInsert(head, x):
    temp = Node(x)
    if head == None:
        return temp
    elif x <= head.key:
        temp.next = head
        return temp
    else:
        curr = head
        while (curr.next != None) and (curr.next.key <= x):
            curr = curr.next

        temp.next = curr.next
        curr.next = temp
        return head
def ReverseLinkedListNaiveSol(head):
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.key)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.key = stack.pop()
        curr = curr.next
    return head
def ReverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def ReverseRecursive(head):
    if head == None:
        return None
    if head.next == None:
        return head
    rest_head = ReverseRecursive(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head
def ReverseRecursive2(curr, prev=None):
    if curr == None:
        return prev
    nxt = curr.next
    curr.next = prev
    # prev = curr
    return ReverseRecursive2(nxt, curr)
# head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
# head = DelFirstNode(head)
# head = DelLastNode(head)
# SortedInsert(head, 25)
PrintLinkedList(ReverseRecursive2(head, prev=None))


from collections import deque
import math

class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
    return


def search(root, x):
    
    if root is None:
        return False
    
    if root.data == x:
        return True
    
    if x > root.data:
        return search(root.right, x)
    else:
        return search(root.left, x)


def insert(root, x):
    if root is None:
        return Node(x)
    
    if x == root.data:
        return root
    
    if x > root.data:
        root.right = insert(root.right, x)
    else:
        root.left = insert(root.left, x)
    
    return root


def insert_iteratively(root, x):
    parent = None
    curr = root
    
    while curr:
        parent = curr
        
        if x == curr.data:
            return root
        elif x > curr.data:
            curr = curr.right
        else:
            curr = curr.left
    
    if parent is None:
        return Node(x)
    
    if x > parent.data:
        parent.right = Node(x)
    else:
        parent.left = Node(x)
    
    return root


def getSucc(root):
    curr = root
    while curr.left:
        curr = curr.left
    
    return curr.data


def delNode(root, x):
    if root is None:
        return 
    
    if x == root.data:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = getSucc(root.right)
            root.data = succ
            root.right = delNode(root.right, succ)
    
    elif x > root.data:
        root.right = delNode(root.right, x)
    else:
        root.left = delNode(root.left, x)
    
    return root


def floorBST(root, x):
    res = None
    while root:
        if root.data == x:
            return [root, root.data]
        elif root.data > x:
            root = root.left
        else:
            res = root
            root = root.right
    
    return res if res == None else [res, res.data]


def ceilBST(root, x):
    res = None
    while root:
        if root.data == x:
            return [root, root.data]
        elif root.data < x:
            root = root.right
        else:
            res = root
            root = root.left
    
    return res if res == None else [res, res.data]


def leftCeil(arr):
    print(-1, end=" ")
    
    s = set()
    s.add(arr[0])
    
    for i in range(1, len(arr)):
        it = [x for x in s if x >= arr[i]]
        
        if len(it) == 0:
            print(-1, end=" ")
        else:
            print(min(it), end=" ")
        
        s.add(arr[i])
    
    return


def kthSmallestElement(root, k):
    
    def inOrder(root):
        return inOrder(root.left) + [root.data] + inOrder(root.right) if root else []
    
    return inOrder(root)[k-1]


root = Node(15)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.right.left = Node(18)
root.right.left.left = Node(16)
root.right.right = Node(80)

# print(search(root, 80))
# insert_iteratively(root, 2)
# print(inorder(root))
# delNode(root, 2)
# print()
# print(inorder(root))
# delNode(root, 100)
# print()
# print(inorder(root))
# print(floorBST(root, 4))
# print(ceilBST(root, 15.8))
# leftCeil([2, 8, 30, 15, 25, 12])
print(kthSmallestElement(root, 3))
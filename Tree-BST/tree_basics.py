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

def preorder(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def height(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return 0
    
    # height_left_subtree = height(root.left)
    # height_right_subtree = height(root.right)
    
    return max(height(root.left), height(root.right)) + 1


def level_order(root):
    if root == None:
        return None
    
    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        
        if node.left:
            q.append(node.left)
        
        if node.right:
            q.append(node.right)
    
    return

def size(root):
    if root == None:
        return 0
    
    left_size = size(root.left)
    right_size = size(root.right)
    
    return left_size + right_size + 1


def maximum(root):
    if root == None:
        return -math.inf
    
    max_left = maximum(root.left)
    max_right = maximum(root.right)
    
    return max(max_left, max_right, root.data)

def print_k_dist(root, k):
    if root == None:
        return 
    
    if k == 0:
        print(root.data, end=" ")
    else:
        print_k_dist(root.left, k-1)
        print_k_dist(root.right, k-1)
    
    return 

def level_order_naive(root):
    h = height(root)
    
    for k in range(h):
        print_k_dist(root, k)
    
    return


def iter_inorder(root):
    if root == None:
        return
    
    stack = []
    curr = root
    while curr:
        stack.append(curr)
        curr = curr.left
    
    while stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        curr = curr.right
        while curr:
            stack.append(curr)
            curr = curr.left
    
    return 

def iter_preorder(root):
    if root == None:
        return
    
    stack = [root]
    
    while stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    
    return


def preOrder(root):
    if root == None:
        return 
    
    stack = []
    curr = root
    while stack or curr:
        while curr:
            print(curr.data, end=" ")
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        if stack:
            curr = stack.pop()
    
    return
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.right = Node(100)
root.left.left.right.left = Node(200)
root.left.left.right.right = Node(300)
# root.right.left = Node(60)
# root.right.right = Node(80)

# inorder(root)
# print('\n')
# preorder(root)
# print('\n')
# postorder(root)
# print(height(root))
# level_order(root)
# print(size(root))
# print(maximum(root))
# print_k_dist(root, k=2)
# level_order_naive(root)
# inorder(root)
# iter_inorder(root)
# iter_preorder(root)
# preOrder(root)
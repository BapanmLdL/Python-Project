from collections import deque, OrderedDict


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


# class DLL:

#     def __init__(self, val) -> None:
#         self.val = val
#         self.prev = None
#         self.next = None


def print_ll(head):
    curr = head

    while curr:
        print(curr.data, end=" ")
        curr = curr.right

    return


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
    

def level_order_line1(root):
    if root == None:
        return

    q = deque()
    q.append(root)
    q.append(None)

    while len(q) > 1:
        curr = q.popleft()

        if curr == None:
            print()
            q.append(None)
            continue

        print(curr.data, end=" ")

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    return


def level_order_line2(root):
    if root == None:
        return

    q = deque()
    q.append(root)

    while q:
        no_nodes = len(q)
        for _ in range(no_nodes):
            curr = q.popleft()
            print(curr.data, end=" ")

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        print()

    return


def height(root):
    if root == None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def isHeightBalance_naive(root):
    if root == None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    return (
        abs(left_height - right_height) <= 1 and
        isHeightBalance_naive(root.left) and
        isHeightBalance_naive(root.right)
    )


def is_HeightBalance(root):
    if root == None:
        return 0

    left_height = is_HeightBalance(root.left)

    if left_height == -1:
        return -1

    right_height = is_HeightBalance(root.right)

    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_HeightBalance_main(root):
    if is_HeightBalance(root) == -1:
        return False

    return True


def vertical_traversal(root):
    mp = {}
    q = deque()

    q.append((root, 0))

    while q:
        curr = q[0][0]
        hd = q[0][1]
        q.popleft()

        if mp.get(hd) == None:
            mp[hd] = []

        mp[hd].append(curr.data)

        if curr.left:
            q.append((curr.left, hd-1))

        if curr.right:
            q.append((curr.right, hd+1))

    # sort the dict based on hirizontal distance
    sorted_map = OrderedDict(sorted(mp.items()))

    for values in sorted_map.values():
        for e in values:
            print(e, end=" ")
        print()

    return


def bottom_view(root):
    mp = {}
    q = deque()

    q.append((root, 0))

    while q:
        curr = q[0][0]
        hd = q[0][1]
        q.popleft()

        mp[hd] = curr.data

        if curr.left:
            q.append((curr.left, hd-1))

        if curr.right:
            q.append((curr.right, hd+1))

    for key in sorted(mp):
        print(mp[key], end=" ")

    return


def top_view(root):
    mp = {}
    q = deque()

    q.append((root, 0))

    while q:
        curr = q[0][0]
        hd = q[0][1]
        q.popleft()

        if mp.get(hd) == None:
            mp[hd] = curr.data

        if curr.left:
            q.append((curr.left, hd-1))

        if curr.right:
            q.append((curr.right, hd+1))

    for key in sorted(mp):
        print(mp[key], end=" ")

    return


def maximum_width(root):
    if root == None:
        return 0

    width = 0

    q = deque()
    q.append(root)

    while q:
        no_nodes = len(q)
        width = max(width, no_nodes)

        for _ in range(no_nodes):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    return width


head, prev = None, None


def convert_inorder(root):
    if root == None:
        return None

    convert_inorder(root.left)

    global prev, head

    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root

    prev = root

    convert_inorder(root.right)

    return head


# def convert_postorder(root):
#     if root == None:
#         return None

#     convert_postorder(root.left)

#     convert_postorder(root.right)

#     global prev, head

#     if prev == None:
#         head = root
#     else:
#         root.left = prev
#         prev.right = root

#     prev = root

#     return head

pre_indx = 0


def build_tree_simple(pre, io, isi, iei):
    if isi > iei:
        return None

    global pre_indx

    root = Node(pre[pre_indx])
    pre_indx += 1

    if isi == iei:
        return root

    for i in range(isi, iei+1):
        if io[i] == root.data:
            break

    root.left = build_tree_simple(pre, io, isi, i-1)
    root.right = build_tree_simple(pre, io, i+1, iei)

    return root


mp = {}
def build_map(io):
    global mp

    for i in range(len(io)):
        mp[io[i]] = i

    return


def build_tree(pre, io, isi, iei):
    if isi > iei:
        return None

    global pre_indx

    root = Node(pre[pre_indx])
    pre_indx += 1

    if isi == iei:
        return root

    i = mp.get(root.data)

    root.left = build_tree(pre, io, isi, i-1)
    root.right = build_tree(pre, io, i+1, iei)

    return root


def spiral_traversal(root):
    if root == None:
        return None
    
    q = deque()
    stack = []
    
    q.append(root)
    rev = False
    
    while q:
        no_nodes = len(q)
        
        for _ in range(no_nodes):
            curr = q.popleft()
            
            if rev:
                stack.append(curr.data)
            else: 
                print(curr.data, end=" ")
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        if rev:
            while stack:
                print(stack.pop(), end=" ")
            
        rev = not rev
    
    return 


def spiral_traverse_eff(root):
    if root == None:
        return None
    
    stack1 = []
    stack2 = []
    
    stack1.append(root)
    
    while stack1 or stack2:
        while stack1:
            curr = stack1.pop()
            print(curr.data, end=" ")
            
            if curr.left:
                stack2.append(curr.left)
            if curr.right:
                stack2.append(curr.right)
        
        while stack2:
            curr = stack2.pop()
            print(curr.data, end=" ")
            
            if curr.right:
                stack1.append(curr.right)
            if curr.left:
                stack1.append(curr.left)
                
    return 
                
            
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50)
# root.left.left.right = Node(100)
# root.left.left.right.left = Node(200)
# root.left.left.right.right = Node(300)

# root = Node(18)
# root.left = Node(4)
# root.right = Node(20)
# root.right.left = Node(13)
# root.right.right = Node(70)

root = Node(10)
root.left = Node(60)
root.right = Node(50)
root.left.right = Node(70)
root.left.right.right = Node(30)
root.left.right.right.right = Node(40)
root.right.left = Node(20)
root.right.left.right = Node(80)


# root = Node(10)
# root.left = Node(20)
# root.right = Node(50)
# root.left.left = Node(30)
# root.left.right = Node(40)
# root.right.left = Node(60)
# root.right.right = Node(70)


# level_order_line1(root)
# print(is_HeightBalance_main(root))
# vertical_traversal(root)
# print()
# # bottom_view(root)
# top_view(root)

# print(maximum_width(root))
# inorder(root)
# head = convert_inorder(root)
# print_ll(head)
# postorder(root)
# head = convert_postorder(root)
# print()

# io = [40, 20, 60, 50, 70, 10, 80, 100, 30]
# pre = [10, 20, 40, 50, 60, 70, 30, 80, 100]
# build_map(io)
# root = build_tree(pre, io, isi=0, iei=len(io)-1)
# preorder(root)

spiral_traversal(root)
print()
spiral_traverse_eff(root)
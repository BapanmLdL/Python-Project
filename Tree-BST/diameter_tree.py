from collections import deque, OrderedDict
import math


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


# class Height:
    
#     def __init__(self) -> None:
#         self.height =  0


def inorder(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
        

def height(root):
    # TC: Theta(n)
    # SC: Theta(height)
    if root == None:
        return 0
    
    # height_left_subtree = height(root.left)
    # height_right_subtree = height(root.right)
    
    return max(height(root.left), height(root.right)) + 1


def diameter_naive(root):
    if root == None:
        return 0
    
    d1 = 1 + height(root.left) + height(root.right)
    d2 = diameter_naive(root.left)
    d3 = diameter_naive(root.right)
    
    return max(d1, d2, d3)


mp = {}
def heights(root):
    if root == None:
        return 0
    
    lh = heights(root.left)
    rh = heights(root.right)
    
    global mp
    
    mp[root] = max(lh, rh) + 1
    
    return max(lh, rh) + 1


def diameter_better_soln(root):
    if root == None:
        return 0
    
    dia_root = 1 + mp.get(root.left, 0) + mp.get(root.right, 0)
    
    dia_left = diameter_better_soln(root.left)
    dia_right = diameter_better_soln(root.right)
    
    return max(dia_root, dia_left, dia_right)


# def diameterOpt(root, height):
#     lh = Height()
#     rh = Height()
    
#     if root == None:
#         height.h = 0
#         return 0
    
    
    
#     dia_left = diameterOpt(root.left, lh)
#     dia_right = diameterOpt(root.right, rh)
    
#     height.h = max(lh, rh) + 1
    
#     dia_root = 1 + lh + rh
    
#     return max(dia_root, dia_left, dia_right)
    
    

# def diameter(root):
#     height = Height()
#     return diameterOpt(root, height)


res = - math.inf
def diameter(root):
    if root == None:
        return 0
    
    lh = diameter(root.left)
    rh = diameter(root.right)
    
    global res
    
    res = max(res, (1 + lh + rh))
    
    return max(lh, rh) + 1



def find_Path(root, path, n):
    if root == None:
        return False
    
    path.append(root.data)
    
    if n == root.data:
        return True
    
    if (
        (root.left and find_Path(root.left, path, n)) or 
        (root.right and find_Path(root.right, path, n))
    ):
        return True
    
    path.pop()
    
    return False


def find_LCA(root, n1, n2):
    path1 = []
    path2 = []
    
    if (not find_Path(root, path1, n1)) or (not find_Path(root, path2, n2)):
        return -1
    
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        
        i += 1
    
    return path1[i-1]


def lca(root, n1, n2):
    if root == None:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    lca1 = lca(root.left, n1, n2)
    lca2 = lca(root.right, n1, n2)
    
    if lca1 and lca2:
        return root
    
    return lca1 if lca1 else lca2


class BurnTree:
    
    def create_parent_mapping(self, root, target, mp):
        
        res = None
        
        q = deque()
        q.append(root)
        
        mp[root] = None
        
        while q:
            front = q.popleft()
            
            if front.data == target:
                res = front
            
            
            if front.left:
                mp[front.left] = front
                q.append(front.left)
            
            if front.right:
                mp[front.right] = front
                q.append(front.right)
        
        return res
            
        
    
    def burn_tree(self, leaf, node_to_parent_map):
        
        visited = {}
        q = deque()
        
        q.append(leaf)
        visited[leaf] = True
        
        ans = 0
        
        while q:
            
            flag = False
            size = len(q)
            
            for i in range(size):
                
                
                front = q.popleft()
                
                if front.left and not visited.get(front.left):
                    flag = True
                    visited[front.left] = True
                    q.append(front.left)
                
                if front.right and not visited.get(front.right):
                    flag = True
                    visited[front.right] = True
                    q.append(front.right)
                
                if node_to_parent_map.get(front) and not visited.get(node_to_parent_map[front]):
                    flag = True
                    visited[node_to_parent_map[front]] = True
                    q.append(node_to_parent_map[front])
            
            if flag:
                ans += 1
        
        return ans
        
        
    
    def minTime(self, root, target):
        
        node_to_parent_map = {}
        
        point_to_leaf = self.create_parent_mapping(root, target, node_to_parent_map)
        
        return self.burn_tree(point_to_leaf, node_to_parent_map)


def countNode(root):
    
    lh, rh = 0, 0
    
    curr = root
    
    while curr:
        lh += 1
        curr = curr.left
    
    curr = root 
    
    while curr:
        rh += 1
        curr = curr.right
    
    if lh == rh:
        return (1 << lh) - 1
    
    return 1 + countNode(root.left) + countNode(root.right)


#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    if root == None:
        A.append(-1)
        return
    
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)
    
#Function to deserialize a list and construct the tree.   

indx = 0

def deSerialize(A):
    global indx
    
    if indx == len(A):
        return None
        
    val = A[indx]
    indx += 1
    
    if val == -1:
        return None
    
    root = Node(val)
    
    root.left = deSerialize(A)
    root.right = deSerialize(A)
    
    return root





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

# root = Node(10)
# root.left = Node(60)
# root.right = Node(50)
# root.left.right = Node(70)
# root.left.right.right = Node(30)
# root.left.right.right.right = Node(40)
# root.right.left = Node(20)
# root.right.left.right = Node(80)


# root = Node(10)
# root.left = Node(20)
# root.right = Node(50)
# root.left.left = Node(30)
# root.left.right = Node(40)
# root.right.left = Node(60)
# root.right.right = Node(70)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.left.left = Node(60)
root.right.right = Node(50)
root.right.right.left = Node(70)
root.right.right.right = Node(80)


# dia = diameter_naive(root)
# print(dia)

# h = heights(root)
# dia = diameter_better_soln(root)
# d  = diameter_naive(root)
# print(dia == d)

# dia = diameter(root)
# print(dia)

# lca_node = lca(root, n1=60, n2=70)
# print(lca_node.data)

arr = []
serialize(root, arr)
r = deSerialize(arr)
inorder(root)
print()
inorder(r)
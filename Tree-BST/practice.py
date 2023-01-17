from collections import deque, OrderedDict


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


pre_indx = 0
def build_tree_InO_PreO(preo, io, isi, iei):
    if isi > iei:
        return None
    
    global pre_indx
    
    root = Node(preo[pre_indx])
    pre_indx += 1
    
    if isi == iei:
        return root
    
    for i in range(io):
        if io[i] == root.data:
            break
    
    root.left = build_tree_InO_PreO(preo, io, isi, i-1)
    root.right = build_tree_InO_PreO(preo, io, i+1, iei)
    
    return root


# res = [[5], [3, 9], [2, 4]]
# res.reverse()
# print(res)


def path_sum(root, target):
    pass
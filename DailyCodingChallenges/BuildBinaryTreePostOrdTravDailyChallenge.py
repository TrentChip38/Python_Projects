#Reconstruct a tree
#Given the sequence of keys 
# visited by a postorder traversal 
# of a binary search tree, 
# reconstruct the tree.

# For example, given the sequence 2, 4, 3, 8, 7, 5, 
# you should construct the following tree:
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

# you could just invert and then use build from binarytree, 
# but i'll manually add nodes to remember how to build a tree for fun
# this doesn't work

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addNode(value, node):
    if node == None:
        print("placed", value)
        node = Node(value)
    elif (value > node.val):
        print("Right")
        addNode(value, node.right)
    elif (value < node.val):
        print("left")
        addNode(value, node.left)
    #return node

def reconstructTree(nums):
    #loop through it backwards
    root = None
    for value in nums[::-1]:
        #print(value)
        addNode(value, root)
    print(root.val)
    return root


nums = [2, 4, 3, 8, 7, 5]
print(nums)
#Tree = Node(3)
Tree = reconstructTree(nums)
print(Tree.val)
print(Tree.left.val)
print(Tree.right.val)
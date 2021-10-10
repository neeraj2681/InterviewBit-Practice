# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inverter(self, root):
        if (root == None):
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.inverter(root.left)
        self.inverter(root.right)
        
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        self.inverter(A)
        return A

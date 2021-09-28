# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    preorder_list = []
    
    def preorder_traversal(self, root):
        
        self.preorder_list.append(root.val)
        
        if (root.left != None):
            self.preorder_traversal(root.left)
        
        if (root.right != None):
            self.preorder_traversal(root.right)
        
    def preorderTraversal(self, A):
        self.preorder_list = []
        if (A == None):
            return self.preorder_list
        self.preorder_traversal(A)
        return self.preorder_list
            

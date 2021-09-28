# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    k = 0
    def inorder_traversal(self, A, B):
        if (A.left != None):
            self.inorder_traversal(A.left, B)
        self.k = self.k + 1
        print("vaL: ",  A.val)
        val = A.val
        if (self.k == B):
            return val
        if (A.right != None):
            self.inorder_traversal(A.right, B)
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        self.k = 0
        return self.inorder_traversal(A, B)
        

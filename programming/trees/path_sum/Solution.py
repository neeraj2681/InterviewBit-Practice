# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    ans = 0
    def summer(self, root, B, summation):
        summation+=root.val
        if (root.left == None and root.right == None and B == summation):
            self.ans = 1
            
        if (root.left != None):
            self.summer(root.left, B, summation)
            
        if (root.right != None):
            self.summer(root.right, B, summation)
        
            
        
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if (A == None):
            return 0
            
        self.ans = 0
        temp = 0
        self.summer(A, B, 0)
        return self.ans

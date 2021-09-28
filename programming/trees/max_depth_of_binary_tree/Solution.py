# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if (A == None):
            return 0
        return max(self.maxDepth(A.left) + 1, self.maxDepth(A.right) + 1)

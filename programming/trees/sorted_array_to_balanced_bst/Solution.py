# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def makeTree(self, low, end, A):
        if (end < low):
            return None
        mid = (end - low + 1) // 2 + low
        root = TreeNode(A[mid])
        root.left = self.makeTree(low, mid - 1, A)
        root.right = self.makeTree(mid + 1, end, A)
        return root
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        low = 0
        end = len(A) - 1
        mid = (end - low + 1) // 2 + low
        root = TreeNode(A[mid])
        root.left = self.makeTree(low, mid - 1, A)
        root.right = self.makeTree(mid + 1, end, A)
        return root

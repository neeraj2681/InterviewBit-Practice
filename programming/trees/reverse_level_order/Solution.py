# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        rev_order = []
        queue = []
        queue.append(A)
        queue.append(TreeNode(-1))
        length = 1
        ptr = 0
        while (length > 0):
            node = queue[ptr]
            ptr+=1
            if (node.val == -1):
                queue.append(TreeNode(-1))
                continue
            else:
                length-=1

            if (node.right != None):
                queue.append(node.right)
                length+=1

            if (node.left != None):
                queue.append(node.left)
                length+=1
        for node in queue:
            if (node.val != -1):
                rev_order.append(node.val)
        rev_order.reverse()
        return rev_order
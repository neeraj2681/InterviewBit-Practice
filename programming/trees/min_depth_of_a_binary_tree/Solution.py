# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = -1
    def min_finder(self, A, temp_sum):
        temp_sum+=1
        #print("temp_val: ", temp_sum)
        #print("cur val: \n", A.val)
        if (A.left == None and A.right == None):
            if (self.ans < 0 or self.ans > temp_sum):
                self.ans = temp_sum
                temp_sum = 0
            #self.temp_sum-=1
            
        if (A.left != None):
            self.min_finder(A.left, temp_sum)
            
        if (A.right != None):
            self.min_finder(A.right, temp_sum)
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        self.ans, temp_sum = -1, 0
        if (A == None):
            return 0
        self.min_finder(A, temp_sum)
        return self.ans
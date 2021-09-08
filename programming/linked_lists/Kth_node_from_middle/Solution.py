# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp = A
        n = 0
        
        while(temp != None):
            n+=1
            temp = temp.next
        
        pos = n // 2 - B
        
        if (pos < 0):
            return -1
        temp = A
        while(pos != 0):
            temp = temp.next;
            pos-=1
        return temp.val

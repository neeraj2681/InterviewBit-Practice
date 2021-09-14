# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if (A == None):
            return None
        ptr1 = A
        temp = None
        ans = None
        checker = ListNode(0)
        while(ptr1 != None):
            if (ptr1.next == checker):
                return ptr1
            temp = ptr1
            ptr1 = ptr1.next
            temp.next = checker
        return None
            

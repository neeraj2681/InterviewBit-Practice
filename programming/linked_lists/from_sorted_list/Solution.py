# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if (A == None):
            return A
            
        ptr1, ptr2 = A, A.next
        if (ptr2 == None):
            return A
        
        while(ptr1 != None and ptr2 != None):
            if (ptr1.val == ptr2.val):
                ptr1.next = ptr2.next
                ptr2 = ptr1.next
            else:
                ptr1 = ptr1.next
                ptr2 = ptr1.next
        return A

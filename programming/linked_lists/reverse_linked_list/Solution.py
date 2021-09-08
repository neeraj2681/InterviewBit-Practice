# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
        ptr_start, ptr_end = A, A.next
        ptr_start.next = None
        new_head = A
        while(ptr_end != None):
            if (ptr_end.next == None):
                new_head = ptr_end
            temp = ptr_end.next
            ptr_end.next = ptr_start
            ptr_start = ptr_end
            ptr_end = temp

        return new_head
        

        


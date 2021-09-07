# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if (A == None and B == None):
            return None
        if (A == None and B != None):
            return B
        if (A != None and B == None):
            return A
            
        head = A
        ptr1, ptr2 = A, B
        carry = 0
        t1 = None
        while(ptr1 != None and ptr2 != None):
            ptr1.val = ptr1.val + ptr2.val + carry
            carry = ptr1.val / 10
            ptr1.val = ptr1.val % 10
            t1 = ptr1
            #print("ptr1.val orignal: ", ptr1.val, "Carry: ", carry)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        while (ptr1 != None):
            ptr1.val = ptr1.val + carry
            carry = ptr1.val / 10
            ptr1.val = ptr1.val % 10
            #print("ptr1.val: ", ptr1.val, "Carry: ", carry)
            t1 = ptr1
            ptr1 = ptr1.next
            #print("ptr1(Null check): ", ptr1, "Carry: ", carry)
        
        if (ptr2 != None):
            ptr1 = t1
            
        while (ptr2 != None):
            #print("ptr2.val: ", ptr2.val, "Carry: ", carry)
            ptr1.next = ListNode(0)
            ptr1 = ptr1.next
            t1 = ptr1
            ptr1.val = ptr2.val + carry
            carry = ptr1.val / 10
            ptr1.val = ptr1.val % 10
            ptr2 = ptr2.next
            
        if (carry > 0):
            #print("Indide carry: ", carry)
            
            ptr1 = t1
            #print("ptr.val: ", ptr1.val)
            ptr1.next = ListNode(carry)
            
        return head




















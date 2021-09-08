# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def find_intersection(self, A, B, diff, bigger):
        head_bigger = None
        head_smaller = None
        
        if (bigger == 1):
            head_bigger = A
            head_smaller = B
        else:
            head_bigger = B
            head_smaller = A
        
        for i in range(diff):
                head_bigger = head_bigger.next
        
        while(head_bigger != None):
            if (head_bigger == head_smaller):
                return head_bigger
            head_bigger = head_bigger.next
            head_smaller = head_smaller.next
        
        return None
            
        
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        temp = A
        count1 = 0
        count2 = 0
        
        while(temp != None):
            temp = temp.next
            count1+=1
        
        temp = B
        while(temp != None):
            temp = temp.next
            count2+=1
            
        diff = 0
        if (count1 > count2):
            diff = count1 - count2
            return self.find_intersection(A, B, diff, 1)
        else:
            diff = count2 - count1
            return self.find_intersection(A, B, diff, 2)
        
        
        
        
        

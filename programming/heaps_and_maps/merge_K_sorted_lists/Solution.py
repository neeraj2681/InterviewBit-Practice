# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        head = ListNode(0)
        temp = head
        heaper = []
        for i in range(len(A)):
            temp2 = A[i]
            while (temp2 != None):
                heapq.heappush(heaper, (temp2.val, i))
                temp2 = temp2.next
        heapq.heapify(heaper)
        #print("heaper: ", heaper)
        while (len(heaper) != 0):
            index = heapq.heappop(heaper)[1]
            #print("indexer: ", index)
            temp.next = A[index]
            #print("node: ", A[index])
            A[index] = A[index].next
            temp = temp.next
        return head.next
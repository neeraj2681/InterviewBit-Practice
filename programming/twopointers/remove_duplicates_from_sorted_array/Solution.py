class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if (len(A) == 0 or len(A) == 1):
            return len(A)
        ptr1, ptr2, swapper = 0, 1, 1
        length = len(A)
        while (ptr2 < length):
            if (A[ptr1] == A[ptr2]):
                ptr2+=1
            else:
                A[ptr1 + 1] = A[ptr2]
                ptr1+=1
                ptr2+=1
        return (ptr1 + 1)
                
            

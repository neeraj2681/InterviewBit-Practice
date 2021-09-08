class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if (len(A) <= 1):
            return A
        ptr1, ptr2 = 0, 1
        
        A = sorted(A)
        
        while(ptr2 < len(A)):
            temp = A[ptr1]
            A[ptr1] = A[ptr2] 
            A[ptr2] = temp
            ptr1+=2
            ptr2+=2
        return A
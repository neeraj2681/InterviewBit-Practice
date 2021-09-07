class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if (len(A) <= 1):
            return 0
            
        ptr1, ptr2 = 0, 1
        while(ptr2 < len(A)):
            #print("ptr1:" , A[ptr1] , "ptr2:" , A[ptr2])
            if ((A[ptr1] - A[ptr2] == B) or (A[ptr2] - A[ptr1] == B)):
                return 1
            if ((A[ptr2] - A[ptr1]) < B):
                ptr2+=1
            else:
                ptr1+=1
            if (ptr1 == ptr2):
                ptr2+=1
                
        return 0
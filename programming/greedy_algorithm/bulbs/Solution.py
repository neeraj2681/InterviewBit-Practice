class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        if (len(A) == 0):
            return 0
        if (len(A) == 1):
            if (A[0] == 0):
                return 1
            else:
                return 0
                
        count = 0
        
        if (A[0] == 0):
            count = 1
            
        for i in range(1,len(A)):
            if (A[i] == A[i - 1]):
                continue
            else:
                count+=1
        return count

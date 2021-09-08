class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        
        A = sorted(A)
        return A[len(A) // 2]
        

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l = len(A)
        ans = 0
        for i in range(l):
            if (A[i] == 'a' or A[i] == 'e' or A[i] == 'i' or A[i] == 'o' or 
            A[i] == 'u' or A[i] == 'A' or A[i] == 'E' or A[i] == 'I' or A[i] == 'O' or A[i] == 'U'):
               ans+=(l - i)
               ans = ans % 10003
        return ans
            

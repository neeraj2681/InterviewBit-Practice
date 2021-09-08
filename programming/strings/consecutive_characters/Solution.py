class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        ptr1 = 0
        ans = ""
        while((ptr1) < len(A)):
            temp = A[ptr1] * B
            if (A[ptr1: ptr1 + B] == temp):
                ptr1+=B
            else:
                ans = ans + A[ptr1:ptr1 + 1]
                ptr1+=1
        return ans
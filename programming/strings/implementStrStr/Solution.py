class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        ans = -1
        if (A == None or B == None):
            return ans
        s_length = len(B)
        for i in range(len(A)):
            #print("current_char: ", B[i])
            if (A[i] == B[0] and len(A) >= (i + s_length) and B == A[i: i + s_length]):
                return i
        return ans
                

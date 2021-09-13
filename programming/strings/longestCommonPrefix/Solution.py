class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if (len(A) == 1):
            return A[0]
        if (len(A) == 0):
            return ""
        word = A[0]
        ans = ""
        for j in range(len(word)):
            for i in range(1, len(A), 1):
                if (j >= len(A[i]) or word[j] != A[i][j]):
                    return ans
            ans = ans + word[j]
            
        return ans
            

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        str_set = A.split()
        if (len(str_set) > 0):
            return len(str_set[len(str_set) - 1])
        return 0
        

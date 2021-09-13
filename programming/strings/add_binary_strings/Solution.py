class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        ptr1, ptr2 = len(A) - 1, len(B) - 1
        d1, d2 = int(A, 2), int(B, 2)
        result = d1 + d2
        result = bin(result).replace("0b", "")
        return result
            

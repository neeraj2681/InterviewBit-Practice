class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        B = []
        flag = True
        for i in A:
            if (i == 0 and flag == True):
                continue
            else:
                B.append(i)
                flag = False
        l = len(B)
        if (l == 0):
            return [1]
        carry = 1
        C = []
        for i in range(l - 1, -1, -1):
            temp = B[i] + carry
            C.append(temp % 10)
            carry = temp // 10
        if (carry > 0):
            C.append(carry)
        C.reverse()
        return C
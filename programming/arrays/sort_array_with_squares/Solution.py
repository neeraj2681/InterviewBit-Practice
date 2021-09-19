class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        if (len(A) == 0):
            return ans
            
        ptr1, ptr2 = 0, len(A) - 1
        while (ptr1 <= ptr2):
            if (abs(A[ptr1]) >= abs(A[ptr2])):
                ans.append(abs(A[ptr1]) * abs(A[ptr1]))
                ptr1+=1
            else:
                ans.append(abs(A[ptr2]) * abs(A[ptr2]))
                ptr2-=1
        ans.reverse()    
        return ans
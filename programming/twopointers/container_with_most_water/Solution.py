class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        ptr1, ptr2 = 0, len(A) - 1
        ans = 0
        while (ptr1 <= ptr2):
            if (A[ptr1] < A[ptr2]):
                area = (ptr2 - ptr1) * A[ptr1]
                ptr1+=1
            else:
                area = (ptr2 - ptr1) * A[ptr2]
                ptr2-=1
            if (ans < area):
                ans = area
        return ans
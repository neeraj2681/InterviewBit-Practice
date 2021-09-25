import heapq
import math
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        C = [-x for x in B]
        heapq.heapify(C)
        ans = 0
        i = 0
        while (i < A):
            val = heapq.heappop(C) * -1
            #print("val: ", val)
            ans += val
            ans %= (1000000007)
            #print("math_floor: ", val // 2)
            heapq.heappush(C, (val // 2) * -1)
            i+=1
        return ans

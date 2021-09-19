#solution is not optimal, new and optimised solution will be added soon!
import heapq

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for vector in A:
            for num in vector:
                ans.append(num)
        heapq.heapify(ans)
        
        real_ans = []
        while(len(ans) > 0):
            real_ans.append(heapq.heappop(ans))
        return real_ans
            
            

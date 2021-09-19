import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        C = []
        for num in A:
            C.append(-1 * num)
        profit = 0
        heapq.heapify(C)
        while ( B > 0):
            temp = heapq.heappop(C)
            profit+=(temp * -1)
            heapq.heappush(C, temp + 1)
            B-=1
        return profit
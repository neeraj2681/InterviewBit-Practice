class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        #if there is no or only single element
        if (len(A) <= 1):
            return 0
            
        profit = 0
        nadir = A[0]
        
        #tries to find the profit based on the minimum stock price in prefix array
        for i in A:
            if (profit <= (i - nadir)):
                profit= i - nadir
            if (nadir >= i):
                nadir = i
        return profit
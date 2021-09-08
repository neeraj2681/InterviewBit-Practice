class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        if (A < 0):
            return 0
        temp = A
        reverse = 0
        while(temp > 0):
            reverse = reverse * 10 + temp % 10
            temp = temp // 10
        
        if (A == reverse):
            return 1

        return 0

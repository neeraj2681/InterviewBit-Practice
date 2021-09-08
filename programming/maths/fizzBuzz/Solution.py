class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
        ans_list = []
        for num in range(A + 1):
            if (num == 0):
                continue

            if (num % 15 == 0):
                ans_list.append("FizzBuzz")
            elif num % 5 == 0:
                ans_list.append("Buzz")
            elif num % 3 == 0:
                ans_list.append("Fizz")
            else:
                ans_list.append(num)
        return ans_list

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        num_steps = [None] * 3
        num_steps[0] = 0
        num_steps[1] = 1
        num_steps[2] = 2

        ptr1, ptr2 = num_steps[1], num_steps[2]

        if (A == 0 or A == 1 or A == 2):
                return num_steps[A]

        for i in range(3, A + 1):
                if (i == 0 or i == 1 or i == 2):
                    continue
                
                ans = ptr1 + ptr2
                ptr1 = ptr2
                ptr2 = ans

        return ans


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if (len(A) <= 1):
            return 0
            
        ptr1 = len(A) - 1
        vowels, cons = 0, 0
        ans = 0
        while(ptr1 >= 0):
            if (A[ptr1] == 'a' or A[ptr1] == 'e' or A[ptr1] == 'i' or A[ptr1] == 'o' or A[ptr1] == 'u'):
               ans+=cons
               vowels+=1
            else:
                ans+=vowels
                cons+=1
            ptr1-=1
            ans = ans % (10000007)
        return ans


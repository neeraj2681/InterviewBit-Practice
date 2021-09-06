class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        open_braces = 0
        required = 0
        for i in A:
            if (i == '('):
                open_braces+=1
            else:
                if (open_braces > 0):
                    open_braces-=1
                else:
                    required+=1
        required+=open_braces
        return required

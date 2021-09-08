xclass Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_num = max(A)
        min_num = min(A)
        return min_num + max_num

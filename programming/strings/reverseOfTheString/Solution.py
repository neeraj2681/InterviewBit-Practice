class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        reverse_list = A.split()
        reverse = ""
        for i in range(len(reverse_list) - 1, -1, -1):
            if (i == len(reverse_list) - 1):
                reverse = reverse_list[i]
            else:
                reverse = reverse + " " + reverse_list[i]
        
        return reverse

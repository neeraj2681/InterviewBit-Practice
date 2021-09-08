class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        new_dict = dict()
        for key, num in enumerate(A):
            new_dict[num] = key
        
        if (B == 0 and len(new_dict.keys()) == len(A)):
            return 0
            
        for key in new_dict.keys():
            if (key + B) in new_dict.keys():
                return 1 
                
        return 0
        

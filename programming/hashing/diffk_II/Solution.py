class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        mapper = dict()
        for num in A:
            if (mapper.has_key(num)):
                mapper.update({num: [num - B, (mapper[num])[1] + 1]})
            else:
                mapper.update({num: [num - B, 1]})
                
        ans = 1
        if (B == 0):
            for key in mapper:
                if ((mapper[key])[1] > 1):
                    return 1
            ans = 0
            
        if (ans == 0):
            return 0
            
        for key in mapper:
            if (mapper.has_key((mapper[key])[0])):
                return 1
        return 0
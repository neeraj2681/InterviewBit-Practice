class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        mapper = dict()
        for char in A:
            if (mapper.has_key(char)):
                mapper.update({char: mapper.get(char) + 1})
            else:
                mapper.update({char: 1})
                
        odd, even = 0, 0
        for key in mapper:
            if (mapper.get(key) % 2 == 0):
                even+=1
            else:
                odd+=1
        if (odd > 1):
            return 0
        return 1
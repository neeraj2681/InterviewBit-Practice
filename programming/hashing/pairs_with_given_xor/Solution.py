class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mapper = dict()
        mapper2 = dict()
        for num in A:
            mapper.update({num: num ^ B})
            
        for num in A:
            if (mapper2.has_key(num)):
                mapper2.update({num: mapper2.get(num) + 1})
            else:
                mapper2.update({num: 1})
        ans = 0
        
        if (B == 0):
            for num in mapper2:
                if (mapper2.get(num) > 1):
                    ans+=1
            return ans
        
        
        for key in mapper:
            if (mapper.has_key(mapper[key])):
                ans+=1
                
        return ans//2
        

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        ans = []
        mapper = {}
        for num in A:
            mapper.update({num: 1})
        #print(mapper)
        for num in B:
            if(mapper.get(num) == 1):
                ans.append(num)
                mapper.update({num: 2})
            elif (mapper.get(num) == 2 or mapper.get(num) == 3):
                continue
            else:
                mapper.update({num: 3})
     #   print(mapper)
    #    print(ans)
        
        for num in C:
            if (mapper.get(num) == 1 or mapper.get(num) == 3):
                ans.append(num)
                mapper.pop(num)
        #print(mapper)
        return sorted(ans)
        
        

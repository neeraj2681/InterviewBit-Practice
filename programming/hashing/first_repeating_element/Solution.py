class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mapper = dict()
        ans = len(A)
        pos = len(A)
        for i in range(len(A)):
            if (mapper.has_key(A[i])):
                if (mapper.get(A[i]) < pos):
                    ans = A[i]
                    pos = mapper.get(A[i])
            else:
                mapper.update({A[i]: i})
            #print("pos: ", pos)
        if (pos == len(A)):
            return -1
        
        return ans
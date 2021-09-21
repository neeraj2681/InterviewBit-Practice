class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if (B > len(A)):
            return []
        ans = []
        mapper = dict()
        ptr1 = 0
        prev = 0
        for i in range(ptr1, ptr1 + B):
            if (mapper.has_key(A[i])):
                mapper.update({A[i] : mapper.get(A[i]) + 1})
            else:
                mapper.update({A[i] : 1})
        ans.append(len(mapper.keys()))
        distinct = len(mapper.keys())
        ptr1+=B
        while (ptr1 < len(A)):
            if (mapper.has_key(A[ptr1])):
                mapper.update({A[ptr1] : mapper.get(A[ptr1]) + 1})
            else:
                mapper.update({A[ptr1] : 1})
                distinct+=1
            count = mapper.get(A[prev])
            if (count == 1):
                mapper.pop(A[prev])
                distinct-=1
            else:
                mapper.update({A[prev] : mapper.get(A[prev]) - 1})
            ptr1+=1
            prev+=1
            ans.append(distinct)
        return ans
                
                
                
            
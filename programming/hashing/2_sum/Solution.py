class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        mapper = dict()
        for i in range(len(A)):
            if (mapper.has_key(A[i])):
                lister = mapper.get(A[i])
                lister.append(i)
                mapper.update({A[i]: lister})
            else:
                mapper.update({A[i]: [B - A[i], i]})
        #print("mapper: ", mapper)
        start, end = len(A), len(A)
        for num in A:
            if (mapper.has_key(mapper.get(num)[0])):
                if (num == (B - num) and len(mapper.get(num)) > 2):
                    new_start = mapper.get(num)[1]
                    new_end = mapper.get(num)[2]
                    if (end > new_end):
                        start = new_start
                        end = new_end
                    
                new_start = mapper.get(num)[1]
                new_end = mapper.get(mapper.get(num)[0])[1]
                if (end > new_end and new_start < new_end):
                    end = new_end
                    start = new_start
        if (start == len(A)):
            return []
        return [start + 1, end + 1]

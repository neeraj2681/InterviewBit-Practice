class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        mapper = dict()
        ans = []
        for i in range(len(A)):
            lister = [0] * 26
            for char in A[i]:
                lister[ord(char) - 97] = lister[ord(char) - 97] + 1
                
            lister2 = tuple(lister)
            if (mapper.has_key(lister2)):
                #print("word: ", A[i])
                #print("lister2: ", lister2)
                jar = mapper.get(lister2)
                jar.append(i + 1)
                #print("jar: ", jar)
                mapper.update({lister2: jar})
            else:
                mapper.update({lister2: [i + 1]})
        #print("mappper: ", mapper)        
        for key in mapper:
            temp = mapper.get(key)
            #print("temp: ", temp)
            ans.append(temp)
        return ans

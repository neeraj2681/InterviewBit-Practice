class Solution:
    def convert(self, c):
        if (ord(c) >= 97 and ord(c) <= 122):
            return chr(ord(c) - 32)
        return chr(ord(c))
    # @param c: character
    #@return a boolean value
    def not_valid(self, c):
        if ((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or
        (ord(c) >= 48 and ord(c) <= 57)):
            return False
        return True
        
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        ptr1, ptr2 = 0, len(A) - 1
        while(ptr1 <= ptr2):
            if (self.not_valid(A[ptr1])):
                ptr1+=1
                continue
            if (self.not_valid(A[ptr2])):
                ptr2-=1
                continue
            #print("print it: ", A[ptr1], A[ptr2])
            t1 = self.convert(A[ptr1])
            t2 = self.convert(A[ptr2])
            if (t1 != t2):
                return 0
            ptr1+=1
            ptr2-=1
            
        
        return 1

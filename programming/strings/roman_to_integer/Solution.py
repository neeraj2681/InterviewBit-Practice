class Solution:
    def value(self, c):
        if (c == 'I'):
            return 1
        elif c == 'II':
            return 2
        elif c == 'III':
            return 3
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        else:
            return 1000
            
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        p_val = 0
        c_val = 0
        val = 0
        for i in A:
            p_val = c_val 
            c_val = self.value(i)
            if (p_val < c_val):
                c_val = c_val - p_val
                val-=p_val
            val+=c_val
            #print("val: ", val)
        return val
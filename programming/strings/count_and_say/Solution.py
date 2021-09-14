class Solution:
    def check_str(self, word):
        if (word == "1"):
            return "11"
        count = 0
        ptr1, ptr2 = 0, 1
        ans = ""
        while(ptr2 < len(word)):
            if (word[ptr1] != word[ptr2]):
                ans = ans +  str(count + 1) + word[ptr1]
                count = 0
            else:
                count+=1
            ptr1+=1
            ptr2+=1
            
        ans = ans + str(count + 1) + word[ptr1]
        return ans
        
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if (A == 1):
            return "1"
        ans = "1"
        for i in range(A - 1):
           # print("ans: ", ans)
            ans = self.check_str(ans)
        return ans

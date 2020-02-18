package com.interviewbit.strings.lengthOfTheLastWord;

public class Solution {
    public int lengthOfLastWord(final String A) {
        int length = 0;
        int ans = 0;
        for(int i = 0; i < A.length(); i++) {
            if(A.charAt(i) == ' ') {
                if(length != 0)
                    ans = length;
                length = 0;
            }else {
                length++;
            }
        }
        if(length != 0)
            return length;

        return ans;
    }
}

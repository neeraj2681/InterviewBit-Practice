package com.interviewbit.programming.strings.lengthOfTheLastWord;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param A: the input string
     * @return the length of the last word present, if present in the string
     */
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

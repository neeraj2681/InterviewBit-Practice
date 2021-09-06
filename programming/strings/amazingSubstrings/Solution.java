package com.interviewbit.programming.strings.amazingSubstrings;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param c: the character of the input string
     * @return the validity whether the character is a vowel or not
     */
    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }

    /**
     *
     * @param A: input string
     * @return all possible amazing substrings modulus 10003
     */
    public int solve(String A) {
        long count = 0;
        for(int i = 0; i < A.length(); i++) {
            if(isVowel(A.charAt(i))) {
                count+=(A.length() - i);
            }
        }
        return (int)(count % 10003);
    }
}

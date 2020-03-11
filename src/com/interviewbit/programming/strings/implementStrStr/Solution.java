package com.interviewbit.programming.strings.implementStrStr;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * @param A: the input string in which search happens
     * @param B: the input substring which needs to be searched
     * @return the staring index of B in A
     */
    public int strStr(final String A, final String B) {
        if (B.length() == 0 || A.length() == 0)
            return -1;
        int lSubstring = B.length();
        int lString = A.length();
        for (int i = 0; i <= (lString - lSubstring); i++) {
            if (A.substring(i, i + lSubstring).equals(B))
                return i;
        }
        return -1;
    }
}

package com.interviewbit.programming.strings.reverseOfTheString;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * @param A: the input string
     * @return the reverse of the string
     */
    public String solve(String A) {
        StringBuilder ans = new StringBuilder("");
        StringBuilder word = new StringBuilder("");
        for (int i = A.length() - 1; i >= 0; i--) {
            if (A.charAt(i) == ' ' && word.length() != 0) {
                if (ans.length() == 0) {
                    ans.append(word.reverse());
                } else {
                    ans.append(" ");
                    ans.append(word.reverse());
                }

                word = new StringBuilder("");
            } else if (A.charAt(i) == ' ' && word.length() == 0)
                continue;
            else {
                word.append(A.charAt(i));
            }
        }
        if (word.length() != 0) {
            if (ans.length() == 0) {
                ans.append(word.reverse());
            } else {
                ans.append(" ");
                ans.append(word.reverse());
            }
        }
        return ans.toString();
    }
}

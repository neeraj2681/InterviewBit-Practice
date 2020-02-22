package com.interviewbit.programming.strings.longestCommonPrefix;

import java.util.ArrayList;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param A the input array-list of strings
     * @return the common prefix among all strings in the array-list
     */
    public String longestCommonPrefix(ArrayList<String> A) {
        String minStr = "";
        int min = Integer.MAX_VALUE;
        for (String value : A) {
            if (value.length() < min) {
                minStr = value;
                min = minStr.length();
            }
        }
        StringBuilder ans = new StringBuilder();
        for(int i = 0; i < minStr.length(); i++) {
            for (String s : A) {
                if (minStr.charAt(i) != s.charAt(i)) {
                    return ans.toString();
                }
            }
            ans.append(minStr.charAt(i));
        }
        return ans.toString();
    }
}

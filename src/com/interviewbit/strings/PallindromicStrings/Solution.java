package com.interviewbit.strings.PallindromicStrings;

public class Solution {
    boolean isValid(String A, int index) {
        if((A.charAt(index) >= 'A' && A.charAt(index) <= 'Z') ||
                (A.charAt(index) >= 'a' && A.charAt(index) <= 'z') ||
                (A.charAt(index) >= '0' && A.charAt(index) <= '9'))
            return true;
        return false;
    }
    public int isPalindrome(String A) {
        int start = 0, end = A.length() - 1;
        char s = ' ', e = ' ';
        while(start <= end) {

            if(isValid(A, start)) {
                if(isValid(A, end)) {
                    if(A.charAt(start) < 97 && A.charAt(start) > 64) {
                        s = (char)(A.charAt(start) + 32);
                    }else {
                        s = A.charAt(start);
                    }

                    if(A.charAt(end) < 97 && A.charAt(end) > 64) {
                        e = (char)(A.charAt(end) + 32);
                    }else {
                        e = A.charAt(end);
                    }
                    if(s == e) {
                        start++;
                        end--;
                        continue;
                    }
                    else
                        return 0;
                }else {
                    end--;
                    continue;
                }
            }else {
                start++;
                continue;
            }
        }
        return 1;
    }
}

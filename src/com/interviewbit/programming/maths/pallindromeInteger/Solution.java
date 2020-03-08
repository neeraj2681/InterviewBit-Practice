package com.interviewbit.programming.maths.pallindromeInteger;

/**
 * to check of pallindrome property
 */
public class Solution {
    /**
     *
     * @param A: user given integer
     * @return 1, if pallindromic in nature, else 0
     */
    public int isPalindrome(int A) {
        if (A < 0)
            return 0;
        int b = A;
        int reverse = 0;
        while (b != 0) {
            reverse = reverse * 10 + b % 10;
            b /= 10;
        }
        if (A == reverse)
            return 1;
        else
            return 0;
    }
}

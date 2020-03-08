package com.interviewbit.programming.maths.reverseInteger;

/**
 * finding the reverse of an integer
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     *
     * @param A: the input integer
     * @return : the reverse of the integer given
     */
    public int reverse(int A) {
        if (A == 0)
            return A;
        int b = A;
        long reverse = 0;
        while (b != 0) {
            reverse = reverse * 10 + b % 10;
            b /= 10;
        }
        if (reverse > (long) Integer.MAX_VALUE)
            return 0;
        if (reverse < (long) Integer.MIN_VALUE)
            return 0;
        return (int) reverse;
    }
}


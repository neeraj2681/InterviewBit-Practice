package com.interviewbit.programming.bitManipulation.reverseBits;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     *
     * @param a the input 32-bit unsigned integer
     * @return the unsigned integer in decimal format, after the bits have been reversed
     */
    public long reverse(long a) {
        long ans = 0;
        int count = 0;
        while (a != 0) {
            if (a % 2 != 0) {
                a /= 2;
                ans += Math.pow(2, 31 - count);
                count++;
            } else {
                count++;
                a /= 2;
            }
        }
        return ans;
    }
}

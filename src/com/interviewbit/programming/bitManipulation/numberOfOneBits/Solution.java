package com.interviewbit.programming.bitManipulation.numberOfOneBits;

/**
 * @author thethinkngphilosopher@keemail.me
 */
public class Solution {
    /**
     *
     * @param a: the unsigned integer inputted by user
     * @return the number of 1's in binary representation of input integer
     */
    public int numSetBits(long a) {
        int count = 0;
        while (a != 0) {
            if (a % 2 != 0)
                count++;
            a /= 2;
        }
        return count;
    }
}

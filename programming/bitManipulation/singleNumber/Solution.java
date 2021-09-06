package com.interviewbit.programming.bitManipulation.singleNumber;

import java.util.List;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * @param A: the input array/list of integer
     * @return the number which occurs only once in array A
     */
    public int singleNumber(final List<Integer> A) {
        long ans = 0;
        for (Integer a : A) {
            ans = ans ^ a;
        }
        return (int) ans;
    }
}

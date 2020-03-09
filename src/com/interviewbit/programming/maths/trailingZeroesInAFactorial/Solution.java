package com.interviewbit.programming.maths.trailingZeroesInAFactorial;

/**
 * @author thethinkingphilosopher
 */
public class Solution {
    int ans = 0;
    /**
     *
     * @param A: the input integer
     */
    void calculate(int A) {
        while (A % 5 == 0) {
            ans++;
            A /= 5;
        }
    }

    /**
     *
     * @param A: the input integer
     * @return the no of trailing zeroes in its factorial
     */
    public int trailingZeroes(int A) {
        for (int i = A; i >= 1; i--) {
            calculate(i);
        }
        return ans;
    }
}

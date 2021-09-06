package com.interviewbit.programming.maths.gcd;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param A first integer
     * @param B second integer
     * @return the gcd of A and B
     */
    public int gcd(int A, int B) {
        if (B == 0)
            return A;
        return gcd(B, A % B);
    }
}

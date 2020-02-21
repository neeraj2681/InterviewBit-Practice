package com.interviewbit.programming.arrays.waveArray;

import java.util.Arrays;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param A the input array
     * @return the wave array
     */
    public int[] wave(int[] A) {
        Arrays.sort(A); // sort the input array
        int temp, j = 1;
        /*
        Swapping happens in this while loop, between every pair of elements
         */
        while(j < A.length) {
            temp = A[j - 1];
            A[j - 1] = A[j];
            A[j] = temp;
            j+=2;
        }
        return A;
    }
}

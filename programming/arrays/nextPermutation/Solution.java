package com.interviewbit.programming.arrays.nextPermutation;

import java.util.Arrays;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * calculates the next permutation
     * @param A the user inputted array
     * @return the next Permutation by modifying the input array
     */
    public int[] nextPermutation(int[] A) {
        if (A.length == 1)
            return A;
        boolean flag = true;
        int j = A.length - 1;
        while (j > 0 && flag) {
            if (A[j - 1] >= A[j])
                j--;
            else {
                flag = false;
                int min = Integer.MAX_VALUE;
                int val = A[j - 1];
                int index = 0;
                for (int i = j; i < A.length; i++) {
                    if (A[i] > val) {
                        if (A[i] - val < min) {
                            min = A[i] - val;
                            index = i;
                        }
                    }
                }
                int temp = A[j - 1];
                A[j - 1] = A[index];
                A[index] = temp;
                Arrays.sort(A, j, A.length);
            }
        }
        if (flag)
            Arrays.sort(A);
        return A;
    }
}

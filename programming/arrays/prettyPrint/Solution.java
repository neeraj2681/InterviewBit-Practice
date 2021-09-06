package com.interviewbit.programming.arrays.prettyPrint;

/**
 * @author neeraj2681
 */
public class Solution {
    int[][] arr;
    void printer(int val, int r1, int r2, int c1, int c2) {
        for(int i = c1; i < c2; i++) {
            arr[r1][i] = val;
            arr[r2 - 1][i] = val;
        }
        for(int i = r1; i < r2; i++) {
            arr[i][c1] = val;
            arr[i][c2 - 1] = val;
        }
    }

    /**
     *
     * @param A user input regarding array structure
     * @return the newly created pretty array
     */
    public int[][] prettyPrint(int A) {
        arr = new int[2 * A - 1][2 * A - 1];
        int r1 = 0, r2 = 2 * A - 1, c1 = 0, c2 = 2 * A - 1;
        for(int i = A; i > 0; i--) {
            printer(i, r1++, r2--, c1++, c2--);
        }
        return arr;
    }
}

package com.interviewbit.programming.arrays.spiralMatrix;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    int[][] arr;
    int n = 1;
    int val = 0;

    /**
     * writes left to right manner
     * @param sc the starting column
     * @param sr the row on which left to right writing will happen
     * @param ec the ending column(if 5, then we go up to 4)
     */
    public void leftToRight(int sc, int sr, int ec) {
        for (int i = sc; i < ec; i++) {
            arr[sr][i] = n++;
        }
        if (n == val)
            return;
        topToBottom(sr + 1, ec - 1, sr + (ec - sc));
    }

    /**
     * writes top to bottom manner
     * @param sr starting row
     * @param sc the column on which top to bottom writing happens
     * @param er ending row
     */
    public void topToBottom(int sr, int sc, int er) {
        for (int i = sr; i < er; i++) {
            arr[i][sc] = n++;
        }
        if (n == val)
            return;
        rightToLeft(sc - 1, er - 1, sc - 1 - (er - sr));
    }

    /**
     * writes right to left manner
     * @param sc the starting column
     * @param sr the row on which right to left writing happens
     * @param ec the ending column
     */
    public void rightToLeft(int sc, int sr, int ec) {
        for (int i = sc; i > ec; i--) {
            arr[sr][i] = n++;
        }
        if (n == val)
            return;
        bottomToTop(sr - 1, ec + 1, sr - (sc - ec));
    }

    /**
     * Writes bottom to top manner
     * @param sr the starting row
     * @param sc the column at which bottomToTop writing happens
     * @param er the end row
     */
    public void bottomToTop(int sr, int sc, int er) {
        for (int i = sr; i > er; i--) {
            arr[i][sc] = n++;
        }
        if (n == val)
            return;
        leftToRight(sc + 1, er + 1, sc + (sr - er) + 1);
    }

    /**
     * Generates the spiral form matrix
     * @param A the size of matrix as user input
     * @return the spiral form matrix
     */
    public int[][] generateMatrix(int A) {

        arr = new int[A][A];
        val = A * A + 1;
        leftToRight(0, 0, A);
        return arr;
    }
}

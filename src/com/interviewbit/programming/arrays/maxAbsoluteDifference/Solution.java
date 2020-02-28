package com.interviewbit.programming.arrays.maxAbsoluteDifference;

import java.util.ArrayList;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     *
     * @param A the user inputted array(in this case an arraylist of Integers)
     * @return
     */
    public int maxArr(ArrayList<Integer> A) {
        int[] sum = new int[A.size()];
        int[] diff = new int[A.size()];

        for (int i = 0; i < A.size(); i++) {
            sum[i] = A.get(i) + i;
            diff[i] = A.get(i) - i;
        }

        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        for (int i = 0; i < A.size(); i++) {
            if (max1 < sum[i])
                max1 = sum[i];

            if (max2 < diff[i])
                max2 = diff[i];

            if (min1 > sum[i])
                min1 = sum[i];

            if (min2 > diff[i])
                min2 = diff[i];
        }
        //System.out.println("max1: "+max1+" min1: "+min1+" max2: "+max2+" min1: "+min1);
        return Math.max(max1 - min1, max2 - min2);
    }
}

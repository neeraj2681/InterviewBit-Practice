package com.interviewbit.programming.arrays.maxContiguousSubArray;

import java.util.Collections;
import java.util.List;

/**
 * @author neeraj2681
 */
public class Solution {
    /**
     *
     * @param A the list of integers
     * @return the maximum possible sum of the contiguous array
     */
    public int maxSubArray(final List<Integer> A) {
        boolean isNeg = true;
        for (Integer integer : A) {
            if (integer >= 0) {
                isNeg = false;
                break;
            }
        }
        int ans = 0;
        if(!isNeg) {
            int maxSum = 0;
            for (Integer integer : A) {
                if (integer + maxSum >= 0) {
                    maxSum = integer + maxSum;
                    if (maxSum > ans)
                        ans = maxSum;
                } else {
                    maxSum = 0;
                }
            }
        }else {
            return Collections.max(A);
        }
        return ans;
    }
}

package com.interviewbit.programming.twopointers.intersectionOfSortedArrays;

import java.util.ArrayList;
import java.util.List;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * @param A the first array
     * @param B the second array
     * @return the array containing intersection of array A and array B
     */
    public ArrayList<Integer> intersect(final List<Integer> A, final List<Integer> B) {
        ArrayList<Integer> ans = new ArrayList<>();
        int ptr1 = 0, ptr2 = 0;
        while (ptr1 < A.size() && ptr2 < B.size()) {
            if (A.get(ptr1) > B.get(ptr2))
                ptr2++;
            else if (A.get(ptr1) < B.get(ptr2))
                ptr1++;
            else {
                ans.add(A.get(ptr1));
                ptr1++;
                ptr2++;
            }
        }
        return ans;
    }
}

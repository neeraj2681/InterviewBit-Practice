package com.interviewbit.programming.twopointers.sortByColor;

import java.util.ArrayList;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * @param a the user inputted array list
     */
    public void sortColors(ArrayList<Integer> a) {
        int zeroes = 0, ones = 0, twos = 0;
        for (Integer i : a) {
            if (i == 0)
                zeroes++;
            else if (i == 1)
                ones++;
            else
                twos++;
        }
        int index = 0;
        while (zeroes-- != 0) {
            a.set(index++, 0);
        }
        while (ones-- != 0) {
            a.set(index++, 1);
        }
        while (twos-- != 0) {
            a.set(index++, 2);
        }
    }
}

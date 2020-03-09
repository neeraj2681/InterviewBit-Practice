package com.interviewbit.programming.maths.fizzBuzz;

import java.util.ArrayList;

/**
 * @author alonewolf
 */
public class Solution {
    /**
     * @param A: the input array
     * @return the desired string
     */
    public ArrayList<String> fizzBuzz(int A) {
        ArrayList<String> list = new ArrayList<String>();
        for (int i = 1; i <= A; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                list.add("FizzBuzz");
                continue;
            }
            if (i % 3 == 0) {
                list.add("Fizz");
                continue;
            }
            if (i % 5 == 0) {
                list.add("Buzz");
                continue;
            }
            list.add(i + "");
        }
        return list;
    }
}


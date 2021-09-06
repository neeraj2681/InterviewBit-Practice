package com.interviewbit.programming.arrays.setMatrixZeroes;

import java.util.ArrayList;

/**
 * @author thethinkingphilosopher@keemail.me
 */
public class Solution {
    /**
     * set zeroes to respective column and row
     * @param a the user inputted 2-D array(in this case list of list of Integers)
     */
    public void setZeroes(ArrayList<ArrayList<Integer>> a) {
        boolean[] rowArr = new boolean[a.size()];
        boolean[] colArr = new boolean[a.get(0).size()];

        for(int i = 0; i < a.size(); i++) {
            for(int j = 0; j < a.get(0).size(); j++) {
                if(a.get(i).get(j) == 0) {
                    rowArr[i] = true;
                    colArr[j] = true;
                }
            }
        }

        for(int i = 0; i < a.size(); i++) {
            for(int j = 0; j < a.get(0).size(); j++) {
                if(rowArr[i]) {
                    for(int k = 0; k < a.get(0).size(); k++) {
                        a.get(i).set(k, 0);
                    }
                    rowArr[i] = false;
                }

                if(colArr[j]) {
                    for(int k = 0; k < a.size(); k++) {
                        a.get(k).set(j, 0);
                    }
                    colArr[j] = false;
                }
            }
        }
    }
}


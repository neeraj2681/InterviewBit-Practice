

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

**Note:**<br>
1. The replacement must be in-place, do **not** allocate extra memory.
2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.

<b><u>Input Format:</u></b><br>
The first and the only argument of input has an array of integers, A.

<b><u>Output Format:</u></b><br>
Return an array of integers, representing the next permutation of the given array.

<b><u>Constraints:</u></b><br>
<code>1 <= N <= 5e5<br>
1 <= A[i] <= 1e9</code>

**Examples:**<br>
<code>Input 1:<br>
    A = [1, 2, 3]<br><br>
Output 1:<br>
    [1, 3, 2]<br><br><br>
Input 2:<br>
    A = [3, 2, 1]<br><br>
Output 2:<br>
    [1, 2, 3]<br><br><br>
Input 3:<br>
    A = [1, 1, 5]<br><br>
Output 3:<br>
    [1, 5, 1]<br><br><br>
Input 4:<br>
    A = [20, 50, 113]<br><br>
Output 4:<br>
    [20, 113, 50]<br><br><br>
</code>
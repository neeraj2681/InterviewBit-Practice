Find the contiguous subarray within an array, A of length N which has the largest sum.

<b>Input Format:</B>

<code>The first and the only argument contains an integer array, A.</code><br><br>
<b>Output Format:</b>

Return an integer representing the maximum possible sum of the contiguous subarray.
<br><br><b>Constraints:</b>

<code>1 <= N <= 1e6
-1000 <= A[i] <= 1000</code><br><br>
<b>For example:</b>

Input 1:<br>
    <code>A = [1, 2, 3, 4, -10]</code>

Output 1:<br>
    <code>10</code>

Explanation 1:<br>
    <code>The subarray [1, 2, 3, 4] has the maximum possible sum of 10.</code>

Input 2:<br>
    <code>A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]</code>

Output 2:<br>
    <code>6</code>

Explanation 2:<br>
    <code>The subarray [4,-1,2,1] has the maximum possible sum of 6.</code>
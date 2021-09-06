

Given a matrix, A of size M x N of 0s and 1s.<br> If an element is 0, set its entire row and column to 0.

<b>Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.</b>


<b>Input Format:</b><br>
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.

<b>Output Format:</b><br>
Return a 2-d matrix that satisfies the given conditions.

<b>Constraints:</b><br>
<code>1 <= N, M <= 1000<br>
0 <= A[i][j] <= 1</code>

<b>Examples:</b><br>
<code>Input 1:<br>
    [   [1, 0, 1],<br>
        [1, 1, 1], <br>
        [1, 1, 1]   ]<br><br>
Output 1:<br>
    [   [0, 0, 0],<br>
        [1, 0, 1],<br>
        [1, 0, 1]   ]<br><br>
Input 2:<br>
    [   [1, 0, 1],<br>
        [1, 1, 1],<br>
        [1, 0, 1]   ]<br><br>
Output 2:<br>
    [   [0, 0, 0],<br>
        [1, 0, 1],<br>
        [0, 0, 0]   ]<br><br>

</code>
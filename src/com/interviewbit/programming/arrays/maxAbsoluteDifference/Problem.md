

You are given an array of <code>N</code> integers, <code>A1, A2 ,…, AN</code>.<br> Return maximum value of <code>f(i, j)</code> for all <code>1 ≤ i, j ≤ N</code>.<br>
<code>f(i, j)</code> is defined as <code>|A[i] - A[j]| + |i - j|</code>, where <code>|x|</code> denotes absolute value of <code>x</code>.

For example,<br>
<code>A=[1, 3, -1]<br><br>
f(1, 1) = f(2, 2) = f(3, 3) = 0<br>
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3<br>
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4<br>
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5<br></code>
<br>So, we return 5.


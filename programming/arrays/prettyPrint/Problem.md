Print concentric rectangular pattern in a 2d matrix.<br>
Let us show you some examples to clarify what we mean.<br><br>
<b>Example 1:</b><br>
<b>Input:</b><br> <code>A = 4</code><br><br>
<b>Output:</b><br>
<code>4 4 4 4 4 4 4<br> 
4 3 3 3 3 3 4 <br>
4 3 2 2 2 3 4 <br>
4 3 2 1 2 3 4 <br>
4 3 2 2 2 3 4 <br>
4 3 3 3 3 3 4 <br>
4 4 4 4 4 4 4</code> <br><br>
<b>Example 2:</b><br>
<b>Input:</b><br> <code>A = 3</code><br><br>
<b>Output:</b><br>
<code>3 3 3 3 3 <br>
3 2 2 2 3 <br>
3 2 1 2 3 <br>
3 2 2 2 3 <br>
3 3 3 3 3</code> <br><br>
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.<br><br>
You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

<b>Input</b><br>
Only argument given is string S.<br>

<b>Output</b><br>
Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
<br><br><b>Constraints</b><br>
1 <= length(S) <= 1e6
S can have special characters
<br><br><b>Example</b>

<i>Input</i><br>
    <code>ABEC</code>

<i>Output</i><br>
    <code>6</code>

<b>Explanation</b><br>
	<code>Amazing substrings of given string are :<br>
	1. A<br>
	2. AB<br>
	3. ABE<br>
	4. ABEC<br>
	5. E<br>
	6. EC<br>
	here number of substrings are 6 and 6 % 10003 = 6.</code>
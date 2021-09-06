Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

<b>For Example</b><br> <code>longest common prefix of <b>"abcdefgh"</b> and <b>"abcefgh"</b> is "abc".</code>

<code><b>Input Format</b><br>
The only argument given is an array of strings A.<br><br>
<b>Output Format</b><br>
Return longest common prefix of all strings in A.</code><br><br>
<b>For Example</b><br>
<code><b>Input 1:</b><br>
    A = ["abcdefgh", "aefghijk", "abcefgh"]<br><br>
<b>Output 1:</b><br>
    "a"<br><br>
    <b>Explanation 1:</b>
        Longest common prefix of all the strings is "a".<br>

<b>Input 2:</b><br>
    A = ["abab", "ab", "abcd"];<br><br>
<b>Output 2:</b><br>
    "ab"<br><br>
    <b>Explanation 2:</b><br>
        Longest common prefix of all the strings is "ab".</code>
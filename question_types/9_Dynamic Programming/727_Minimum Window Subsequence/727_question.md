727. Minimum Window Subsequence 

https://www.lintcode.com/problem/857/

Description
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the smallest starting index.

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
Example
Example 1:

Input：S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl"，T="u"
Output：""
Explanation： unable to match
Example 2:

Input：S = "abcdebdde"， T = "bde"
Output："bcde"
Explanation："bcde" is the answer and "deb" is not a smaller window because the elements of T in the window must occur in order.

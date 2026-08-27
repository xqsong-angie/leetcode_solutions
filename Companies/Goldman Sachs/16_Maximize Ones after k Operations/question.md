Given a binary string s consisting only of '0's and '1's, determine the maximum number of '1's that can be obtained after performing at most k operations.

In a single operation:

* Choose an index i such that 0 <= i < length(s) - 1.
* Update the character at position i as:
* s[i] = max(s[i], s[i + 1]).



**Note:**

* You may perform at most k operations.
* Each operation modifies only one position.
* The goal is to maximize the total count of '1's in the final string.

Return the maximum possible number of '1's after applying at most k operations.

**Example**
s = "10110"
k = 1

An optimal sequence of at most k operations:

| Operation Number | s before | Choosen Index (0-based) | s after |
| --- | --- | --- | --- |
| 1 | 10110 | Choose the index i = 1 | 1110 |

Hence, the maximum number of ones is 4.

**Constraints**

* 1 <= length of s <= 2 * 10^5
* 0 <= k <= length of s
* It is guaranteed that string s contains only '0's and '1's.

**Sample Case 0**

**Sample Input 0**
STDIN:
00011
2

FUNCTION:
s = "00011"
k = 2

**Sample Output 0**
4
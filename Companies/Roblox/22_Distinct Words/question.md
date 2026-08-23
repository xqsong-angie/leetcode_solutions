You are given a matrix of characters and an array of distinct strings `words`. Your task is to implement a simplified string search by determining the number of times in which strings from `words` can be found in the matrix under the following constraints:

* A string is found when it can be formed by combining characters along some path in the matrix.
* A path may start at any cell, and initially must go from left to right or from top to bottom.
* All paths are allowed to change direction once to go in the opposite direction (i.e., from left -> right to right -> left, or from top -> bottom to bottom -> top).

Review the examples below for details.

*Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(matrix.length * matrix[0].length * words.length * max(words[i].length)) will fit within the execution time limit.*

---

**Example**

**Example 1:**

For

```text
matrix = [["a", "b", "a", "c"],
          ["x", "a", "c", "d"],
          ["y", "r", "d", "s"]]

```

and `words = ["ac", "cat", "car", "bar", "acdc", "abacaba"]`, the output should be `solution(matrix, words) = 7`.

Explanation:

* The string `"ac"` can be formed using characters along the paths:
* `matrix[0][2] -> matrix[0][3]`
* `matrix[0][2] -> matrix[1][2]`
* `matrix[1][1] -> matrix[1][2]`
so it is counted three times.


* The strings `"cat"` and `"car"` cannot be formed using the matrix characters under the described constraints.
* The string `"bar"` can be formed using characters along the path `matrix[0][1] -> matrix[1][1] -> matrix[2][1]`.
* The string `"acdc"` can be formed using characters along the paths:
* `matrix[0][2] -> matrix[1][2] -> matrix[2][2] -> matrix[1][2]`
* `matrix[1][1] -> matrix[1][2] -> matrix[1][3] -> matrix[1][2]`
so it is counted twice.


* The string `"abacaba"` can be formed using characters along the path:
* `matrix[0][0] -> matrix[0][1] -> matrix[0][2] -> matrix[0][3] -> matrix[0][2] -> matrix[0][1] -> matrix[0][0]`


* Thus, the final answer is `3 + 1 + 2 + 1 = 7`.

**Example 2:**

For

```text
matrix = [["a", "a", "a"],
          ["a", "a", "a"]]

```

and `words = ["aaaa"]`, the output should be `solution(matrix, words) = 4`.

Explanation:

* The string `"aaaa"` can be formed using characters along four distinct paths:
* `matrix[0][0] -> matrix[0][1] -> matrix[0][2] -> matrix[0][1]`
* `matrix[0][1] -> matrix[0][2] -> matrix[0][1] -> matrix[0][0]`
* `matrix[1][0] -> matrix[1][1] -> matrix[1][2] -> matrix[1][1]`
* `matrix[1][1] -> matrix[1][2] -> matrix[1][1] -> matrix[1][0]`



---

**Input/Output**

* **[execution time limit] 3 seconds (java)**
* **[memory limit] 1 GB**
* **[input] array.array.char matrix**
A matrix of characters. It is guaranteed that the characters in the matrix are all lowercase English letters.
*Guaranteed constraints:*
`1 <= matrix.length <= 20`
`1 <= matrix[i].length <= 20`
* **[input] array.string words**
An array of distinct strings. It is guaranteed that all strings consist of lowercase English letters.
*Guaranteed constraints:*
`1 <= words.length <= 50`
`1 <= words[i].length <= 50`
* **[output] integer**
The number of times that strings within `words` that can be found in the matrix under the described constraints.
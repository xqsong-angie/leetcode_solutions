Given two arrays of integers `a` and `b` of the same length, find the number of pairs `(i, j)` such that `i <= j` and `a[i] - b[j] = a[j] - b[i]`.

**Example**

* For `a = [2, -2, 5, 3]` and `b = [1, 5, -1, 1]`, the output should be `solution(a, b) = 6`.
* For `(i, j) = (0, 0)` equality holds: `a[0] - b[0] = 2 - 1 = 1` and `a[0] - b[0] = 2 - 1 = 1`,
* For `(i, j) = (0, 1)` equality holds: `a[0] - b[1] = 2 - 5 = -3` and `a[1] - b[0] = (-2) - 1 = -3`,
* For `(i, j) = (0, 2)` equality doesn't hold: `a[0] - b[2] = 2 - (-1) = 3` and `a[2] - b[0] = 5 - 1 = 4`,
* For `(i, j) = (0, 3)` equality doesn't hold: `a[0] - b[3] = 2 - 1 = 1` and `a[3] - b[0] = 3 - 1 = 2`,
* For `(i, j) = (1, 1)` equality holds: `a[1] - b[1] = (-2) - 5 = -7` and `a[1] - b[1] = (-2) - 5 = -7`,
* For `(i, j) = (1, 2)` equality doesn't hold: `a[1] - b[2] = (-2) - (-1) = -1` and `a[2] - b[1] = 5 - 5 = 0`,
* For `(i, j) = (1, 3)` equality doesn't hold: `a[1] - b[3] = -2 - 1 = -3` and `a[3] - b[1] = 3 - 5 = -2`,
* For `(i, j) = (2, 2)` equality holds: `a[2] - b[2] = 5 - (-1) = 6` and `a[2] - b[2] = 5 - (-1) = 6`,
* For `(i, j) = (2, 3)` equality holds: `a[2] - b[3] = 5 - 1 = 4` and `a[3] - b[2] = 3 - (-1) = 4`,
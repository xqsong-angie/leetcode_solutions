For a grid of black and white cells with `rows` rows and `cols` columns, you're given an array `black` that contains the `[row, column]` coordinates of all the black cells in the grid.

Your task is to compute how many $2 \times 2$ submatrices of the grid contain exactly `blackCount` black cells, for each $0 \le \text{blackCount} \le 4$. As a result, you will return an array of 5 integers, where the $i^{\text{th}}$ element is the number of $2 \times 2$ submatrices with exactly $i$ black cells.

It is guaranteed that black cell coordinates in the `black` array are pairwise unique, so the same cell is not colored twice.

---

**Example**

* For `rows = 3`, `cols = 3`, and `black = [[0, 0], [0, 1], [1, 0]]`, the output should be `solution(rows, cols, black) = [1, 2, 0, 1, 0]`.
▼ Expand to see the example video.
$$\begin{bmatrix}   1 & 1 & 0 \\   1 & 0 & 0 \\   0 & 0 & 0   \end{bmatrix} = \text{grid}$$


`# black cells in the 2x2 submatrix:` 1
$$\begin{bmatrix}   0 & 1 & 2 & 3 & 4 \\   0 & 2 & 0 & 1 & 0   \end{bmatrix} = \text{result}$$


*Note: If you are not able to see the video, use this link to access it.*
* Initially, `result = [0, 0, 0, 0, 0]`.
* The $2 \times 2$ submatrix with the upper-left corner at `(0, 0)` contains 3 black cells. `result = [0, 0, 0, 1, 0]`.
* The $2 \times 2$ submatrix with the upper-left corner at `(0, 1)` contains 1 black cell. `result = [0, 1, 0, 1, 0]`.
* The $2 \times 2$ submatrix with the upper-left corner at `(1, 0)` contains 1 black cell. `result = [0, 2, 0, 1, 0]`.
* The $2 \times 2$ submatrix with the upper-left corner at `(1, 1)` contains 0 black cells. `result = [1, 2, 0, 1, 0]`.
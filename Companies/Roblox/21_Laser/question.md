Imagine a board of size numRows x numColumns with some lasers placed on it. These lasers are placed at coordinates specified in the two-dimensional array laserCoordinates, where laserCoordinates[i] is a two-element array containing coordinates for the center of the i-th laser. Lasers with a center in a cell (row, column) destroy everything in the same row (i.e., rows with index row) and the same column (i.e., columns with index column).

Now imagine there is a robot at coordinates (curRow, curColumn). The robot can only move in a straight line, either left, right, up, or down within this board. Your task is to count the maximum number of cells that the robot can safely move through (in any direction) before being destroyed by lasers.

Note: You can assume that the initial cell is protected, and lasers cannot destroy the robot there even if they cover this cell in their destruction area.

**Example**

For numRows = 8, numColumns = 8, curRow = 5, curColumn = 3, and laserCoordinates = [[1, 6], [2, 8]], the output should be solution(numRows, numColumns, curRow, curColumn, laserCoordinates) = 3.

Explanation:

```text
XXXXXLXX
XXXXXXXL
.....X.X
.....X.X
..o..X.X
..v..X.X
..v..X.X
..v..X.X

```
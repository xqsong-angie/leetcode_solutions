Given a matrix of integers, with each element containing either 0, 1, or 2, your task is to find the longest diagonal segment which matches the following pattern: 1, 2, 0, 2, 0, 2, 0, ... (where the first element is 1, and then 2 and 0 are repeating infinitely), and finishes at a matrix border. Return the length of this diagonal segment.

The diagonal segment:

* May start at any matrix element
* May go toward any possible diagonal direction
* Must end at an element in the first or last row or column

See the example videos below.

*Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(matrix.length² · matrix[0].length²) will fit within the execution time limit.*

**Example**

* For

```text
matrix = [[0, 0, 1, 2],
          [0, 2, 2, 2],
          [2, 1, 0, 1]]

```

the output should be `solution(matrix) = 3`.

▼ Expand to see the example video.

```text
[ 0  0  1  2 ]
[ 0  2  2  2 ]
[ 2  1  0  1 ]

```
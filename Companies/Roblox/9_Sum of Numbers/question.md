1. Given a rectangular matrix `matrix` and an integer `frameSize`, consider the outer frames of all `frameSize` x `frameSize` contiguous square submatrices of `matrix`. Your task is the following:

* Calculate the sum of all numbers located on the frame of each `frameSize` x `frameSize` submatrix.
* Determine the maximum of all these sums.
* Considering only these frames with the maximum sum, find all the distinct numbers that appear in at least one of the frames. Each integer from these square frames should be calculated only once.
* Return the sum of these distinct numbers.

Note: A `frameSize` x `frameSize` square frame contains $\max(1, 4 \times (\text{frameSize} - 1))$ cells. See the frames for some of the values of `frameSize` below for better understanding.
frameSize = 1
frameSize = 3
frameSize = 5

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than $O(\text{matrix.length} \cdot \text{matrix[0].length})$ will fit within the execution time limit.

Example

For

```text
matrix = [[9, 7, 8, 9, 2],
          [6, 9, 9, 6, 1],
          [4, 10, 1, 3, 10],
          [18, 2, 3, 9, 3],
          [4, 6, 8, 5, 21]]

```
**Spiral Order Primes**

Lauren gave George a grid and wants him to traverse the grid in spiral order. To check whether George is doing it correctly, Lauren asked him to report all the primes as they are encountered. Help George to find these primes while traversing the grid in spiral order.

For example, grid = [[7, 7, 3, 8, 1], [13, 5, 4, 5, 2], [9, 2, 12, 3, 9], [6, 12, 1, 11, 41]] with the number of rows, n = 4, and the number of columns, m = 5. Traversal is as follows:

```
 7   7   3   8   1
13   5   4   5   2
 9   2  12   3   9
 6  12   1  11  41

```

The traversal order is: [7, 7, 3, 8, 1, 2, 9, 41, 11, 1, 12, 6, 9, 13, 5, 4, 5, 3, 12, 2] and primes as encountered in the traversal are [7, 7, 3, 2, 41, 11, 13, 5, 5, 3, 2]. Note that 1 is not a prime number.

**Function Description**
Complete the function spiralOrderPrimes in the editor below. The function must return an array of integers that denote the primes in the grid in the spiral order traversal. Spirals start from top-left.

spiralOrderPrimes has the following parameter(s):

* grid[grid[0][0]....grid[n-1][m-1]]: a 2D array of integers
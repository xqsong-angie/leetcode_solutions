**1. GoodArray**

For a number N, a goodArray is the smallest possible array that consists of only powers of two (2^0, 2^1 ... 2^k) such that the sum of all the numbers in the array is equal to N.

For each query that consists of three integers l, r, and m, find out the product of elements goodArray[l] through goodArray[r] modulo m when goodArray is sorted in non-decreasing order.

**Example**
For N = 26, queries = [[1, 2, 1009], [3, 3, 5]]

goodArray when sorted is [2, 8, 16].

For query l = 1, r = 2, m = 1009, ans = goodArray[1] * goodArray[2] = (2 * 8) modulo 1009 = 16.
For query l = 3, r = 3, m = 5, ans = goodArray[3] = (16) modulo 5 = 1.

The answer is [16, 1].

**Function Description**
Complete the function getQueryResults in the editor below.

getQueryResults has the following parameters:

* long N: the integer N
* int queries[q][3]: a 2D array of queries, each with 3 elements l, r, and m.

**Return**

* int answer[q]: the answers to the queries

**Constraints**

* 1 <= N <= 10^18
* 1 <= q <= 10^5
* 1 <= m <= 10^5
* 1 <= l <= r <= |goodArray|, where |goodArray| denotes the length of the array

---

**Sample Case 0**

**Sample Input For Custom Testing**
STDIN:
6
3
3
1 2 4
2 2 8
1 1 4

FUNCTION:
N = 6
q = 3
q[] size = 3
queries = [[1,2,4], [2,2,8], [1,1,4]]

**Sample Output**
0
4
2

**Explanation**
The sorted goodArray is [2, 4]. This is the smallest possible array in which every element is a power of 2, and the elements sum up to N = 6.

Query 1: l = 1, r = 2, m = 4; ans = goodArray[1] * goodArray[2] = (2 * 4) modulo 4 = 0.
Query 2: l = 2, r = 2, m = 8; ans = goodArray[2] = 4 modulo 8 = 4.
Query 3: l = 1, r = 1, m = 4; ans = goodArray[1] = 2 modulo 4 = 2.

---

**Sample Case 1**

**Sample Input For Custom Testing**
STDIN:
12
2
3
1 2 84
2 2 3

FUNCTION:
N = 12
q = 2
q[] size = 3
queries = [[1,2,84], [2,2,3]]

**Sample Output**
32
2

**Explanation**
The sorted goodArray is [4, 8].
Query 1: l = 1, r = 2, m = 84; ans = goodArray[1] * goodArray[2] = (4 * 8) modulo 84 = 32.
Query 2: l = 2, r = 2, m = 3; ans = goodArray[2] = 8 modulo 3 = 2.
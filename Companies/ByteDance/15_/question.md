Description

You are given two arrays of integers a and b, and an array queries, the elements of which are queries you are required to process. Every queries[i] can have one of the following two forms:

- [0, i, x]. In this case, you need to assign a[i] the value of x (a[i] = x).

- [1, x]. In this case, you need to find the total number of pairs of indices i and j such that a[i] + b[j] = x.

Perform the given queries in order and return an array containing the results of the queries of the type [1, x].


Example

- For a = [3, 4], b = [1, 2, 3], and queries = [[1, 5], [0, 0, 1], [1, 5]], the output should be solution(a, b, queries) = [2, 1].

  The arrays look like this initially:
  a = [3, 4] and b = [1, 2, 3]

  For the query [1, 5], there are two ways to form a sum of 5 using an element from each array: 5 = 3 + 2 = a[0] + b[1] and 5 = 4 + 1 = a[1] + b[0]. So the result is 2.

  The query [0, 0, 1] re-assigns the value of a[0] to 1, so the arrays now look like this:
  a = [1, 4] and b = [1, 2, 3]

  For the final [1, 5] query, there's now only one way to form a sum of 5 using an element from each array: 5 = 4 + 1 = a[1] + b[0]. So the result is 1.

  Since the two queries of type [1, x] gave results of 2 and 1 respectively, the answer is [2, 1].

- For a = [2, 3], b = [1, 2, 2], and queries = [[1, 4], [0, 0, 3], [1, 5]], the output should be solution(a, b, queries) = [3, 4].

  The arrays look like this initially:
  a = [2, 3] and b = [1, 2, 2]

  For the query [1, 4], there are three ways to form a sum of 4 using an element from each array: 4 = 2 + 2 = a[0] + b[1], 4 = 2 + 2 = a[0] + b[2], and 4 = 3 + 1 = ...
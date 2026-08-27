Given two integer arrays arr1 and arr2, for each element in arr1, find the index of the first element in arr2 that is strictly greater than it. If no such element exists in arr2, the result for that element should be -1.

Return an array of integers representing the index of the first element in arr2 strictly greater than each corresponding element in arr1.

Example 1:

Input: arr1 = [2, 4, 3], arr2 = [1, 3, 5, 2]

Output: [1, 2, 1]

Explanation:

For arr1[0] = 2: The first element in arr2 greater than 2 is 3 at index 1.

For arr1[1] = 4: The first element in arr2 greater than 4 is 5 at index 2.

For arr1[2] = 3: The first element in arr2 greater than 3 is 5 at index 2.

Constraints:

1 <= arr1.length, arr2.length <= 2 * 10^5

1 <= arr1[i], arr2[i] <= 10^9
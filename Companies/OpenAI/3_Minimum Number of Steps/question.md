Minimum Steps to Reach Target Number via Modular Addition

Description:
You are given an array of integers nums, an integer start, an integer target, and a modulus value N.

You start at the integer start. In each step, you can select any integer x from the array nums and move to a new number calculated as:
(current_number + x) % N

Return the minimum number of steps required to reach the target number. If it is impossible to reach target from start, return -1.

Example 1:
Input: nums = [2, 5], start = 0, target = 7, N = 10
Output: 2
Explanation:

* Step 1: Choose 2. New value = (0 + 2) % 10 = 2.
* Step 2: Choose 5. New value = (2 + 5) % 10 = 7.
* Minimum steps taken: 2.

Example 2:
Input: nums = [3, 6], start = 1, target = 2, N = 9
Output: -1
Explanation:

* Starting from 1 with operations (+3) % 9 or (+6) % 9, the reachable states are only 1, 4, and 7.
* Target value 2 can never be reached, so return -1.

Constraints:

* 1 <= nums.length <= 10^3
* 1 <= nums[i] <= 10^9
* 2 <= N <= 10^5
* 0 <= start, target < N
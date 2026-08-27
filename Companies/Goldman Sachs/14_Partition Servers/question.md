Given an array of integers difficulty representing the difficulty levels of several tasks, you need to partition these tasks into three non-empty servers (i.e., every server must get at least one task).

After partitioning:

An adversary (or algorithm) will choose one task from each server—let their difficulties be d1, d2, and d3 respectively—to minimize the cost function:
Cost = |d1 - d2| + |d2 - d3|

Your goal as the system designer is to partition the tasks into the three servers such that this minimum possible cost is maximized.

Return the maximum possible minimum cost value that can be achieved.

Example 1:

Input: difficulty = [1, 5, 8, 12, 15]

Output: 7

Explanation:

If sorted: [1, 5, 8, 12, 15].

One optimal strategy is to assign tasks to 3 servers such that the minimum difference between chosen elements from 3 servers is maximized.

Notice that |d1 - d2| + |d2 - d3| for three values (where d2 is between d1 and d3) simplifies to max(d1, d2, d3) - min(d1, d2, d3).

Constraints:

3 <= difficulty.length <= 2 * 10^5

1 <= difficulty[i] <= 10^9
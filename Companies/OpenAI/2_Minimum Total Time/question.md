Minimum Time to Visit All Task Nodes in a Tree

Description:
You are given an undirected, unweighted tree with n nodes labeled from 0 to n - 1. The tree structure is given as a 2D integer array edges of size n - 1, where edges[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i.

You are also given:

* An integer startNode representing your starting location.
* An integer endNode representing your required final location.
* An integer array tasks containing the labels of all nodes that must be visited at least once.

Traveling along any edge takes 1 unit of time.

Return the minimum total time required to start at startNode, visit all nodes specified in tasks in any order, and finish at endNode.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], startNode = 0, endNode = 4, tasks = [3, 5]
Output: 6
Explanation:

* The minimal subtree that connects startNode (0), endNode (4), and all task nodes (3, 5) consists of the edges: (0,1), (0,2), (1,3), (1,4), and (2,5). The total number of edges in this subtree is 5.
* An optimal traversal route is: 0 -> 2 -> 5 -> 2 -> 0 -> 1 -> 3 -> 1 -> 4.
* Total time = 2 * (subtree edges) - distance(startNode, endNode) = 2 * 5 - 4 = 6.

Example 2:
Input: n = 4, edges = [[0,1],[1,2],[2,3]], startNode = 0, endNode = 3, tasks = [1, 2]
Output: 3
Explanation:

* All task nodes lie directly on the path from startNode (0) to endNode (3).
* No backtracking is necessary.
* Total time = distance(startNode, endNode) = 3.

Constraints:

* 1 <= n <= 10^5
* edges.length == n - 1
* edges[i].length == 2
* 0 <= u_i, v_i < n
* u_i != v_i
* The given edges form a valid tree.
* 0 <= startNode, endNode < n
* 1 <= tasks.length <= n
* 0 <= tasks[i] < n
* All values in tasks are unique.
6. Equalize Server Latency

TikTok's server network is structured as a perfect binary tree with n servers, where servers are numbered from 0 to n-1. Each server is connected to its parent with the following configuration:

- The parent of server i is server floor((i-1)/2), for i >= 1. Here, floor(x) denotes the greatest integer less than equal to x.
- The children of server i are the servers numbered 2*i + 1 and 2*i + 2, if they exist.
- The root server (server 0) has no parent.

The root server (server 0) handles requests, which are passed down to its child servers.

- The latency cost between server i and its parent is defined as the time taken for data to travel along the edge between them and is given by latency[i-1] for i >= 1.
- The latency from the root server to any leaf server is the sum of the latencies along the path from the root to that leaf.

The goal is to ensure that the latency from the root to every leaf server is the same. Currently, latencies along different paths may vary. You are allowed to increase the latency of some connections but cannot decrease any latency. You have to find the minimum amount of additional latency needed to equalize the latency from the root to all leaf servers.


Example

Suppose n = 7 and latency = [3, 1, 2, 1, 5, 4]
The given arrangement should look like this:

       0
     3/ \1
     1   2
   2/ \1 5/ \4
   3   4 5   6

We can increment the latencies as follows:

- Incrementing edge latency[0] by 1. (Connecting nodes 0 and 1)
- Incrementing edge latency[3] by 1. (Connecting nodes 1 and 4)
- Incrementing edge latency[5] by 1. (Connecting nodes 2 and 6)

After making the above increments, the cost from the root node to each leaf node is equal to 6.
Since we have made a total of 3 increments, hence the answer is 3. It can be shown that the answer cannot be less than 3.


Function Description

Complete the function minAdditionalLatency in the editor below.

minAdditionalLatency has the following parameters:
  n: an integer denoting the number of servers in the network.
  latency[n-1]: an integer array of size n - 1

Returns
  long int: The minimum total increment in latency required to make the latency from the root node to each leaf node equal.


Constraints

- 3 <= n <= 2^17 - 1
- 1 <= latency[i] <= 10^9
- It is guaranteed that n corresponds to a perfect binary tree


Input Format For Custom Testing

The first line contains an integer, n, denoting the number of servers in the network.
The next line contains an integer, m (= n - 1), denoting the number of edges in the tree.
Each line i of the m subsequent lines (where 0 <= i < m) contains an integer denoting the elements of the latency[i] array.


Sample Case 0

Sample Input For Custom Testing

STDIN       FUNCTION
-----       --------
3     ->    n = 3
2     ->    m = n - 1 = 2
10    ->    latency = [10, 5]
5

Sample Output
5

Explanation
Here, n = 3, latency = [10, 5].
The given arrangement should look as:

     0
   10/ \5
    1   2

Considering 0-based indexing, we can increment the latency for the connection between servers 0 and 2 by 5. After making the increment the distance from the root server to each leaf server will be equal to 10. Since we have made a total of increment of 5, hence the answer is 5. It can be shown that the answer cannot be less than 5.


Sample Case 1

Sample Input For Custom Testing

STDIN       FUNCTION
-----       --------
7     ->    n = 7
6     ->    m = n - 1 = 6
5     ->    latency = [5, 5, 2, 2, 2, 2]
5
2
2
2
2

Sample Output
0

Explanation
Here, n = 7, latency = [5, 5, 2, 2, 2, 2].
The given arrangement should look as:

       0
     5/ \5
     1   2
   2/ \2 2/ \2
   3   4 5   6

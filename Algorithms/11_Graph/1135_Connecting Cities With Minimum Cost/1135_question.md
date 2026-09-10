1135. Connecting Cities With Minimum Cost

https://www.lintcode.com/problem/3672/

Description
There are n cities in this question, and their numbers range from 1 to n.

At the same time, there is a connections array and 
c
o
n
n
e
c
t
i
o
n
s
[
i
]
=
[
a
i
,
b
i
,
c
i
]
connections[i]=[a 
i
​
 ,b 
i
​
 ,c 
i
​
 ], which means that the cost of connecting cities 
a
i
a 
i
​
  and 
b
i
b 
i
​
  is 
c
i
c 
i
​
 .

Please return the minimum cost required to connect all cities. If all cities cannot be connected, return -1.

Example
Example 1

Input:

3
[[1,2,1], [2,3,2], [1,3,3]]
Ouput:

3
Explanation:

Choose [1,2,1] and [2,3,2] to connect all n cities. At this time, the cost is the least, which is 3.

Example 2

Input:

3
[[1,2,1]]
Output:

-1
Explanation:

Unable to connect all cities according to connections.


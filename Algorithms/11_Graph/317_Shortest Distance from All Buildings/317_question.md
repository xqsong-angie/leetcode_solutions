317. Shortest Distance from All Buildings

https://www.lintcode.com/problem/803/

Description
You want to build a house on an empty, two-dimensional, 
m
×
n
m×n grid grid and reach all the buildings in the shortest distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
There will be at least one building

1
≤
m
,
n
≤
50
1≤m,n≤50

g
r
i
d
[
i
]
[
j
]
=
0
,
1
,
2
grid[i][j]=0,1,2

If it is not possible to build such house according to the above rules, return -1

Example
Example 1

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation:
In this example, there are three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
Example 2

Input: [[1,0],[0,0]]
Output: 1
In this example, there is one buildings at (0,0).
1 - 0
|   |
0 - 0
The point (1,0) or (0,1) is an ideal empty land to build a house, as the total travel distance of 1 is minimal. So return 1.
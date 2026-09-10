The assistant sales manager in the head office of the company 'Jotuway' receives lists of sales data from the regional offices scattered around the country. The assistant sales manager must compile the data and submit the list to the sales manager. The compiled list should be the longest palindromic list of sales data from the regional offices. He/she can add together any two consecutive elements of a list to form a single element. The result thus obtained can be reused further and this process can be repeated any number of times to convert the given list into a palindromic list of maximum length.

Write an algorithm to help the assistant sales manager convert the given list into a palindromic list of maximum length.

Input
The first line of the input consists of an integer num, representing the number of elements in the list (N).
The second line consists of N space-separated positive integers, salesData[0], salesData[1],........, salesData[N-1], representing the sales data.

Output
Print the space-separated positive integers representing the palindromic list of maximum length.

Constraints
0 ≤ num ≤ 10^3
1 ≤ salesData[i] ≤ 10^6
0 ≤ i < num

Example
Input:
6
15 10 15 34 25 15

Output:
15 25 34 25 15

Explanation:
The given list [15 10 15 34 25 15] can be converted into a palindromic list [15 25 34 25 15] by combining 10 and 15 at index 2 and index 3, respectively, to create 25 at index 2.
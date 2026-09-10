Bob has to send a secret code S to his boss. He designs a method to encrypt the code using two key values N and M. The formula that he uses to develop the encrypted code is shown below:

(((S^N % 10)^M) % 1000000007)

Write an algorithm to help Bob encrypt the code.

Input
The input consists of an integer secretCode, representing the secret code (S).
The second line consists of an integer firstKey, representing the first key value (N).
The third line consists of an integer secondKey, representing the second key value (M).

Output
Print an integer representing the code encrypted by Bob.

Constraints
1 ≤ secretCode ≤ 10^9
0 ≤ firstKey, secondKey ≤ 1000000007

Example
Input:
2
3
4

Output:
4096

Explanation:
S = 2, N = 3, M = 4 and the formula of the encrypted code is:
(((S^N % 10)^M) % 1000000007)
(((2^3 % 10)^4) % 1000000007) = 4096
So, the output is 4096.
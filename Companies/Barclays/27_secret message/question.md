An agent sends a secret message containing the details of his project as a soft copy to the company's computer (P) and as a hard copy by fax to Roger, the technical head of the company (Q). But during the transmission, due to some noise in the network, some of the bits of the message P get distorted. However, we know that Roger always matches the binary values of both the messages and checks whether he can convert the message P to message Q by flipping the minimum number of bits.
Write an algorithm to help Roger find the minimum number of bits required to be flipped to convert message P to message Q.

Input
The input consists of two space-separated integers - num1 and num2, representing the secret message sent to the company's computer (P) and to the technical head of the company (Q), respectively.

Output
Print an integer representing the minimum number of bits required to be flipped to convert message P to message Q.

Constraints
0 ≤ num1, num2 ≤ 10^9

Example
Input:
7 10

Output:
3

Explanation:
Binary representation of P is 00000111
Binary representation of Q is 00001010
We need to flip three bits of P at position 5, 6 and 8.
So, the number of bits flipped is 3.
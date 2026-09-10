Question

The manager of the grocery company tagGrocery wishes to identify which products are most frequently purchased by the customers. He selects N customers that purchase combo bags of products. Each combo bag consists of M products and each product is labeled with a productID. He needs to find the productIDs of the products that are purchased by all the N customers in common.

Write an algorithm to help the manager find the lexicographically sorted productIDs of the products that are most frequently purchased by all the N customers.

Input
The first line of the input consists of two space-separated integers - customers and products, representing the number of customers selected by the manager (N) and the number of products in the bag of the customer (M), respectively.
Next N lines consist of M space-separated integers - tag[0], tag[1], ........, tag[M-1], representing the productIDs of the products that are present in the combo bag of each customer.

Output
Print space-separated integers representing the lexicographically sorted productIDs of the products that are most frequently purchased by all the N customers.

Constraints
1 ≤ customers, products ≤ 10^3
0 ≤ tag[i] ≤ 10^9
0 ≤ i ≤ products -1

Example
Input:
4 4
8 2 3 2
2 3 4 8
8 3 11 12
2 3 6 8

Output:
3 8
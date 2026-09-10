A distributor distributes energy drinks in a 34 oz can to the customer where every customer has an ID associated with them. He distributes the drink according to the demand of the drink. He has developed a system that handles all the transaction queries of the store. The system will handle two types of queries i.e. query 1 and query 2. Query 1 updates the quantity of the drink purchased by a customer where if there is already an entry for the given ID, then the total amount of drink purchased by the customer is updated by adding the new quantity to the previous one. Query 2 retrieves the quantity of cans purchased by the given range of the customer ID. At the end of the day, the distributor has to share a report for all the type 2 queries.
Write an algorithm to help the distributor find the answer for all the type 2 queries.

Input
The first line of the input consists of two space-separated integers C and Q, representing the number of customers and the number of queries respectively.
The next Q lines consist of three space-separated integers, where the first integer represents the type of the query and can only be 1 or 2. If the first integer is 1 then it is a type 1 query and the second and third integers represent the customer ID and the quantity of drink purchased respectively. If the first integer is 2, then it is a type 2 query and the second and the third integers represent the starting and ending customer ID range (both inclusive).

Output
Print space-separated integers representing the answers to all the type 2 queries.

Constraints
0 ≤ C ≤ 10^5
0 ≤ Q ≤ 10^5

Example
Input:
4 5
1 3 12
2 0 2
1 1 4
1 3 2
2 2 4

Output:
[0,18]

Explanation:
12 drinks have been distributed to the customer with ID 3, therefore, the total drink distributed from the ID range 0-2 is 0.
4 and 2 are the drinks distributed to the customers with ID 1 and 3 respectively, therefore the total drink distributed from the ID range 2-4 is 18.
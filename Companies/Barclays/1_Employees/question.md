Question

In an organization, N employees with employee IDs from 1 to N, are working in different teams. Each employee shares a bond of great understanding with his/her fellow team members. Each employee is assigned an integer X that represents the employee's efficiency. The sum of efficiencies of all the employees indicates the reputation of the organization.

Edwin is appointed manager of the organization for Q days. Edwin, being short-tempered, fires one employee each day. Because the team members have a close relationship, K colleagues of the fired employee resign in protest. (These K colleagues have the least efficiency of the remaining team members.)

Kevin is the head of the database management system and has to update the reputation of the organization at the end of each day. Write an algorithm to help him determine the reputation of the organization at the end of each day for Q number of days.

Input
The first line of the input consists of an integer - num, representing the number of employees in the efficiency list (num is always equal to given number of employees N).
The second line consists of N space-separated integers - eff0, eff1, .......effN-1, representing the efficiency of the employees.
The third line consists of an integer - numT, representing the number of employees with a team ID (numT is always equal to given number of employees N).
The fourth line consists of N space-separated integers - idE0, idE1, .......idEN-1, representing the team ID of the employees.
The fifth line consists of two space-separated integers - numDays and numE, representing the number of days for which Edwin is manager of the organization (Q) and the number of elements in each Q lines (numE (P) is always equal to 2).
The last Q lines consist of P space-separated integers - idFire and numResign, representing the ID of the employee that was fired each day and the number of employees who resign along with the fired employee (K), respectively.

Output
Print Q space-separated integers representing the reputation of the organization at the end of each day.

Constraints
1 <= num <= 10^4
-10^9 <= eff0, eff1, .......effN-1 <= 10^9
1 <= idE0, idE1, .......idEM-1 <= numT
num = numT
1 <= numDays <= num
1 <= idFire <= num
0 <= numResign <= c; where c is the number of employees in the team on the current day

Note
The ID of a fired employee cannot be the ID of a person who has already resigned.

Example
Input:
5
1 2 3 4 5
5
1 2 1 1 2
2 2
3 2
2 0

Output:
7 5

Explanation:
There are two teams (ID's 1 and 2).
The initial reputation of the organization is 1 + 2 + 3 + 4 + 5 = 15.
At the end of day 1, employee 3 is fired. Employee 1 and employee 4 resign. The revised reputation is 7 (15 - 3 - 1 - 4).
At the end of day 2, employee 2 is fired but nobody resigns. The revised reputation is 5 (7 - 2).
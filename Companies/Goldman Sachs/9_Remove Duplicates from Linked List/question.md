Given a list of integers, remove any nodes that have values that have previously occurred in the list and return a reference to the head of the list.

For example, the following list has a recurrence of the value 3 initially:

**Linked List**
3 (head) -> 4 -> 3 -> 6 (tail)
*Redundant nodes are colored with the same color*

3 (head) -> 4 -> 6 (tail)
*Redundant nodes are removed after calling condense*

Remove the node at position 2 in the list above, 0 based indexing.

**Function Description**
Complete the function condense in the editor below. The function must return a reference to a LinkedListNode, the first node of a list that contains only the unique value nodes from the original list, in order.

condense has the following parameter(s):

* head: the head of a singly-linked list of integers, a LinkedListNode

**Note:** A LinkedListNode has two attributes: data, an integer, and next, a reference to the next item in the list or the language equivalent of null at the tail.

**Constraints**

* 1 <= n <= 10^5
* 0 <= LinkedListNode[i].val <= 1000

**Input Format for Custom Testing**

Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the size of the array list.
Each of the next n lines contains an integer list[i] where 0 <= i < n.

---

**Sample Case 0**

**Sample Input 0**

STDIN:
8
3
4
3
2
6
1
2
6

Function Parameters:
list[] Size n = 8
list[] = [ 3, 4, 3, 2, 6, 1, 2, 6 ]

**Sample Output 0**

3
4
2
6
1

**Explanation 0**
The list looks like this:

**Linked List**
3 (head) -> 4 -> 3 -> 2 -> 6 -> 1 -> 2 -> 6 (tail)
*Redundant nodes are colored with the same color*

3 (head) -> 4 -> 2 -> 6 -> 1 (tail)
*Redundant nodes are removed after calling condense*

From the first list in the diagram, remove:

* list[2] = 3
* list[6] = 2
* list[7] = 6
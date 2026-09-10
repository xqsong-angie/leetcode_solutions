Stephen runs a small library with "N" number of students as its members. All members have their unique studentID. The library has the certain number of books on "M" different subjects. Each student is given an individual assignment to complete by taking help from different books as per their requirement. The library has already issued some books to its members prior to this. The students can still issue required number of books from the library to complete their respective assignments. Each student submits the book issued to him/her in the library after completing their assignment. Only when the books have been submitted to the library can another student issue that book. Also, while assigning books Stephen starts assigning books to the student with the smallest studentID and proceed to the student with the higher studentID. Once he reaches to the student with the largest studentID then again goes back to the smallest studentID to whom the book was not assigned and follow the same process.
Stephen wants to find the sequence of studentIDs in which the students optimally complete their assignments.

Write an algorithm to help Stephen find the sequence of studentIDs in which the students optimally complete their assignments. If all students can't complete their assignment, output a list of length 1 with content -1.

Input
The first line of the input consists of two space-separated integers - num and subBooks representing the number of students (N) and different subjects, respectively (M).
The second line consists of N space-separated integers - avail[0], avail[1], ...., avail[N-1], representing the books available in the library that have not been issued to any student.
The next N lines consist of M space-separated integers representing the required books required by the students to complete their assignment.
The next N lines consist of M space-separated integers representing the books already issued to the students.

Output
Print space-separated integers representing the studentID in the order in which the students optimally complete their assignments. If all students can't complete their assignment, output a list of length 1 with content -1.

Constraints
1 ≤ num ≤ 100
1 ≤ subBooks ≤ 100

Example
Input:
3 3
2 2 3
2 4 0
0 0 1
0 1 3
3 5 4
1 3 4
2 3 5

Output:
2 0 1

Explanation:
The available Books =[2 2 3]
studentID  Issued Books  Required Books  Needs
0          2 4 0         3 5 4           1 1 4
1          0 0 1         1 3 4           1 3 3
2          0 1 3         2 3 5           2 2 2

The needs of the student with the studentID 2 can be fulfilled directly as he needs only 2, 2, 2 different books and the available books are 2, 2, 3. So, after the completion of his/her assignment, the books returned would be 0, 1, 3. Therefore, the books available in the library would be [2 2 3] + [0 1 3] = [2 3 6].

The students with the studentID 0 and 1 can complete their assignment with the books available in the library. However, since the preference is being given to the student with a smaller studentID, the assignment of the student with the studentID 0, would get completed before the student with the studentID 1. After the completion of the assignment of the student with the studentID 0, the books returned would be 2, 4, 0. So, the books available in the library would be [2 3 6] + [2 4 0] = [4 7 6].

Similarly, for the student with the studentID 1, the books returned would be 0, 0, 1. So, the books available in the library would be [4 7 6] + [0 0 1] = [4 7 7].

Therefore, the order in which the students optimally complete their assignments is [2, 0, 1].
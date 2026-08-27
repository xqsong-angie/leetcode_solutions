**Find the rank**

'n' Students of a class appear for number of exams. Each student appears for exactly k exams. The marks scored by a student in each exam is given. Now, the Teacher needs to identify the student with the nth Rank. Rank is the position in the sorted list of total marks, from high to low, maintaining order of students with equal total marks.

Given the initial order of the Student Marks and the required rank of the student, output the index of the chosen Student by the teacher. Take for example, given the data for n = 3 student as performance = [[79, 89, 15], [85, 89, 92], [71, 96, 88]] and the required position be rank = 2, the Student with index 2 is the answer. The total marks for each student in class are [183, 266, 255] respectively and the student with total score of 255 has a rank of 2.

**Function Description**
Complete the function findTheRank in the editor below. The function must return an integer, the index of the student at the required rank.

findTheRank has the following parameter(s):

* performance[performance[0]....performance[n-1][k-1]]: a 2D array of integers that denote the performance (marks) of n students in k exams
* rank: The required rank

**Constraints**

* 1 <= n <= 10
* 1 <= k <= 10
* 1 <= rank <= n
* 0 <= performance[i][j] <= 100 (where 0 <= i < n, 0 <= j < k)
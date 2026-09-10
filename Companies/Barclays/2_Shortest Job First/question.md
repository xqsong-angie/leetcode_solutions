Shortest Job First (SJF) is a system for scheduling task requests.

Each task request is characterized by its request time (i.e., the time at which the task is submitted to the system) and its duration time (i.e., the time needed to complete the task).

When the SJF system completes a task, it selects the task with the smallest duration to execute next. If multiple tasks have the same smallest duration, SJF selects the task with the earliest request time. The waiting time for a task is the difference between the request time and the actual start time (i.e., the time that it spends waiting for the system to execute it). You may assume that the tasks arrive in such frequency that the system executes tasks constantly and is never idle.

Given a list of request times and duration times, calculate the average task waiting time when scheduled using the Shortest Job First (SJF) algorithm.

Input
The first line of input consists of a positive integer - req_size, representing the number of tasks (N).
The second line consists of N space-separated integers - req[1], req[2],..., req[N] representing the request time of the tasks.
The third line consists of a positive integer - dur_size, representing the number of tasks (M).
The last line consists of M space-separated integers - dur[1], dur[2],..., dur[N] representing the duration of the tasks.

Output
Print a real number representing the average task waiting time, which is calculated using non-preemptive SJF scheduling. Print the output upto two decimal places.

Constraints
0 ≤ req[i] < 100
0 < dur[i] < 100
0 < i ≤ req_size, dur_size

Note
The request times and duration times are sorted in ascending order of request time.
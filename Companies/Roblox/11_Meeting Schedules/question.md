You are given an array `schedules` representing existing meetings for all employees over the course of an entire day, and an integer `length` representing the length of a new meeting in minutes.

Each element in `schedules` is an array, such that `schedules[i][j]` represents the $j^{\text{th}}$ meeting of the $i^{\text{th}}$ employee. Each meeting is represented by a pair of integers: `[startTime, finishTime]`, where each integer represents the number of minutes passed since the beginning of the day. `startTime` and `finishTime` do not exceed $24 \times 60$.

Your task is to find the earliest possible time when a meeting of length `length` can be scheduled for all employees. If there is no time block which suits everyone, return `-1`.

*Note: The new meeting should also fit within the same day, so the finish time for this meeting should not exceed $24 \times 60$.*

*Note: You are not expected to provide the most optimal solution, but a solution with time complexity no worse than $O(\text{schedules.length}^2 \cdot \max(\text{schedules}[i].\text{length})^2)$ will fit within the execution time limit.*

**Example**

* For

```text
schedules = [
  [[60, 150], [180, 240]],
  [[0, 210], [360, 420]]
]

```

and `length = 120`, the output should be `solution(schedules, length) = 240`.

**Explanation:**
If the new meeting is scheduled to start from minute `240`, it will last until minute `360`. The interval `[240, 360]` does not coincide with any other intervals from `schedules`, so it's possible to schedule this meeting to allow all employees to attend.

A meeting with a duration of `120` minutes that suits the schedule of all employees can't be scheduled earlier, so the answer is `240`.

* For

```text
schedules = [
  [[480, 510]],
  [[240, 330]],
  [[375, 400]]
]

```

and `length = 180`, the output should be `solution(schedules, length) = 0`.


*Explanation:*
If the new meeting is scheduled right at the beginning of the day, then it wouldn't conflict with any other meetings, so the answer is `0`.

* For

```text
schedules = [
  [[0, 1439]],
  [[0, 1439]],
  [[0, 390], [480, 510]]
]

```

and `length = 90`, the output should be `solution(schedules, length) = -1`.

*Explanation:*
The first two employees are booked for the whole day, so it's not possible to have a meeting with a duration of `90` minutes that all the employees can attend. Thus the answer is `-1`.

**Input/Output**

* **[execution time limit] 4 seconds (py3)**
* **[memory limit] 1 GB**
* **[input] array.array.array.integer schedules**
An array of arrays of integer arrays, where each integer array `schedules[i][j]` contains 2 distinct integers representing the $j^{\text{th}}$ meeting booked for the $i^{\text{th}}$ employee. Each integer within the array represents the time (in minutes) passed since the beginning of the day.
*Guaranteed constraints:*
`1 <= schedules.length <= 100`
`0 <= schedules[i].length <= 100`
`schedules[i][j].length = 2`


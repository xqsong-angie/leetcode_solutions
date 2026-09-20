
leetcode 1360,Optiver考该题变体
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.


变体：
Days Between 3.0 (V2)

Write a function, DaysBetween, which returns an integer representing the number of days between two dates.

Each date is represented by three integers: year, month(1-12), day(1-31). The first date is guaranteed to occur before the second date. We have also provided a function, DaysInMonth, which returns an integer representing the number of days in a month given two integer parameters: month and year. Do not use system provided Date objects. We are testing your implementation, not the system's.

Example: DaysBetween(2010, 5, 1, 2011, 5, 1) returns 365.

Note on Custom Input: You can test against custom input at the very bottom. Each variable must be on its own line. You will notice this if you download the sample testcases. The example input above would be typed into the custom input box as follows:
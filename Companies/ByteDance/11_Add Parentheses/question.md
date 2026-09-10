Description

You are given a string expr representing a sum of two positive integers. Both of these integers do not have zeros in their decimal representation. For example, expr can contain "741+12" but can't be equal to "+74112" or "740+12".

You should add exactly one pair of parentheses to this string so that:

- the plus ('+') sign is inside these parentheses;
- there is at least one digit between the plus sign and each of the two parentheses.

For example, "741+12" can be transformed into "74(1+1)2" but can't be turned into "(74)1+12" or "741(+12)".

The resulting string still represents a valid arithmetic expression that can be evaluated. For example, "74(1+1)2" should be interpreted as "74*(1+1)*2", which is equal to 296.

Find and return the smallest possible value that can be obtained from expr after performing the operations described above.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(expr.length^4) will fit within the execution time limit.


Example
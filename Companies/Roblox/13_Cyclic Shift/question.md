A *cyclic shift* is the operation of rearranging the digits in a number (in decimal format) by moving some digits at the end of the number to before the beginning of the number, while shifting all other digits to the next position. Given two integers of the same length `a` and `b`, `a` would be a cyclic pair of `b` if it's possible for `a` to become equal to `b` after performing cyclic shifts on `a` - moving 0 or more ending digits to the beginning while shifting all other digits to the next position in the same order.

Given an array of positive integers `a`, your task is to count the number of cyclic pairs `i` and `j` (where `0 <= i < j < a.length`), such that `a[i]` and `a[j]` have the same number of digits and `a[i]` is equal to a cyclic shift of `a[j]`.

**Example**

For `a = [13, 5604, 31, 2, 13, 4560, 546, 654, 456]`, the output should be `solution(a) = 5`.

There are 5 cyclic pairs of numbers - pairs which are equal to each other after cyclic shifts:

* `a[0] = 13` and `a[2] = 31` (`i = 0` and `j = 2`),
* `a[0] = 13` and `a[4] = 13` (`i = 0` and `j = 4`),
* `a[2] = 31` and `a[4] = 13` (`i = 2` and `j = 4`),
* `a[1] = 5604` and `a[5] = 4560` (`i = 1` and `j = 5`),
* `a[6] = 546` and `a[7] = 654` (`i = 6` and `j = 7`).

Note that `a[6] = 546` and `a[8] = 456` are not cyclic pairs - `546` can only be paired with cyclic shift of `546`, `465` and `654`.

Also, note that `a[5] = 4560` and `a[8] = 456` are not cyclic pairs because they have different number of digits.

**Input/Output**

* **[execution time limit] 3 seconds (java)**
* **[memory limit] 1 GB**
* **[input] array.integer a**
**1. Cardinality Sorting**

The binary cardinality of a number is the total number of 1's it contains in its binary representation. For example, the decimal integer 20 corresponds to the binary number 10100. There are 2 1's in the binary representation so its binary cardinality is 2.

Given an array of decimal integers, sort it ascending first by binary cardinality, then by decimal value. Return the resulting array.

**Example**

n = 4

nums = [1, 2, 3, 4]

* 1 -> 1 (binary), so 1's binary cardinality is 1.
* 2 -> 10 (binary), so 2's binary cardinality is 1.
* 3 -> 11 (binary), so 3's binary cardinality is 2.
* 4 -> 100 (binary), so 4's binary cardinality is 1.

The sorted elements with binary cardinality of 1 are [1, 2, 4]. The array to return is [1, 2, 4, 3].

**Function Description**

Complete the function *cardinalitySort* in the editor below.

*cardinalitySort* has the following parameter(s):

* *int nums[n]*: an array of decimal integers
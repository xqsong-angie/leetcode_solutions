**1. Better Compression**

Consider a string, $S$, that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be multiple occurrences of the same character. A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string.

**Example**

The string `'a3c9b2c1'` has two instances where `'c'` is followed by a count: once with 9 occurrences, and again with 1. It should be compressed to `'a3b2c10'`.

**Function Description**

Complete the function *betterCompression* in the editor below.

*betterCompression* has the following parameter:

* *S*: a compressed string

**Returns:**

* *string*: the properly compressed string

**Constraints**

* 1 <= size of S <= 100000
* 'a' <= characters in S <= 'z'
* 1 <= frequency of each character in S <= 1000
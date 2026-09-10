**Codewriting**

You are given an array of integers `memory` consisting of `0`s and `1`s which indicates whether the corresponding memory unit is free or not. `memory[i] = 0` means that the $i^{\text{th}}$ memory unit is free, and `memory[i] = 1` means it's occupied.

The memory is aligned with segments of `8` units so all occupied memory blocks must start at an index divisible by `8` (e.g. `0`, `8`, `16`, etc).

Your task is to perform two types of queries:

* `alloc x`: Find the left-most **aligned** memory block of `x` consecutive free memory units and mark these units as occupied (ie: find the left-most contiguous subarray of `0`s, starting at the position `start` which is divisible by `8`, and replace all these memory units with `1`s).
* If there is no proper aligned memory block with `x` consecutive free units, return `-1`; otherwise return the index of the first position of the allocated block segment and assign an **ID** to every single element in the block, based on an **atomic counter** *(the counter starts at `1` and is incremented on every successful alloc operation)*.
* Note: `x` may be greater than `8`, so the block may cover more than one memory segment.


* `erase ID`: If there exists an allocated memory block with element ids equal to `ID`, free all its memory units (set all of the bits in the block to `0`).
* Return the length of the deleted memory block. If there is no such `ID` or the block with this `ID` has already been deleted, return `-1`.



The queries are given in the following format:

* `queries` is an array of 2-elements arrays;
* if `queries[i][0] == 0` then this is an `alloc` type query, where `x = queries[i][1]`;
* if `queries[i][0] == 1` then this is an `erase` type query, where `ID = queries[i][1]`.

Return an array containing the results of all the queries.

*Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than $O(\text{queries.length} \cdot \text{memory.length}^2)$ will fit within the execution time limit.*

**Example**

* For `memory = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]` and `queries = [[0, 2], [0, 1], [0, 1], [1, 1], [0, 3], [1, 4], [0, 4]]`, the output should be `solution(memory, queries) = [8, 0, -1, 2, 8, -1, -1]`.

▼ Expand to see the example video.

\
queries                     results
[0, 2] alloc 2      (allocated!) 8
[0, 1] alloc 1


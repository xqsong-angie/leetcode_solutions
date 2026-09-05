**Organize Encyclopedias**

Cole needs to remove all encyclopedias from an n x m shelf in a library. When selecting an encyclopedia, all other encyclopedias in the same row and column by the same author are also removed. Determine the minimum number of encyclopedias Cole needs to select to remove all encyclopedias.

The shelf contains encyclopedias by k authors, each represented by an integer from 1 to k.

**Example**

Let there be k = 3 authors. Let the following matrix represent the encyclopedias shelf:

2 2 1

1 1 1

2 3 3

Cole can choose the encyclopedia at position (2,3) in the first operation and remove it (1-based rows and columns). Then, the matrix looks like this:

2 2 x

x x x

2 3 3

Cole can choose the encyclopedia at position (1,1) in the second operation and remove it. Then, the matrix looks like this:

x x x

x x x

x 3 3

Cole can choose the encyclopedia at position (3,3) in the third operation and remove it. Then, the matrix looks like this:

x x x

x x x

x x x

Therefore, the minimum number of encyclopedias to select from the shelf is 3.
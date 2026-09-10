Description

Given matrix, an n x n square matrix of integers, let's define its 0-border as the union of its leftmost and rightmost columns, as well as its top and bottom rows.

If we were to remove the matrix's 0-border, then the 0-border of the resulting matrix can be defined as the 1-border of the original matrix. We can continue this way to define the 2-border, 3-border, etc.

  0-border           1-border           2-border
┌───┬───┬───┬───┬───┐ ┌───┬───┬───┬───┬───┐ ┌───┬───┬───┬───┬───┐
│ X │ X │ X │ X │ X │ │   │   │   │   │   │ │   │   │   │   │   │
├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤
│ X │   │   │   │ X │ │   │ X │ X │ X │   │ │   │   │   │   │   │
├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤
│ X │   │   │   │ X │ │   │ X │   │ X │   │ │   │   │ X │   │   │
├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤
│ X │   │   │   │ X │ │   │ X │ X │ X │   │ │   │   │   │   │   │
├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┤
│ X │ X │ X │ X │ X │ │   │   │   │   │   │ │   │   │   │   │   │
└───┴───┴───┴───┴───┘ └───┴───┴───┴───┴───┘ └───┴───┴───┴───┴───┘

For each k in [0, 1, ..., floor((n - 1) / 2)], your task is to sort the elements in each k-border and place them in clockwise order, starting from the top-left corner.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(n^3) will fit within the execution time limit.
Description

Imagine there is a circle of red and blue tiles. The color of the tiles are represented by the array tileColors, where tileColors[i] = 0 means that the i^th tile is red, whereas tileColors[i] = 1 means that the i^th tile is blue.

We want to determine whether the tiles that are next to each other in the circle have alternating colors - the i^th tile should have a different color than both the i+1^th and the i-1^th neighboring tiles. Given an integer size, we want to know how many groups of size consecutive tiles have alternating colors.

Note that because tileColors represents a circle, the first and last tiles (elements in the array) are considered to be next to each other.

Also note that you are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(tileColors.length^2) will fit within the execution time limit.


Example

- For tileColors = [0, 1, 0, 1, 1] and size = 3, the output should be solution(tileColors, size) = 3.

  Explanation:

  - There are five unique subarrays of size 3.

  - First: tileColors[0...2] = [0, 1, 0], which has alternating colors;

  - Second: tileColors[1...3] = [1, 0, 1], which has alternating colors;

  - Third: tileColors[2...4] = [0, 1, 1], which does not have alternating colors;

  - Fourth: tileColors[3...4] + tileColors[0] = [1, 1, 0] (+ is the array concatenation operation), which does not have alternating colors;

  - Fifth: tileColors[4] + tileColors[0...1] = [1, 0, 1], which has alternating colors.
You are given an array of integers `towers` representing the height of some block towers (in number of blocks), and are asked to make the towers into an ascending or descending stair-step pattern. This means the height of each tower should differ from its neighbors by exactly 1, and the whole sequence should be either strictly increasing or decreasing. To change the towers, you can make multiple moves in which you add only one block to the top of any tower. Your task is to find the minimum number of moves required to make the towers either consecutively taller or shorter - whichever sequence requires fewer moves.

**Example**

* For `towers = [1, 4, 3, 2]`, the output should be `solution(towers) = 4`.
The optimal solution is to add:
* Four blocks to the top of the first tower.


The final height of the towers will be: `[5, 4, 3, 2]`.
* For `towers = [5, 7, 9, 4, 11]`, the output should be `solution(towers) = 9`.
The optimal solution is to add:
* Two blocks to the top of the first tower;
* One block to the top of the second tower;
* Six blocks to the top of the fourth tower.


The final height of the towers will be: `[7, 8, 9, 10, 11]`.

**Input/Output**

* **[execution time limit] 4 seconds (py3)**
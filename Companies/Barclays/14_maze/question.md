A mouse is placed in a maze. There is a huge chunk of cheese somewhere in the maze. The maze is represented as an N x M grid of integers where 0 represents a wall, 1 represents the path where the mouse can move and 9 represents the chunk of cheese. The mouse starts at the top left corner at (0,0). Write an algorithm to output 1 if the mouse can reach the chunk of cheese, else output 0.

Input
The first line of the input consists of two space-separated integers - maze_row and maze_col representing the number of rows (N) and the number of columns (M) in the maze, respectively.
The next N lines consist of M space-separated integers representing the maze.

Output
Print 1 if there is a path from the initial position of the mouse to the cheese, else print 0.

Note
The mouse is not allowed to leave the maze or climb the walls.

Example
Input:
8 8
1 0 1 1 1 0 0 1
1 0 0 0 1 1 1 1
1 0 0 0 0 0 0 0
1 0 1 0 9 0 1 1
1 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 1

Output:
1
1244. Design A Leaderboard

https://www.lintcode.com/problem/3660/

Description
Now you are required to design a Leaderboard that can dynamically display the score data of the players.

Please refine the 3 methods in the Leaderboard class to achieve the following effects:

addScore(playerId, score):
If the player is already on the leaderboard, add score points to his current score and update the ranking
If the player is not on the leaderboard, add him to the list and set his score to score
top(k): returns the sum of the scores of the top k players in terms of scores
reset(playerId): Zeroes out the score for the specified player. It is guaranteed that the player has a score and is on the list before calling this function.
Note that in the initial state, the leaderboard is empty.

It's guaranteed that k is less than or equal to the current number of players.

There will be at most 1000 function calls.

1
<
=
p
l
a
y
e
r
I
d
,
K
<
=
10000
1<=playerId,K<=10000

1
<
=
s
c
o
r
e
<
=
100
1<=score<=100

Example
The Leaderboard class you designed will be instantiated and called as such:

java
python
cpp
Leaderboard leaderboard = new Leaderboard();
leaderboard.addScore(playerId, score);
int ans = leaderboard.top(k);
leaderboard.reset(playerId);
Example 1

Input

addScore(1,73)
addScore(2,56)
addScore(3,39)
addScore(4,51)
addScore(5,4)
top(1)
reset(1)
reset(2)
addScore(2,51)
top(3)
Output

73
141
Explanation

Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
Example 2

Input

addScore(1,9)
addScore(2,90)
addScore(3,84)
addScore(4,12)
top(4)
addScore(5,1)
addScore(6,21)
reset(5)
addScore(5,98)
addScore(7,5)
top(5)
Output

195
305
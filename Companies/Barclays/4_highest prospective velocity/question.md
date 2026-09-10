Martin's father goes for a jog every morning. Martin follows him several minutes later. His father starts at a position that is X1 meters away from their home and runs rectilinearly at a constant speed of V1 meters per step for N steps.

Martin is standing at X2 meters away from his home. He wonders how fast he must run at some constant speed of V2 meters per step so as to maximize F, where F equals the number of his father's footsteps that Martin will land on during his run. It is given that the first step that Martin will land on, from his starting position, will have been landed on by his father.

Note that if more than one prospective velocity results in the same number of maximum common steps, output the highest prospective velocity as V2.

Write an algorithm to help Martin calculate F and V2.

Input
The first line of the input consists of an integer fatherPos, representing the initial position of Martin's father (X1).
The second line consists of an integer martinPos, representing the initial position of Martin (X2).
The third line consists of an integer velFather, representing the velocity of the father (V1).
The last line consists of an integer steps, representing the number of steps taken by the father (N).

Output
Print two space-separated integers as the maximum number of common footsteps F and respective speed V2.

Constraints
1 ≤ fatherPos ≤ 10^5
0 ≤ martinPos ≤ fatherPos
1 ≤ velFather ≤ 10^4
1 ≤ steps ≤ 10^6

Example
Input:
3
2
2
20

Output:
21 1

Explanation:
Martin can have a maximum of 21 common footsteps with a velocity of 1 m/step.
General Rules
Grid cells represent entities in a 2D matrix.   
Synchronous Update: All cells transition their states simultaneously per day based on the state of the system on that day.   
Spread Direction: 8-directional neighbors (up, down, left, right, and 4 diagonals) unless specified otherwise.   
Time Semantics: Day 0 is the initial state. Newly infected cells cannot infect others on the day they become infected; they can only spread infection starting from the next day (Day + 1).   

Part 1: Basic Infection Simulation   
Given a 2D grid where:".": Uninfected / Healthy   
"X": Infected   Rules:On each day, every currently infected cell ("X") spreads infection to all uninfected 8-directional neighbors.   
Return the total number of days needed for the system to reach a stabilized state (i.e., no new infections occur).   
If the grid is already stable at start, return 0.   

Part 2: Infection with Immune Obstacles   
Extends Part 1 by introducing immune cells:"I": Immune wall / Obstacle   
Rules:"I" cells can never be infected and do not spread infection.   
They act as barriers blocking infection spread.   
Return the number of days until the system reaches equilibrium (no more state changes).  

Part 3: Advanced Variants   

Part 3A: Recovery / Limited Infection Lifespan   
"." = Healthy, "X" = Infected, "I" = Immune.   
Each infected cell maintains an infection_age starting at 0 on the day it becomes infected.   
An infected cell remains contagious and active for D days.   
On Day D, the cell transitions to "I" (Immune). Once immune, it can no longer be infected or spread infection.   
Return the total number of days until there are no active infected cells ("X") left in the system.   

Part 3B: Threshold Infection   
Extends Part 1/2 with an integer parameter T.   
A healthy cell "." becomes infected on the next day if and only if it has at least T infected 8-directional neighbors.   
Return the days to reach stabilization.   

Part 4: Death Countdown Variant   
Introduced integer threshold K and countdown duration C.   
When a healthy cell has >=K infected neighbors, it enters a "countdown" state (e.g., "C").   After C consecutive days in countdown, it transitions to "dead" (acts as an obstacle).   
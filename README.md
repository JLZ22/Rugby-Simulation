# Rugby Simulation

## Context

In rugby, a common drill to warm up is "infinite passing". This is a drill where players will line up in `n` lines (typically no more than 5 or 6) and pass the ball according to the following algoirthm. 

The ball starts on the leftmost line. 

1. the player with the ball passes to the adjacent right line
2. the player who just passed the ball goes to the end of the adjacent right line
3. repeat steps 1 and 2 until the ball reaches the rightmost line
4. the player with the ball passes to the adjacent left line 
5. the player who just passed the ball goes to the end of the adjacent left line
6. repeat steps 1-6

## Problem

## Approach
- Simulates a rugby drill in which players are in 2+ lines and pass the ball to one of the adjacent lines before switching
- perform brute force to see if the current number of players and lines will lead to a player being stuck oscillating between two lines

# Rugby Simulation

## Packages

```
textual
```

To install with `pip`, run `pip install -r requirements.txt`.
## Context

In rugby, a common drill to warm up is "infinite passing". This is a drill where players will line up in lines (typically no more than 5 or 6) and pass the ball according to the following algoirthm. 

The ball starts on the leftmost line. 

1. the player with the ball passes to the adjacent right line
2. the player who just passed the ball goes to the end of the adjacent right line
3. repeat steps 1 and 2 until the ball reaches the rightmost line
4. the player with the ball passes to the adjacent left line 
5. the player who just passed the ball goes to the end of the adjacent left line
6. repeat steps 1-6

Below is a diagram of the drill running where the ball is passed 4 times. Each column is a line of players where each number is a unique player. A number with `b` immediately after it represents the player with the ball. For example, `1b` means player 1 has the ball.

The example below was generated by the code in main.
```
Initial State:
Line 1:    Line 2:    Line 3:    
1b         2          3          
4          5          6          
7          8          9          

Iteration 1:
Line 1:    Line 2:    Line 3:    
4          2b         3          
7          5          6          
           8          9          
           1                     

Iteration 2:
Line 1:    Line 2:    Line 3:    
4          5          3b         
7          8          6          
           1          9          
                      2          

Iteration 3:
Line 1:    Line 2:    Line 3:    
4          5b         6          
7          8          9          
           1          2          
           3                     

Iteration 4:
Line 1:    Line 2:    Line 3:    
4b         8          6          
7          1          9          
5          3          2          
```

## Problem

A common occurence in this drill is that one or more players will be stuck oscillating between two lines. This is happens when a player goes to the line they were just in without going all the way down to the last line. For example, if a player, Jeff, is in a drill with 3 lines and is the first person in the first line, Jeff would have oscillated one time if he were to pass (and subsequently join) line 2 and then pass to line 1 and join line 1 again. 

A key characteristic that determines whether a player will oscillate or not is whether the line they are entering has an odd or even number excluding that player. If Jeff passes the ball and goes to the end of a line with an even number of players (excluding Jeff), his next turn would not result in an oscillation. Conversly, if Jeff were to enter a line with an odd number of players (excluding himself), his next turn would not result in an oscillation. The only exception is if the ball reaches the end and switches direction. Since that is a necessary part of the drill, we will not be counting changes in direction on the ends of the drill as an oscillation. Below is a brief example where Jeff is player 1. 

**Jeff enters an odd line** (example generated by the code in main)

```
Initial State:
Line 1:    Line 2:    Line 3:    
1b         2          3          
4                                

Iteration 1:
Line 1:    Line 2:    Line 3:    
4          2b         3          
           1                     

Iteration 2:
Line 1:    Line 2:    Line 3:    
4          1          3b         
                      2          

Iteration 3:
Line 1:    Line 2:    Line 3:    
4          1b         2          
           3                     

Iteration 4:
Line 1:    Line 2:    Line 3:    
4b         3          2          
1                                

Player 1 oscillated 1 times.
Player 2 did not oscillate.
Player 3 did not oscillate.
Player 4 did not oscillate.
```

**Jeff enters an even line** (example generated by the code in main)

```
Initial State:
Line 1:    Line 2:    Line 3:    
1b         2          3          
4          5                     

Iteration 1:
Line 1:    Line 2:    Line 3:    
4          2b         3          
           5                     
           1                     

Iteration 2:
Line 1:    Line 2:    Line 3:    
4          5          3b         
           1          2          

Iteration 3:
Line 1:    Line 2:    Line 3:    
4          5b         2          
           1                     
           3                     

Iteration 4:
Line 1:    Line 2:    Line 3:    
4b         1          2          
5          3                     

Iteration 5:
Line 1:    Line 2:    Line 3:    
5          1b         2          
           3                     
           4                     

Iteration 6:
Line 1:    Line 2:    Line 3:    
5          3          2b         
           4          1          

Player 1 did not oscillate.
Player 2 did not oscillate.
Player 3 did not oscillate.
Player 4 did not oscillate.
Player 5 did not oscillate.
```

As you can see from the visualization above, Jeff (player 1) passes the ball a total of two times in each instance. When there was an even number of players in line 2, he did not oscillate. However, when there was an odd number of players in line 2, he did oscillate. 

## Approach

1. To gain intuition on the problem and potentially observe patterns, I am starting with a brute force approach where I am keeping track of which players oscillate. 
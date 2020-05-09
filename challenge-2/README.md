# Challenge 2 - The Lucky One

We really enjoy ping-pong in our office. We enjoy tournaments too. Everyone thinks she's the best, but that's far from the truth. Everyone has an inner skill si. If players i and j play a game of ping-pong, player i wins if si is greater than sj, but otherwise they lose. No two players have the same skill level.

We have a ping-pong tournament coming up. Help me predict the winner! I have a list of matches and their outcome. Can you tell me who the strongest player in our office is?

A unique solution is guaranteed to exist.

## Input

The first line has an integer **C**, which is the number of cases for the problem.

Each case starts with a line with one integer, **N**, which is the number of matches. The following **N** lines contain three integers: **A**, the number of the first player, **B**, the number of the second player, and **R**, which is 1 if A won, and 0 otherwise. Players are numbered from 1 to P, with P being the total number of players.

## Output

For each case, output a line starting with `Case #x: ` followed by the number of the strongest player. Every line should end with a new line character.

## Limits

1 ≤ **C** ≤ 10

1 ≤ **N** ≤ 1000000

## Sample Input

```
1
3
3 2 1
1 3 0
3 2 1
```

## Sample Output

```
Case #1: 3
```
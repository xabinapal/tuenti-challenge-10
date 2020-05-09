# Write-up 1 - Rock, Paper, Scissors

The first challenge could be solved with some nested *ifs*, but more elegant solutions can be achieved using simple math. The winner of this game can be represented as a cyclic graph and, if we assign the values `0`, `1` and `2` to the different choices (`R` for rock, `P` for paper and `S` for scissors), the winner can be calculated with a modulo operation.

|        | **R0** | **P1** | **S2** |
|--------|--------|--------|--------|
| **R0** |   --   |   P1   |   R0   |
| **P1** |   P1   |   --   |   S2   |
| **S2** |   R0   |   S2   |   --   |

There are only three possibilities:
* If both players choose the same element, no one wins and it's a draw
* If the choice of the first player plus 1 modulo 3 equals the choice of the second player, he wins
* Else, the second player wins

The output of `player1 + 1 mod 3` is the following one:
* **R0 + 1 mod 3** = P1
* **P1 + 1 mod 3** = S2
* **S2 + 1 mod 3** = R0
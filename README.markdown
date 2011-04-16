# Simple Cellular Automata

This is a straight-forward implementation of cellular automata, based on the description in [1].
Initial implementation uses a simple 1D cellular space and transition functions based on Wolfram rules.

[1] Bio-Inspired Artificial Intelligence, 2008, D. Florreano and C. Mattiussi, MIT Press

## Example

Using cells with state `'x'` (corresponding to 1) or `' '` (corresponding to 0) and wolfram rule 110, the following development occur:

     0 |xx     x   x   xx     x   x   |
     1 |xx    xx  xx  xxx    xx  xx  x|
     2 | x   xxx xxx xx x   xxx xxx xx|
     3 |xx  xx xxx xxxxxx  xx xxx xxxx|
     4 | x xxxxx xxx    x xxxxx xxx   |
     5 |xxxx   xxx x   xxxx   xxx x   |
     6 |x  x  xx xxx  xx  x  xx xxx  x|
     7 |x xx xxxxx x xxx xx xxxxx x xx|
     8 |xxxxxx   xxxxx xxxxxx   xxxxx |
     9 |x    x  xx   xxx    x  xx   xx|
    10 |x   xx xxx  xx x   xx xxx  xx |

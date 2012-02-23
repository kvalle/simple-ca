# Simple Cellular Automata

This is a straight-forward implementation of cellular automata, based on the description in [1].
Initial implementation uses a simple 1D cellular space and transition functions based on Wolfram rules.

[1] Bio-Inspired Artificial Intelligence, 2008, D. Florreano and C. Mattiussi, MIT Press

## Example

Using cells with state `'x'` (corresponding to 1) or `' '` (corresponding to 0) and wolfram rule 110, the following development occur:

     0 | xxxxx xx  xxxx  xxxxx x x xx x  x   x  xxxx xx x xx  x x    xxxx xx    x xx xx |
     1 |xx   xxxx xx  x xx   xxxxxxxxxx xx  xx xx  xxxxxxxxx xxxx   xx  xxxx   xxxxxxxx |
     2 |xx  xx  xxxx xxxxx  xx        xxxx xxxxxx xx       xxx  x  xxx xx  x  xx      xx|
     3 | x xxx xx  xxx   x xxx       xx  xxx    xxxx      xx x xx xx xxxx xx xxx     xx |
     4 |xxxx xxxx xx x  xxxx x      xxx xx x   xx  x     xxxxxxxxxxxxx  xxxxxx x    xxx |
     5 |x  xxx  xxxxxx xx  xxx     xx xxxxxx  xxx xx    xx           x xx    xxx   xx xx|
     6 |x xx x xx    xxxx xx x    xxxxx    x xx xxxx   xxx          xxxxx   xx x  xxxxx |
     7 |xxxxxxxxx   xx  xxxxxx   xx   x   xxxxxxx  x  xx x         xx   x  xxxxx xx   xx|
     8 |        x  xxx xx    x  xxx  xx  xx     x xx xxxxx        xxx  xx xx   xxxx  xx |
     9 |       xx xx xxxx   xx xx x xxx xxx    xxxxxxx   x       xx x xxxxxx  xx  x xxx |
    10 |      xxxxxxxx  x  xxxxxxxxxx xxx x   xx     x  xx      xxxxxxx    x xxx xxxx x |
    11 |     xx      x xx xx        xxx xxx  xxx    xx xxx     xx     x   xxxx xxx  xxx |
    12 |    xxx     xxxxxxxx       xx xxx x xx x   xxxxx x    xxx    xx  xx  xxx x xx x |
    13 |   xx x    xx      x      xxxxx xxxxxxxx  xx   xxx   xx x   xxx xxx xx xxxxxxxx |
    14 |  xxxxx   xxx     xx     xx   xxx      x xxx  xx x  xxxxx  xx xxx xxxxxx      x |
    15 | xx   x  xx x    xxx    xxx  xx x     xxxx x xxxxx xx   x xxxxx xxx    x     xx |
    16 |xxx  xx xxxxx   xx x   xx x xxxxx    xx  xxxxx   xxxx  xxxx   xxx x   xx    xxx |
    17 |x x xxxxx   x  xxxxx  xxxxxxx   x   xxx xx   x  xx  x xx  x  xx xxx  xxx   xx xx|
    18 |xxxxx   x  xx xx   x xx     x  xx  xx xxxx  xx xxx xxxxx xx xxxxx x xx x  xxxxx |
    19 |x   x  xx xxxxxx  xxxxx    xx xxx xxxxx  x xxxxx xxx   xxxxxx   xxxxxxxx xx   xx|
    20 |x  xx xxxxx    x xx   x   xxxxx xxx   x xxxx   xxx x  xx    x  xx      xxxx  xx |
    21 |x xxxxx   x   xxxxx  xx  xx   xxx x  xxxx  x  xx xxx xxx   xx xxx     xx  x xxxx|
    22 |xxx   x  xx  xx   x xxx xxx  xx xxx xx  x xx xxxxx xxx x  xxxxx x    xxx xxxx   |
    23 |x x  xx xxx xxx  xxxx xxx x xxxxx xxxx xxxxxxx   xxx xxx xx   xxx   xx xxx  x  x|
    24 |xxx xxxxx xxx x xx  xxx xxxxx   xxx  xxx     x  xx xxx xxxx  xx x  xxxxx x xx xx|
    25 |  xxx   xxx xxxxxx xx xxx   x  xx x xx x    xx xxxxx xxx  x xxxxx xx   xxxxxxxx |
    26 | xx x  xx xxx    xxxxxx x  xx xxxxxxxxxx   xxxxx   xxx x xxxx   xxxx  xx      x |
    27 |xxxxx xxxxx x   xx    xxx xxxxx        x  xx   x  xx xxxxx  x  xx  x xxx     xx |
    28 |x   xxx   xxx  xxx   xx xxx   x       xx xxx  xx xxxxx   x xx xxx xxxx x    xxxx|
    29 |x  xx x  xx x xx x  xxxxx x  xx      xxxxx x xxxxx   x  xxxxxxx xxx  xxx   xx   |
    30 |x xxxxx xxxxxxxxxx xx   xxx xxx     xx   xxxxx   x  xx xx     xxx x xx x  xxx  x|
    31 |xxx   xxx        xxxx  xx xxx x    xxx  xx   x  xx xxxxxx    xx xxxxxxxx xx x xx|
    32 |  x  xx x       xx  x xxxxx xxx   xx x xxx  xx xxxxx    x   xxxxx      xxxxxxxx |
    33 | xx xxxxx      xxx xxxx   xxx x  xxxxxxx x xxxxx   x   xx  xx   x     xx      x |
    34 |xxxxx   x     xx xxx  x  xx xxx xx     xxxxx   x  xx  xxx xxx  xx    xxx     xx |
    35 |x   x  xx    xxxxx x xx xxxxx xxxx    xx   x  xx xxx xx xxx x xxx   xx x    xxxx|
    36 |x  xx xxx   xx   xxxxxxxx   xxx  x   xxx  xx xxxxx xxxxxx xxxxx x  xxxxx   xx   |
    37 |x xxxxx x  xxx  xx      x  xx x xx  xx x xxxxx   xxx    xxx   xxx xx   x  xxx  x|
    38 |xxx   xxx xx x xxx     xx xxxxxxxx xxxxxxx   x  xx x   xx x  xx xxxx  xx xx x xx|
    39 |  x  xx xxxxxxxx x    xxxxx      xxx     x  xx xxxxx  xxxxx xxxxx  x xxxxxxxxxx |
    40 | xx xxxxx      xxx   xx   x     xx x    xx xxxxx   x xx   xxx   x xxxx        x |
    41 |xxxxx   x     xx x  xxx  xx    xxxxx   xxxxx   x  xxxxx  xx x  xxxx  x       xx |
    42 |x   x  xx    xxxxx xx x xxx   xx   x  xx   x  xx xx   x xxxxx xx  x xx      xxxx|
    43 |x  xx xxx   xx   xxxxxxxx x  xxx  xx xxx  xx xxxxxx  xxxx   xxxx xxxxx     xx   |
    44 |x xxxxx x  xxx  xx      xxx xx x xxxxx x xxxxx    x xx  x  xx  xxx   x    xxx  x|
    45 |xxx   xxx xx x xxx     xx xxxxxxxx   xxxxx   x   xxxxx xx xxx xx x  xx   xx x xx|
    46 |  x  xx xxxxxxxx x    xxxxx      x  xx   x  xx  xx   xxxxxx xxxxxx xxx  xxxxxxx |
    47 | xx xxxxx      xxx   xx   x     xx xxx  xx xxx xxx  xx    xxx    xxx x xx     x |
    48 |xxxxx   x     xx x  xxx  xx    xxxxx x xxxxx xxx x xxx   xx x   xx xxxxxx    xx |
    49 |x   x  xx    xxxxx xx x xxx   xx   xxxxx   xxx xxxxx x  xxxxx  xxxxx    x   xxxx|
    50 |x  xx xxx   xx   xxxxxxxx x  xxx  xx   x  xx xxx   xxx xx   x xx   x   xx  xx   |

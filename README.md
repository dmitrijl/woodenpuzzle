Solves a specific little puzzle I have at home. 

The puzzle is basically a 5x4 grid (5 rows 4 columns) with 10 pieces in it:

One blue piece, 2x2 size.
Five red pieces of size 1x2
Four yellow pieces of size 1x1

Four of the red pieces start in a vertical position, and one in horizontal.
Due to physical constraints, they cannot be rotated, and thus are best viewed as
two different types of pieces: horizontal and vertical. There are then 4 vertical
and 1 horizontal piece.

The Start position is then like this (X means empty):
| -   -   -   - |
| X | B   B | X |
| -           - |
| V | B   B | V |
|     -   -     |
| V | H   H | V |
| -   -   -   - |
| V | Y | Y | V |
|     -   -     |
| V | Y | Y | V |
| -   -   -   - |

Or in short:
XBBX
VBBV
VHHV
VYYV
VYYV

Because a vertical piece always occupies a 2x1 (2 rows 1 col) its unambiguous.

There are thus 2 empties cells at all time. The challange is to move the pieces in 
such a way that the blue piece ends up at the bottom center:
(in this figure X just means "anything". Its not important where anything else is just
that the blue piece is in that specific position)

XXXX
XXXX
XXXX
XBBX
XBBX

In the physical puzzle, the blue piece's depth is half of all other pieces, and 
is the only piece which this would fit through the hole at the bottom there (it 
is like a thin gate, the other pieces are too "high" to get through, while the
blue is just the right size)

A piece can be moved only if it can be moved into an empty spot (obviously). 


-----------------------------------------------------

The solution and the method isn't anything groundbreaking, it's just a brute force
approach with a breath first search. It works fine because the puzzle is quite small.

From output.txt:
Tested 23540 positions in total, found solution in 115 steps.

I tested the solution on the physical puzzle and it was correct. Also, since it is 
breath first search the solution is guaranteed to be the shortest one.

Why do this? I don't know I just got tired of aimlessly moving pieces, accidently finding
the solution and not being able to recreate it.

===================================================================
License:
I don't know why anyone would take any of this specific code, its just a small project I did
which only took a few hours. Anyway, here is the GPL license: 

Copyright 2015 Dmitrij Lioubartsev

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

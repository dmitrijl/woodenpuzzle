"""
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

"""

import Queue

class Blue(object):
    def __init__(self,pos):
        """pos should be the top left corner of the piece"""
        
        self.pos = pos
        
    def __str__(self):
        return "Blue at " + str(self.pos)
        
    def __repr__(self):
        return "Blue at " + str(self.pos)
        
    def get_moves(self,empties):
    
        #can move left?
        if empties[0] == self.pos-1 and empties[1] == self.pos+3 and self.pos%4 != 0:
            return [-1]
            
        #can move top?
        if empties[0] == self.pos-4 and empties[1] == self.pos-3:
            return [-4]

        #can move right?
        if empties[0] == self.pos+2 and empties[1] == self.pos+6 and self.pos%4 != 2:
            return [1]
            
        #can move bot?
        if empties[0] == self.pos+8 and empties[1] == self.pos+9:
            return [4]
        
        #else return empty list
        return []
        
    def new_empties(self,move,empties):
        if move == 1:
            nempt = [self.pos,self.pos+4]      
        elif move == -1:
            nempt = [self.pos+1,self.pos+5]
        elif move == -4:
            nempt = [self.pos+4,self.pos+5]
        elif move == 4:
            nempt = [self.pos,self.pos+1]
            
        return nempt 
        
class Horizontal(object):
    def __init__(self,pos):
        self.pos = pos
        
    def __str__(self):
        return "Horizontal at " + str(self.pos)

    def __repr__(self):
        return "Horizontal at " + str(self.pos)
        
    def get_moves(self,empties):
        #can move top?
        if empties[0] == self.pos-4 and empties[1] == self.pos-3:
            return [-4]
            
        #can move bot?
        if empties[0] == self.pos+4 and empties[1] == self.pos+5:
            return [4]
        
        moves = []
        
        #can move left?
        if (empties[0] == self.pos-1 or empties[1] == self.pos-1) and self.pos%4 != 0:
            moves.append(-1)
            
        #can move right?
        if (empties[0] == self.pos+2 or empties[1] == self.pos+2) and self.pos%4 != 2:
            moves.append(1)
            
        return moves
            
    def new_empties(self,move,empties):
        nempt = list(empties)
        if move == 1:
            if empties[0] == self.pos+2:
                nempt[0] = self.pos
            else:
                nempt[1] = self.pos
            nempt.sort()
                
        elif move == -1:
            if empties[0] == self.pos-1:
                nempt[0] = self.pos+1
            else:
                nempt[1] = self.pos+1   
            nempt.sort()
            
        elif move == -4 or move == 4:
            nempt = [self.pos,self.pos+1]
            
        return nempt
        
class Vertical(object):
    def __init__(self,pos):
        self.pos = pos
        
    def __str__(self):
        return "Vertical at " + str(self.pos)

    def __repr__(self):
        return "Vertical at " + str(self.pos)
        
    def get_moves(self,empties):
        #can move left?
        if empties[0] == self.pos-1 and empties[1] == self.pos+3 and self.pos%4 != 0:
            return [-1]
            
        #can move right?
        if empties[0] == self.pos+1 and empties[1] == self.pos+5 and self.pos%4 != 3:
            return [1]
        
        moves = []
        
        #can move top?
        if empties[0] == self.pos-4 or empties[1] == self.pos-4:
            moves.append(-4)
            
        #can move bot?
        if empties[0] == self.pos+8 or empties[1] == self.pos+8:
            moves.append(4)
            
        return moves
            
    def new_empties(self,move,empties):
        nempt = list(empties)
        if move == 4:
            if empties[0] == self.pos+8:
                nempt[0] = self.pos
            else:
                nempt[1] = self.pos
            nempt.sort()
                
        elif move == -4:
            if empties[0] == self.pos-4:
                nempt[0] = self.pos+4
            else:
                nempt[1] = self.pos+4   
            nempt.sort()
            
        elif move == -1 or move == 1:
            nempt = [self.pos,self.pos+4]
            
        return nempt

class Yellow(object):
    def __init__(self,pos):
        self.pos = pos
        
    def __str__(self):
        return "Yellow at " + str(self.pos)
        
    def __repr__(self):
        return "Yellow at " + str(self.pos)
        
    def get_moves(self,empties):
        moves = []
    
        #can move top?
        if empties[0] == self.pos-4 or empties[1] == self.pos-4:
            moves.append(-4)
            
        #can move bot?
        if empties[0] == self.pos+4 or empties[1] == self.pos+4:
            moves.append(4)
        
        #can move left?
        if (empties[0] == self.pos-1 or empties[1] == self.pos-1) and self.pos%4 != 0:
            moves.append(-1)
            
        #can move right?
        if (empties[0] == self.pos+1 or empties[1] == self.pos+1) and self.pos%4 != 3:
            moves.append(1)
            
        return moves
            
    def new_empties(self,move,empties):
        nempt = list(empties)
        if empties[0] == self.pos+move:
            nempt[0] = self.pos
        else:
            nempt[1] = self.pos
            
        nempt.sort()
        return nempt
        
class State(object):

    pieces = None
    empties = None
    
    def __init__(self, other_state, move):
        if other_state == None:
            return
        self.pieces = list(other_state.pieces)
        #self.empties = other_state.empties
        #print "Creating new state from old state:"
        #other_state.draw_state()
        #print other_state.empties
        #print move
        for i in range(len(self.pieces)):
            if move[0] == self.pieces[i].pos:
                self.empties = tuple(self.pieces[i].new_empties(move[1],other_state.empties))
                self.pieces[i] = self.pieces[i].__class__(self.pieces[i].pos+ move[1])
                break
                
        self.pieces.sort(key=lambda piece: piece.pos)
        self.pieces = tuple(self.pieces)
            
    def create_empty(self, pieces, empty_spots):
        self.pieces = pieces
        self.empties = empty_spots
        self.empties.sort()
        self.pieces.sort(key=lambda piece: piece.pos)
        self.pieces = tuple(self.pieces)
        self.empties = tuple(self.empties)
        
    def compare(self, other):
        return self.pieces == other.pieces and self.empties == other.empties
        
    def get_possible_moves(self):
        #return zip([p.pos for p in pieces],
    
        res = []
        for p in self.pieces:
            moves = p.get_moves(self.empties)
            for m in moves:
                res.append((p.pos,m))
                
        return res
        
    def draw_state(self):
        d = ["X"]*20
        for p in self.pieces:
            if isinstance(p,Blue):
                d[p.pos] = "B"
                d[p.pos+1] = "B"
                d[p.pos+4] = "B"
                d[p.pos+5] = "B"
            elif isinstance(p,Horizontal):
                d[p.pos] = "H"
                d[p.pos+1] = "H"
            elif isinstance(p,Vertical):
                d[p.pos] = "V"
                d[p.pos+4] = "V"
            else: #yellow
                d[p.pos] = "Y"
                
        print ''.join(d[0:4])
        print ''.join(d[4:8])
        print ''.join(d[8:12])
        print ''.join(d[12:16])
        print ''.join(d[16:20])
        
    def __hash__(self):
        l = [None,None,[],[]]
        for p in self.pieces:
            if isinstance(p,Blue):
                l[0] = p.pos
            elif isinstance(p,Horizontal):
                l[1] = p.pos
            elif isinstance(p,Vertical):
                l[2].append(p.pos)
            else: #yellow
                l[3].append(p.pos)
        l[2] = tuple(l[2])
        l[3] = tuple(l[3])   
        #print "hashtuple: " + str(tuple(l))        
        return hash(tuple(l))
        
    def __eq__(self,other):
        if not isinstance(other, State):
            return False
        
        return hash(self) == hash(other)
        
        
def is_win(state):
    for p in state.pieces:
        if isinstance(p,Blue):
            return p.pos == 13
    return False
        
def main():
    
    #create initial state
    initial = [
        Blue(1),
        Horizontal(9),
        Vertical(4),
        Vertical(7),
        Vertical(12),
        Vertical(15),
        Yellow(13),
        Yellow(14),
        Yellow(17),
        Yellow(18)
    ]
    empties = [0,3]
    start_state = State(None,None)
    start_state.create_empty(initial,empties)
    
    visited = {start_state: None}
    queue = Queue.Queue()
    queue.put(start_state)
    
    win_state = None
    
    #some stats
    pos_tested = 0
    
    #import pdb
    #pdb.set_trace()
    
    done = False
    while not queue.empty() and not done:
        current = queue.get(False)
        #print "=============="
        #print "currently visiting:"
        #current.draw_state()
        #print "hash: " + str(hash(current))
        
        pos_tested += 1
        #moaves = current.get_possible_moves()
        #print moaves
        nexts = [State(current,m) for m in current.get_possible_moves()]
        #print "possible next states:"
        #for n in nexts:
        #    n.draw_state()
        #    print "=="
        
        for n in nexts:
            if not n in visited:
                visited[n] = current
                queue.put(n)
                if is_win(n):
                    win_state = n
                    done = True
                    break
            #else:
                #print "already visited: " 
            #    n.draw_state()
                    
                    
    if not win_state:
        print "No solution found"
        print pos_tested
        return        
                    
    #solution found, backtrack
    sol = []
    done = False
    current = win_state
    while current != None:
        sol.append(current)
        current = visited[current]
        
    sol.reverse()
    
    #print
    print "Tested " + str(pos_tested) + " positions in total, found solution in " + \
                str(len(sol)) + " steps."
                
    i = 1
    for s in sol:
        print "== " + str(i) + " =="
        s.draw_state()
        i += 1
        
    #print
    print "Tested " + str(pos_tested) + " positions in total, found solution in " + \
                str(len(sol)) + " steps."                
    
        
if __name__ == "__main__":
    main()
            

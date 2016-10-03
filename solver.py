#! /usr/bin/python3

from cube import PocketCube

class Node:
    def __init__(self, state, move=None, parent=None):
        self.state = state
        self.parent = parent

        self.cube = PocketCube(state)
        self.children = {_: None for _ in ("R", "U", "F", "R'", "U'", "F'", "R2", "U2", "F2")}
        return

    def makeChildren(self):
        moves = {"R":self.cube.R , "U":self.cube.U , "F":self.cube.F ,
                 "R'":self.cube.R_prime , "U'":self.cube.U_prime , "F'":self.cube.F_prime ,
                 "R2":self.cube.R2 , "U2":self.cube.U2 , "F2": self.cube.F2}
        for command in moves:
            moves[command]()
            self.children[command] = Node(self.cube.state, move = command, parent = self)

            if '2' in command:
                moves[command]()    # Half turns have period 2, returning cube to original state
            else:
                moves[command]()    # Quater turns have period 4
                moves[command]()
                moves[command]()

        return

    def __repr__(self):
        return 'Node with state {}'.format(self.state)


if __name__ == '__main__':
    cube = PocketCube('WWWWBBBBGGGGRRRRYYYYOOOO')
    node = Node(cube.state, None, None)
    node.makeChildren()
    print(node.children["R'"].parent)

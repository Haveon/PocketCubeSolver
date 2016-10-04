#! /usr/bin/python3

from cube import PocketCube
from collections import deque

class Node:
    def __init__(self, state, move=None, parent=None):
        self.state = state
        self.parent = parent
        self.move   = move

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

class Solver:
    def __init__(self, state):
        self.solvedCubeState = ' '*4 + ' '*4 + state[11]*4 + state[14]*4 + ' '*4 + state[22]*4
        self.mixedCubeState = []
        for char in state:
            if char in state[11]+state[14]+state[22]:
                self.mixedCubeState.append(char)
            else:
                self.mixedCubeState.append(' ')
        self.mixedCubeState = ''.join(self.mixedCubeState)
        # Solved instance: the corner FUR defines anchor colors for F,U,R while corner LDB anchors the other colors

        self.forwardNode  = Node(self.mixedCubeState)
        self.backwardNode = Node(self.solvedCubeState)

        self.forwardSolution = {self.mixedCubeState: self.forwardNode}
        self.backwardSolution = {self.solvedCubeState: self.backwardNode}


    def _traverseTree(self, queue, ownDict, otherDict):
        node = queue.popleft()
        node.makeChildren()
        for command, child in node.children.items():
            state = child.state
            if state in ownDict:
                # We already have this state in our dict
                continue
            else:
                ownDict[state] = child
                if state in otherDict:
                    # We have a match forward and backward
                    return state
        queue.extend([child for key,child in node.children.items()])
        return None

    def _search(self):
        backwardNodes = deque([self.backwardNode])
        forwardNodes  = deque([self.forwardNode])

        while True:
            state = self._traverseTree(backwardNodes, self.backwardSolution, self.forwardSolution)

            if state != None:
                return state

            state = self._traverseTree(forwardNodes, self.forwardSolution, self.backwardSolution)

            if state != None:
                return state

    def solve(self):

        if self.solvedCubeState == self.mixedCubeState:
            return ''

        state = self._search()

        solution = []
        node = self.forwardSolution[state]
        while True:
            move = node.move
            if move == None:
                break
            else:
                solution.append(move)
            node = node.parent

        solution.reverse()
        node = self.backwardSolution[state]
        while True:
            move = node.move
            if move == None:
                break
            else:
                if '2' in move:
                    pass
                elif "'" in move:
                    move = move.replace("'",'')
                else:
                    move = move + "'"
                solution.append(move)
            node = node.parent
        return ' '.join(solution)

if __name__ == '__main__':
    solver = Solver('WOWOBBBBYGYGRRRRYWYWOGOG')
    print(solver.solve())

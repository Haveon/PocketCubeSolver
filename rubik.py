#! /usr/bin/python3

from cube import PocketCube
from solver import Solver
import os

def confirmCube(scrambledState):
    cubelets = [set(['w','r','b']),set(['w','r','g']),set(['w','b','o']),set(['w','o','g']),
                set(['y','b','o']),set(['y','g','o']),set(['y','b','r']),set(['y','r','g'])]
    cubeletsIndeces = ((19,1,4), (21,3,6), (15,2,20), (18,0,13),
                       (8,5,17),(9,12,16),(10,7,23), (11,14,22))

    for _ in range(8):
        i,j,k = cubeletsIndeces[_]
        cubelet = set([scrambledState[ind] for ind in [i,j,k]])
        if cubelet in cubelets:
            ind = cubelets.index(cubelet)
            cubelets.pop(ind)
        else:
            return False
    return True

unwrappedCube = """
 -  -  16 17   - -  -  -
 -  -  18 19   - -  -  -
12 13   0  1  4 5   8  9
14 15   2  3  6 7  10 11
 -  -  20 21   - -  -  -
 -  -  22 23   - -  -  -

"""

while True:
    # Get Cube input from user
    print(unwrappedCube)
    scrambledState = ''
    for i in range(6):
        while True:
            face = input("Enter {}-{}:\n".format(i*4, i*4+3)).lower()
            face = "".join(face.split())
            if len(face)!=4:
                print("This face has {} stickers, it should have 4".format(len(face)))
                print("Try again\n")
                continue
            break
        scrambledState += face

    if confirmCube(scrambledState) != True:
        print("There's something wrong with your cubelets")
        print("Please try again\n")
    else:
        break

# Solve the cube
cube = PocketCube(scrambledState)
print(cube)
solver = Solver(cube.state)
solution = solver.solve()
print(solution)

# Write solution out to text file
try:
    os.remove('solution.txt')
except OSError:
    pass

moves = solution.split()
with open('solution.txt','w') as tmp:
    for move in moves:
        tmp.write(move+'\n')

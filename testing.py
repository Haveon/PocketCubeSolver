from cube import PocketCube
from solver import Solver
from random import choice

cube = PocketCube('WWWWBBBBGGGGRRRRYYYYOOOO')
moves = {"R":cube.R , "U":cube.U , "F":cube.F ,
         "R'":cube.R_prime , "U'":cube.U_prime , "F'":cube.F_prime ,
         "R2":cube.R2 , "U2":cube.U2 , "F2": cube.F2}
keys = moves.keys()

for i in range(40):
    moves[choice(keys)]()

print(cube)
solver = Solver(cube.state)
solution = solver.solve()
print(solution)

for _ in solution.split(' '):
    print(cube)
    moves[_]()

print(cube)

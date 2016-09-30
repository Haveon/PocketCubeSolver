#! /usr/bin/python3

class PocketCube(object):
    def __init__(self, state):
        """
        The state should be a string of length 24 with 6 unique identifiers.
        The first four characters represent the front face, then the next four
        the right, then back, left, up, and down.
        """
        self.state = state

        self._rightRotAssignment = (0, 21, 2, 23, 6, 4, 7, 5, 19, 9, 17, 11, 12, 13, 14, 15, 16, 1, 18, 2, 20, 10, 22, 8)
        self._frontRotAssignment = (2, 0, 3, 1, 18, 5, 19, 7, 8, 9, 10, 11, 12, 20, 14, 21, 16, 17, 15, 13, 6, 4, 22, 23)
        self._upRotAssignment = (4, 5, 2, 3, 8, 9, 6, 7, 12, 13, 10, 11, 0, 1, 14, 15, 18, 16, 19, 17, 20, 21, 22, 23)
        return

    def _reAssign(self, newAssignment, numberOfTimes=1):
        for _ in range(numberOfTimes):
            newState = ''
            for i in newAssignment:
                newState += self.state[i]
            self.state = newState
        return

    def R(self):
        self._reAssign(self._rightRotAssignment)

    def F(self):
        self._reAssign(self._frontRotAssignment)

    def U(self):
        self._reAssign(self._upRotAssignment)

    def R2(self):
        self._reAssign(self._rightRotAssignment, 2)

    def F2(self):
        self._reAssign(self._frontRotAssignment, 2)

    def U2(self):
        self._reAssign(self._upRotAssignment, 2)

    def R_prime(self):
        self._reAssign(self._rightRotAssignment, 3)

    def F_prime(self):
        self._reAssign(self._frontRotAssignment, 3)

    def U_prime(self):
        self._reAssign(self._upRotAssignment, 3)

    def __repr__(self):
        unwrappedCube = """
        - -  {16} {17}  - -  - -
        - -  {18} {19}  - -  - -
        {12} {13}  {0} {1}  {4} {5}  {8} {9}
        {14} {15}  {2} {3}  {6} {7}  {10} {11}
        - -  {20} {21}  - -  - -
        - -  {22} {23}  - -  - -

        """.format(*tuple(self.state))
        return unwrappedCube


if __name__ == '__main__':
    cube = PocketCube('WWWWBBBBGGGGRRRRYYYYOOOO')
    print(cube)
    cube.R()
    print(cube)
    cube.F()
    print(cube)
    cube.U()
    print(cube)

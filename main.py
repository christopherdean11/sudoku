"""
testing out finding missing values in a puzzle row

"""
from solver import Solver
import copy


def main():
    """
    docstring for main
    :return: n/a
    """
    pz = get_puzzle(1)
    solv = Solver(pz)

    prettyprintpuzzle(copy.deepcopy(pz))

    solv.solve_puzzle()

    prettyprintpuzzle(pz)


def get_puzzle(puznum):
    p = list(range(0,2))
    p[0] = [[0, 0, 0, 5, 0, 0, 6, 4, 0],
              [4, 5, 8, 0, 6, 7, 9, 1, 0],
              [3, 2, 6, 0, 9, 1, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 1, 0, 8],
              [0, 7, 1, 0, 3, 0, 5, 2, 0],
              [8, 0, 2, 0, 0, 0, 0, 0, 9],
              [0, 0, 0, 3, 5, 0, 2, 9, 7],
              [0, 8, 7, 1, 2, 0, 3, 6, 4],
              [0, 9, 3, 0, 0, 6, 0, 0, 0]]

    p[1] = [[0, 8, 4, 9, 0, 0, 2, 0, 0],
              [6, 5, 7, 4, 2, 3, 0, 0, 8],
              [3, 0, 0, 8, 7, 0, 0, 6, 4],
              [0, 0, 0, 0, 4, 5, 0, 8, 7],
              [0, 0, 1, 0, 0, 0, 3, 0, 0],
              [8, 6, 0, 3, 1, 0, 0, 0, 0],
              [2, 9, 0, 0, 6, 8, 0, 0, 5],
              [4, 0, 0, 5, 9, 2, 6, 3, 1],
              [0, 0, 6, 0, 0, 4, 8, 9, 0]]
    return p[puznum]


def prettyprintpuzzle(puzzle):
    out = []
    for row in range(0, 9):
        for col in range(0, 9):
            if (col % 3 == 0) and col > 0:
                out.append('|')
            if puzzle[row][col] == 0:
                puzzle[row][col] = ' '
            out.append(puzzle[row][col])

        if ((row + 1) % 3 == 0) and row < 8:
            out.append('\n------------')
        out.append('\n')
    print(''.join([str(x) for x in out]))


if __name__ == "__main__":
    main()
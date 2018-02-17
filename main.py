
from solver import Solver
import puzzle


def main():
    """
    main program, solves a users sudoku puzzle
    :return: n/a
    """
    pz = puzzle.get_puzzle(0)
    solver = Solver(pz)

    puzzle.pretty_print_puzzle(pz)
    solver.solve_puzzle()
    puzzle.pretty_print_puzzle(pz)


if __name__ == "__main__":
    main()

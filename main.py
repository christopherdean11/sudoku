"""
testing out finding missing values in a puzzle row

"""
import header
import solver
import sections


def main():
    """
    docstring for main
    :return: n/a
    """
    solv = solver.Solver()
    x = sections.Square(solv.puzzle)
    print(x[1])
    # solv.set_temp_values(header.Section('row', 1))
    solv.put_section(header.Section('square', 1), [1 for _ in range(1, 10)])
    print(x[1])
    x[1] = [2 for _ in range(1, 10)]
    print(x[1])




if __name__ == "__main__":
    main()
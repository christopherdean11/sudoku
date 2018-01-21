"""
testing out finding missing values in a puzzle row

"""
import header
import solver


def main():
    """
    docstring for main
    :return: n/a
    """
    solv = solver.Solver()
    # print(repr(solv))
    solv.set_temp_values(header.Section('row', 1))

if __name__ == "__main__":
    main()
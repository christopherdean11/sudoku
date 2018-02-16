import solver
import header


def test_get_row():
    # create a fake List[][] and get a row
    test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

    testpuz = solver.Solver(test_list)
    assert testpuz.row[0] == [1, 1, 1]
    assert testpuz.row[1] == [2, 2, 2]


def test_get_col():
    # use [1 for _ in range(9)]
    test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    testpuz = solver.Solver(test_list)
    # testpuz.puzzle = test_list

    assert testpuz.col[0] == [1, 2, 3]
    assert testpuz.col[1] == [1, 2, 3]


def test_get_square():
    test_list = [[x for x in range(1, 10)] for _ in range(1, 10)]
    testpuz = solver.Solver(test_list)

    assert testpuz.sq[0] == [1, 2, 3] * 3
    assert testpuz.sq[2] == [7, 8, 9] * 3


def test_find_missing():
    test_list = [1, 2, 0, 4, 5, 0, 0, 8, 9]   # 3, 6, 7 are missing
    testpuz = solver.Solver(test_list)

    assert testpuz._find_missing(test_list) == header.Missing([3, 6, 7], [2, 5, 6])


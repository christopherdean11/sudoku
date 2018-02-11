import solver


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


import puzzle
import solver
import header


def get_puzzle_obj():
    return puzzle.Puzzle()


def get_solver():
    return solver.Solver()


def make_valid_puzzle(solved: bool):
    """
    creates a valid, solved sudoku puzzle
    :return: a valid solved puzzle
    """
    puz = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [4, 5, 6, 7, 8, 9, 1, 2, 3],
           [7, 8, 9, 1, 2, 3, 4, 5, 6],
           [2, 3, 1, 5, 6, 4, 8, 9, 7],
           [5, 6, 4, 8, 9, 7, 2, 3, 1],
           [8, 9, 7, 2, 3, 1, 5, 6, 4],
           [3, 1, 2, 6, 4, 5, 9, 7, 8],
           [6, 4, 5, 9, 7, 8, 3, 1, 2],
           [9, 7, 8, 3, 1, 2, 6, 4, 5]]

    if not solved:
        for x in range(9):
            puz[x][x] = 0
        for x in range(8):
            puz[x+1][x] = 0
        for x in range(4):
            puz[x][x+5] = 0
        for x in range(4):
            puz[x+5][x] = 0
    return puz


def make_test_puzzle(mode: str, zero_slant: bool) -> list:
    """
    generate a false puzzle to prove functions work
    :param mode: str - seqrow for sequential rows (1-9 for each row)
                       flatrow for same value in each row (1, 1, ...)
    :param zero_slant: bool - true places a diagonal 0 from top left to bot. right
    :return: puzzle as a list
    """
    test_puzzle = []

    # seqrow for sequential row, i.e. 1-9 on each row
    if mode=='seqrow':
        for _ in range(1, 10):
            test_puzzle.append([y for y in range(1, 10)])

    # flat row = each row is same value, i.e. all 1 then all 2 ...
    elif mode == 'flatrow':
        for x in range(1, 10):
            test_puzzle.append([x for _ in range(1, 10)])

    if zero_slant:
        for i, x in enumerate(test_puzzle):
            x[i] = 0

    return test_puzzle


def test_puzzle_is_valid():
    puz = [[0, 0, 0, 5, 0, 0, 6, 4, 0],
           [4, 5, 8, 0, 6, 7, 9, 1, 0],
           [3, 2, 6, 0, 9, 1, 0, 0, 0],
           [6, 0, 0, 0, 0, 0, 1, 0, 8],
           [0, 7, 1, 0, 3, 0, 5, 2, 0],
           [8, 0, 2, 0, 0, 0, 0, 0, 9],
           [0, 0, 0, 3, 5, 0, 2, 9, 7],
           [0, 8, 7, 1, 2, 0, 3, 6, 4],
           [0, 9, 3, 0, 0, 6, 0, 0, 0]]
    assert puz == get_puzzle_obj().puzzle


def test_get_row():
    # create a fake List[][] and get a row
    test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

    testpuz = get_solver()
    testpuz.puzzle = test_list

    section = header.Section('row', 0)
    assert testpuz.get_section(section=section) == [1, 1, 1]

    section = header.Section('row', 1)
    assert testpuz.get_section(section=section) == [2, 2, 2]


def test_get_col():
    # use [1 for _ in range(9)]
    test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    testpuz = get_solver()
    testpuz.puzzle = test_list

    section = header.Section('col', 0)
    assert testpuz.get_section(section=section) == [1, 2, 3]

    section = header.Section('col', 1)
    assert testpuz.get_section(section=section) == [1, 2, 3]


def test_get_square():

    testpuz = get_solver()
    testpuz.puzzle = make_test_puzzle('flatrow', False)

    section = header.Section('square', 0)
    assert testpuz.get_section(section=section) == [1, 1, 1, 2, 2, 2, 3, 3, 3]

    section = header.Section('square', 5)
    assert testpuz.get_section(section=section) == [4, 4, 4, 5, 5, 5, 6, 6, 6]

    section = header.Section('square', 8)
    assert testpuz.get_section(section=section) == [7, 7, 7, 8, 8, 8, 9, 9, 9]


def test_find_missing():
    testpuz = get_solver()
    testpuz.puzzle = [[1, 2, 0, 4, 0, 6, 0, 8, 9]]

    # s = header.Section('row', 0)
    row = testpuz.Row()
    result = testpuz.find_missing(row[0])

    assert result.values == [3, 5, 7]
    assert result.locations == [2, 4, 6]


def test_fewest_missing():
    testpuz = get_solver()
    testpuz.puzzle = make_valid_puzzle(solved=False)

    result = testpuz.fewest_missing()
    assert result == header.Section('square', 1)
    # assert result.type == 'row'
    # assert result.idx == 0


def test_put_row():
    testpuz = get_solver()
    testpuz.puzzle = make_test_puzzle('flatrow', False)

    s = header.Section('row', 0)
    test_list = [10 for _ in range(1,10)]
    testpuz.put_section(s, test_list)

    assert testpuz.get_section(s) == test_list


def test_put_col():
    testpuz = get_solver()
    testpuz.puzzle = make_test_puzzle('flatrow', False)

    s = header.Section('col', 0)
    test_list = [10 for _ in range(1, 10)]

    # TEST FUNCTION
    testpuz.put_section(s, test_list)

    assert testpuz.get_section(s) == test_list


def test_put_square():
    testpuz = get_solver()
    testpuz.puzzle = make_test_puzzle('flatrow', False)

    s = header.Section('square', 0)
    test_list = [10 for _ in range(1, 10)]

    # TEST FUNCTION
    testpuz.put_section(s, test_list)

    assert testpuz.get_section(s) == test_list
    assert testpuz.get_section(header.Section('row', 0)) == [10, 10, 10, 1, 1, 1, 1, 1, 1]


def test_set_temp_values_row():
    testpuz = get_solver()

    # 1 row puzzle with 1,3,9 missing
    testpuz.puzzle = [[0, 2, 0, 4, 5, 6, 7, 8, 0]]
    s = header.Section('row', 0)

    # TEST FUNCTION
    testpuz.set_temp_values(s)

    assert testpuz.get_section(s) == [[1, 3, 9], 2, [1, 3, 9], 4, 5, 6, 7, 8, [1, 3, 9]]
    # assert testpuz.get_section(header.Section('row', 0)) == [10, 10, 10, 1, 1, 1, 1, 1, 1]


def test_set_temp_values_col():
    testpuz = get_solver()

    # 1 column puzzle with 2, 4, 6, missing
    testpuz.puzzle = [[1], [0], [3], [0], [5], [0], [7], [8], [9]]

    s = header.Section('col', 0)

    # TEST FUNCTION
    testpuz.set_temp_values(s)

    assert testpuz.get_section(s) == [1, [2, 4, 6], 3, [2, 4, 6], 5, [2, 4, 6], 7, 8, 9]


def test_set_temp_values_square():
    testpuz = get_solver()

    # 1 square puzzle with 5,7,8 missing
    testpuz.puzzle = [[1, 2, 3], [4, 0, 6], [0, 0, 9]]
    s = header.Section('square', 0)
    testpuz.set_temp_values(s)

    assert testpuz.get_section(s) == [1, 2, 3, 4, [5, 7, 8], 6, [5, 7, 8], [5, 7, 8], 9]

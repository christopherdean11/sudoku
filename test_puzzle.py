from unittest import TestCase

import puzzle


def get_puzzle_obj():
    return puzzle.Puzzle()


def make_puzzle(mode: str, zero_slant: bool) -> list:
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

    testpuz = get_puzzle_obj()
    testpuz.puzzle = test_list

    assert testpuz.get_row(0) == [1, 1, 1]
    assert testpuz.get_row(1) == [2, 2, 2]


def test_get_col():
    # use [1 for _ in range(9)]
    test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

    testpuz = get_puzzle_obj()
    testpuz.puzzle = test_list

    assert testpuz.get_col(0) == [1, 2, 3]
    assert testpuz.get_col(1) == [1, 2, 3]


def test_get_square():

    # get puzzle object to inherit functions
    testpuz = get_puzzle_obj()
    # replace puzzle with test puzzle
    testpuz.puzzle = make_puzzle('flatrow', False)

    assert testpuz.get_square(0) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert testpuz.get_square(5) == [4, 4, 4, 5, 5, 5, 6, 6, 6]
    assert testpuz.get_square(8) == [7, 7, 7, 8, 8, 8, 9, 9, 9]


def test_find_missing():
    testpuz = get_puzzle_obj()

    section = [1, 2, 0, 4, 0, 6, 0, 8, 9]
    result = testpuz.find_missing(section)
    assert result.values == [3, 5, 7]
    assert result.locations == [2, 4, 6]



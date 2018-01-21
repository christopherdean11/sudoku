def get_row(puzzle: list, index: int) -> list:
    return puzzle[index]


def get_col(puzzle: list, index: int) -> list:
    col = []
    for row in puzzle:
        # get index'th element for each row
        col.append(row[index])
    return col


def get_square(puzzle: list, index: int) -> list:
    # return a list of the index'th square
    # from (index*3)-3 to index*3

    hstart, hstop, vstart, vstop = get_square_bounds(index)
    sq = []
    for x in range(vstart, vstop):
        sq.extend(puzzle[x][hstart:hstop])
    return sq


def get_square_bounds(index):
    _, hstart = divmod(index, 3)
    hstart *= 3
    hstop = hstart + 3
    vstart, _ = divmod(index, 3)
    vstart *= 3
    vstop = vstart + 3
    return hstart, hstop, vstart, vstop


def put_square(puzzle: list, index: int):
    pass
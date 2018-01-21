from puzzle import Puzzle


class Row(Puzzle):

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __getitem__(self, item):
        return self.puzzle[item]

    def __setitem__(self, key, value):
        self.puzzle[key] = value


class Column(Puzzle):
    # TODO: not sure if this inheritance is needed???
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __getitem__(self, item):
        col = []
        for row in self.puzzle:
            # get index'th element for each row
            col.append(row[item])
        return col

    def __setitem__(self, key, value):
        for i, row in enumerate(self.puzzle):
            row[key] = value[i]


class Square(Puzzle):

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __getitem__(self, item):
        hstart, hstop, vstart, vstop = self._get_square_bounds(item)
        sq = []
        for x in range(vstart, vstop):
            sq.extend(self.puzzle[x][hstart:hstop])
        return sq

    def __setitem__(self, key, value):
        hstart, hstop, vstart, vstop = self._get_square_bounds(key)
        for i, x in enumerate(range(vstart, vstop)):
            self.puzzle[x][hstart:hstop] = value[i * 3:i * 3 + 3]

    def _get_square_bounds(self, index):
        _, hstart = divmod(index, 3)
        hstart *= 3
        hstop = hstart + 3
        vstart, _ = divmod(index, 3)
        vstart *= 3
        vstop = vstart + 3
        return hstart, hstop, vstart, vstop

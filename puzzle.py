"""
Puzzle Class definition
"""
from collections import namedtuple
import header


class Puzzle:
    """
    Puzzle class
    """
    def __init__(self):
        """
        return a new puzzle
        :return: puzzle as a list
        """
        self.puzzle = [[0, 0, 0, 5, 0, 0, 6, 4, 0],
                       [4, 5, 8, 0, 6, 7, 9, 1, 0],
                       [3, 2, 6, 0, 9, 1, 0, 0, 0],
                       [6, 0, 0, 0, 0, 0, 1, 0, 8],
                       [0, 7, 1, 0, 3, 0, 5, 2, 0],
                       [8, 0, 2, 0, 0, 0, 0, 0, 9],
                       [0, 0, 0, 3, 5, 0, 2, 9, 7],
                       [0, 8, 7, 1, 2, 0, 3, 6, 4],
                       [0, 9, 3, 0, 0, 6, 0, 0, 0]]

    def fewest_missing(self) -> namedtuple('Start', 'name loc'):
        """
        return a tuple of (section, index) for the puzzle
        section with the lowest amount of empty spaces
        :param puzzle: puzzle object
        :return: tuple as (section: str, index: int)
        """
        Startpos = namedtuple('Start', 'name loc')

        missing = 9
        best = 0
        # walk through all rows to find least missing values
        for i in range(9):
            temp = self.find_missing(self.get_row(i))
            if len(temp.values) < missing:
                missing = len(temp.values)
                best = Startpos('row', i)

        # walk through all columns to fine least missing values
        for i in range(9):
            if len(self.find_missing(self.get_col(i))) < missing:
                missing = len(self.find_missing(self.get_col(i)))
                best = Startpos('col', i)

        # walk through all squares to find least missing values
        for i in range(9):
            if len(self.find_missing(self.get_square(i))) < missing:
                missing = len(self.find_missing(self.get_square(i)))
                best = Startpos('square', i)

        return best

    def find_missing(self, section: list) -> header.Missing:  # namedtuple('MissingValues', 'values locations'):
        """
        find and return the missing values from a puzzle section as a list
        eventually implement this as the __len__ method on a puzzle Class for Square, Row, Column
        :param section: puzzle section object (square, row, or column)
        :return namedtuple of type Missing(values, locations)
        """
        # Missing = namedtuple('MissingValues', 'values locations')
        Missing = header.Missing
        exists = []
        locs = []
        full_set = range(1, 10)
        missing = []

        # find non-zero spaces in provided section (row,col,sq)
        for idx, element in enumerate(section):
            if element != 0:
                # get a list of elements that do exist
                exists.append(element)
            elif element == 0:
                # get a list of the blank locations
                locs.append(idx)

        # walk through full_set (ints 1-9) and create a list called missing with missing values
        for value in full_set:
            if value not in sorted(exists):
                missing.append(value)

        return Missing(missing, locs)

    def get_section(self, section_type, index) -> list:
        if section_type == 'row':
            return self.get_row(index)
        elif section_type == 'col':
            return self.get_col(index)
        elif section_type == 'square':
            return self.get_square(index)

    def get_row(self, index: int) -> list:
        return self.puzzle[index]

    def get_col(self, index: int) -> list:
        col = []
        for row in self.puzzle:
            # get index'th element for each row
            col.append(row[index])
        return col

    def get_square(self, index: int) -> list:
        # return a list of the index'th square
        # from (index*3)-3 to index*3

        _, hstart = divmod(index, 3)
        hstart *= 3
        hstop = hstart + 3

        vstart, _ = divmod(index, 3)
        vstart *= 3
        vstop = vstart + 3
        sq = []
        for x in range(vstart, vstop):
            sq.extend(self.puzzle[x][hstart:hstop])
        return sq

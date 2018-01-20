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

    def fewest_missing(self) -> header.Section:
        """
        return a tuple of (section, index) for the puzzle
        section with the lowest amount of empty spaces
        :param puzzle: puzzle object
        :return: tuple as (section: str, index: int)
        """
        missing_count = 9
        best = header.Section('null', 0)
        # walk through all rows to find least missing values
        section_types = ['row', 'col', 'square']
        for sec in section_types:
            best, missing_count = self._fewest_missing_from_section(best, missing_count, sec)

        return best

    def _fewest_missing_from_section(self, best: header.Section, missing_count: int, section_type: str):
        """
        sub routine for fewest_missing, gets the fewest missing from all possible sections (row, col, sq)
        :param best: namedtuple (Section) with fewest missing so far in search
        :param missing_count: number of best case missing items found so far
        :param section_type: string ('row', 'col', or 'square)
        :return: new best (or best as passed if no new best found), and missing count
        """
        for i in range(9):
            # make a Section to slice the puzzle by
            s = header.Section(section_type, i)
            # get the missing values for the Section
            temp = self.find_missing(s)

            # if length of missing values is a new low, store this section info and count
            if len(temp.values) < missing_count:
                missing_count = len(temp.values)
                best = header.Section(section_type, i)

        return best, missing_count

    def find_missing(self, section: header.Section) -> header.Missing:  # namedtuple('MissingValues', 'values locations'):
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

        elements = self.section_to_list(section)

        # find non-zero spaces in provided section (row,col,sq)
        for idx, element in enumerate(elements):
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

    def section_to_list(self, section: header.Section) -> list:
        """
        convert a Section to a list
        :param section: namedtuple Section(type (row,col,square), idx(0-8))
        :return: flat 1 dimensional list
        """

        # extract row as list
        if section.type == 'row':
            return self.get_row(section.idx)

        # extract column as list
        elif section.type == 'col':
            return self.get_col(section.idx)

        # extract square as a list
        elif section.type == 'square':
            return self.get_square(section.idx)


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

    def puzzle_print(self):
        for x in range(9):
            for y in range(9):

                if (y % 3 == 0) and y > 0:
                    print('| ', end='')
                if self.puzzle[x][y] == 0:
                    self.puzzle[x][y] = ' '
                print(self.puzzle[x][y], end=' ')

            if ((x + 1) % 3 == 0) and x < 8:
                print('\n----------------------', end='')
            print('')
            # print(' '.join(map(str, puz[x])))

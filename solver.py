import solver_helper
import header
from puzzle import Puzzle


class Solver(Puzzle):

    def get_section(self, section: header.Section) -> list:

        # extract row as list
        if section.type == 'row':
            return solver_helper.get_row(self.puzzle, section.idx)

        # extract column as list
        elif section.type == 'col':
            return solver_helper.get_col(self.puzzle, section.idx)

        # extract square as a list
        elif section.type == 'square':
            return solver_helper.get_square(self.puzzle, section.idx)

    def put_section(self, section: header.Section, flat_list: list):

        if section.type == 'row':
            # insert row into puzzle
            self.puzzle[section.idx] = flat_list

        if section.type == 'col':
            # for each row, update index "idx" with flat_list[row_n]
            for i, row in enumerate(self.puzzle):
                row[section.idx] = flat_list[i]

        if section.type == 'square':
            raise NotImplementedError

    def fewest_missing(self) -> header.Section:
        """
        return a Section type with the least amount of empty spaces
        :return: Section type with least empties
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

    def find_missing(self, section_to_search: header.Section) -> header.Missing:
        """
        find and return the missing values from a puzzle section as a list
        eventually implement this as the __len__ method on a puzzle Class for Square, Row, Column
        :param section_to_search: puzzle section object (square, row, or column)
        :return namedtuple of type Missing(values, locations)
        """
        # Missing = namedtuple('MissingValues', 'values locations')
        Missing = header.Missing
        exists = []
        locs = []
        full_set = range(1, 10)
        missing = []

        elements = self.get_section(section=section_to_search)

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
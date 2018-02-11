import header
from sections import Sections


class Solver:

    def __init__(self, puzzle):
        s = Sections(puzzle)
        self.row = s.make('row')
        self.col = s.make('col')
        self.sq = s.make('sq')

    def solve_puzzle(self):
        self.__set_temp_vals(self.row)
        self.__set_temp_vals(self.col)
        self.__set_temp_vals(self.sq)
        i = 0
        while not self.is_puzzle_complete():
            self.__check_temp_vals(self.row)
            self.__check_temp_vals(self.col)
            self.__check_temp_vals(self.sq)
            i += 1
        # print('completed in {} rounds\n'.format(i))


    def is_puzzle_complete(self):

        r = self.__is_sectiontype_valid(self.row)
        c = self.__is_sectiontype_valid(self.col)
        sq = self.__is_sectiontype_valid(self.sq)

        if r and c and sq:
            return True
        else:
            return False

    def __is_sectiontype_valid(self, section_type) -> bool:

        # for all row/col/squares
        for n in range(0, 9):

            # if not valid, stop checking and return False
            if not self.__is_section_valid(section_type, n):
                return False

        # if get to the end, section is valid (haven't returned False yet)
        return True

    def __is_section_valid(self, section_type, index) -> bool:

        s = section_type[index]

        for element in s:
            if type(element) == list:
                return False

        if sorted(s) == list(range(1, 10)):
            return True
        else:
            return False

    def __set_temp_vals(self, section_type):

        for r in range(0, 9):
            msgv = self.find_missing(section_type[r])

            for l in msgv.locations:
                temps = []
                for val in msgv.values:
                    temps.append(val)
                section_type[r][l] = temps

    def __check_temp_vals(self, section_type):
        badvals = []
        for index in range(0, 9):
            for subidx, element in enumerate(section_type[index]):
                if type(element) == list:
                    badvals = []
                    for tempv in element:
                        if tempv in section_type[index]:
                            # if index == 3:
                            # print('found: ' + str(tempv))
                            badvals.append(tempv)
                    self.__remove_invalid_temps(section_type, index, subidx, badvals)


    def __remove_invalid_temps(self, section_type, idx, subidx, badvals):
        s = section_type[idx]
        for val in badvals:
            s[subidx].remove(val)
        section_type[idx] = s
        self.__is_final_temp(section_type, idx)

    def __is_final_temp(self, section_type, n):
        for i, el in enumerate(section_type[n]):
            if type(el) == list:
                if len(el) == 1:
                    # workaround while the setter does not support col[x][n] = m syntax
                    s = section_type[n]
                    s[i] = el[0]
                    section_type[n] = s

    def find_missing(self, section: list) -> header.Missing:
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

        # elements = self.get_section(section=section_to_search)

        # find non-zero spaces in provided section (row,col,sq)
        for idx, element in enumerate(section):
            if element != 0 and type(element) != list:
                # get a list of elements that do exist
                exists.append(element)
            elif element == 0 or type(element)==list:
                # get a list of the blank locations
                locs.append(idx)

        # walk through full_set (ints 1-9) and create a list called missing with missing values
        for value in full_set:
            if value not in exists:
                missing.append(value)

        return Missing(missing, locs)
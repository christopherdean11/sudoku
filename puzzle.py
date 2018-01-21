"""
Puzzle Class definition
"""
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

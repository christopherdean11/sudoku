"""
testing out finding missing values in a puzzle row

"""
import header
import solver
import sections


def main():
    """
    docstring for main
    :return: n/a
    """
    pz = get_puzzle()
    solv = solver.Solver(pz)

    s = sections.Sections(pz)
    row = s.make('row')
    col = s.make('col')
    sq = s.make('sq')

    # prettyprintpuzzle(pz.copy())

    set_temp_vals(solv, row)

    check_temp_vals(col)

    set_temp_vals(solv, col)
    check_temp_vals(row)

    set_temp_vals(solv, sq)
    check_temp_vals(sq)

    check_temp_vals(row)
    check_temp_vals(col)

    check_temp_vals(col)

    check_temp_vals(row)
    check_temp_vals(col)

    prettyprintpuzzle(puzzle=pz)


def check_temp_vals(section_type):
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
                remove_invalid_temps(section_type, index, subidx, badvals)


def remove_invalid_temps(section_type, idx, subidx, badvals):
    s = section_type[idx]
    for val in badvals:
        s[subidx].remove(val)
    section_type[idx] = s
    is_final_temp(section_type, idx)


def is_final_temp(section_type, n):
    for i, el in enumerate(section_type[n]):
        if type(el) == list:
            if len(el) == 1:
                # workaround while the setter does not support col[x][n] = m syntax
                s = section_type[n]
                s[i] = el[0]
                section_type[n] = s


def set_temp_vals(solv, section_type):

    for r in range(0, 9):
        msgv = solv.find_missing(section_type[r])

        for l in msgv.locations:
            temps = []
            for val in msgv.values:
                temps.append(val)
            section_type[r][l] = temps


def get_puzzle():
    return [[0, 0, 0, 5, 0, 0, 6, 4, 0],
              [4, 5, 8, 0, 6, 7, 9, 1, 0],
              [3, 2, 6, 0, 9, 1, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 1, 0, 8],
              [0, 7, 1, 0, 3, 0, 5, 2, 0],
              [8, 0, 2, 0, 0, 0, 0, 0, 9],
              [0, 0, 0, 3, 5, 0, 2, 9, 7],
              [0, 8, 7, 1, 2, 0, 3, 6, 4],
              [0, 9, 3, 0, 0, 6, 0, 0, 0]]


def prettyprintpuzzle(puzzle):
    out = []
    for row in range(0, 9):
        for col in range(0, 9):
            if (col % 3 == 0) and col > 0:
                out.append('|')
            if puzzle[row][col] == 0:
                puzzle[row][col] = ' '
            out.append(puzzle[row][col])

        if ((row + 1) % 3 == 0) and row < 8:
            out.append('\n------------')
        out.append('\n')
    print(''.join([str(x) for x in out]))


if __name__ == "__main__":
    main()
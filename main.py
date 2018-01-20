"""
testing out finding missing values in a puzzle row

"""
import header
import puzzle as puz


def main():
    """
    docstring for main
    :return: n/a
    """
    mypuzzle = puz.Puzzle()
    start = mypuzzle.fewest_missing()
    print('start location: ', start.type, start.idx)
    # set_temp_values()

    # mypuzzle.get_section()
    # mypuzzle.find_missing()
    # print(mypuzzle.find_missing(mypuzzle.get_section(start.name, start.loc)))


def set_temp_values(section: list, position: int, temp_vals: list)->list:
    section[position] = temp_vals
    return section


if __name__ == "__main__":
    main()
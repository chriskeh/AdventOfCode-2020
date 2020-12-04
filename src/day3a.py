#!/usr/bin/env /usr/bin/python36

input_data_file = "day3.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Three parameters
        a list of lists which is the representation of the input data
        the number of lines in the file
        the number of columns in the file
    """

    my_list = []
    lines = 0
    with open(input_file, 'r') as f:
        for line in f:
            # line = line.rstrip('\n')
            line_list = [char for char in line.rstrip('\n')]
            my_list.append(line_list)
            lines += 1
    columns = len(line_list)
    return my_list, lines, columns


def walk_through_the_forest(forest, max_col_index, max_line_index, col_step, line_step):
    """
    Check how many trees are encountered for the given parameters
    :param forest: a list of list representing the forest
    :param max_col_index:
    :param max_line_index:
    :param col_step:
    :param line_step:
    :return: the number of encountered trees
    """

    # We do one jump as a start and then dive into the loop
    current_line = line_step
    current_col = col_step
    trees = 0
    while current_line <= max_line_index:
        # print("At {}, {} the value is {}".format(current_line, current_col, forest[current_line][current_col]))
        if forest[current_line][current_col] == "#":
            trees += 1
        current_line += line_step
        current_col += col_step
        if current_col > max_col_index:
            current_col = (current_col % max_col_index) - 1
    return trees


def main():

    # The parameters for the jump: 3 right and 1 down
    col_step = 3
    line_step = 1

    # read the input data
    # input_data_file = "day3_test.data"
    forest, total_lines, total_columns = slurp_input(input_data_file)

    # indexing starts at 0, so wa have to subtract 1 from the numbers to get the maximum valid index
    max_line_index = total_lines - 1
    max_col_index = total_columns - 1

    total = 1
    jump_list = [ (1,1), (3, 1), (5,1), (7,1), (1,2)]
    for elem in jump_list:
        trees = walk_through_the_forest(forest, max_col_index, max_line_index, elem[0], elem[1])
        print("Trees: {}".format(trees))
        total *= trees

    print("Total: {}".format(total))



if __name__ == "__main__":
    main()

#!/usr/bin/env /usr/bin/python36
import re

input_data_file = "day18.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of strings, each string is a line of the input file
    """
    with open(input_file) as f:
    #     my_list = list(f)

        my_list = [x.strip() for x in f.readlines()]
    return my_list


def calculate(equation):
    """
    calculate an equation according to the rules given in AoC2020 Day18
    :param equation:
    :return:
    """
    result = 0
    partial = -1
    operation = "undefined"

    while len(equation) > 0:
        character = equation[0]
        if re.match("[0-9]", character):
            if partial == -1:
                partial = int(character)
            else:
                if operation == "addition":
                    partial += int(character)
                elif operation == "multiplication":
                    partial *= int(character)
        elif re.match("\+", character):
            operation = "addition"
        elif re.match("\*", character):
            operation = "multiplication"
        elif re.match("\(", character):
            equation, temp = calculate(equation[1:])
            if partial == -1:
                if character == '(':
                    partial = temp
                else:
                    partial = int(character)
            else:
                if operation == "addition":
                    partial += temp
                elif operation == "multiplication":
                    partial *= temp
        elif re.match("\)", character):
            return equation, partial
        else:
            print("Oops an unknown character '{}' has been found".format(equation[0]))
            exit(1)

        equation = equation[1:]

    return equation, partial


def calculate_sum(list_of_equations):
    """
    For each line in the given list call a method calculate that does the calculation on this line. The results of the
    equations are added together and the final sum is returned.
    :param list_of_equations:
    :return:
    """
    result = 0
    for zeile in list_of_equations:
        zeile = zeile.replace(" ", "")  # blanks are just distracting
        ignore, temp = calculate(zeile)
        result += temp
    return result


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day18_test.data"

    all_equations = slurp_input(input_data_file)
    total = calculate_sum(all_equations)


    print("Total: {}".format(total))


if __name__ == "__main__":
    main()

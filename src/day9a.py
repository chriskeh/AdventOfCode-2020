#!/usr/bin/env /usr/bin/python36

input_data_file = "day9.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of integers representing the numbers n the input file
    """
    with open(input_file) as f:
        my_list = list(f)
    my_list = list(map(int, my_list))
    return my_list


def check_sum(nrs, current, index, preamble_count):
    """
    Check if any two of the numbers in the list "nrs" in the range from "index" to "index + preamble_count"
    sum up to "current"
    :param nrs:     the list of numbers
    :param current: the number that should be matched
    :param index:   the first number that should be used
    :param preamble_count: the amount of numbers in the list that can be used
    :return: True if any of those two numbers um up to be identically to current
             False otherwise
    """

    for i in range(index, index + preamble_count - 1):
        for j in range(i + 1, index + preamble_count):
            # print("In check_sum: i={}".format(i))
            foo = nrs[i] + nrs[j]
            if foo == current:
                return True
    return False


def find_smallest_invalid(list_of_numbers, length):
    """
    Implement day9a of Advent Of Code 2020
    :param list_of_numbers: the input data
    :param length: the length of the preamble
    :return: the smallest number that is invalid
    """
    preamble_index = 0
    while True:
        current_index = preamble_index + length
        current_nr = list_of_numbers[current_index]
        # print("current_index: {} ({})".format(current_index, current_nr))
        if current_index == len(list_of_numbers):
            # Oops end of numbers reached
            current_nr = -1
            print("End Of Numbers reached")
            break

        if not check_sum(list_of_numbers, current_nr, preamble_index, length):
            break

        preamble_index += 1

    return current_nr


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day9_test.data"
    # preamble_count = 5
    preamble_count = 25

    all_numbers = slurp_input(input_data_file)

    smallest_invalid = find_smallest_invalid(all_numbers, preamble_count)

    if smallest_invalid== -1:
        # All numbers matched, so we didn't find a number that broke us
        print("Sorry nothing found")
    else:
        print("Your result: {}".format(smallest_invalid))   # Should be 556543474


if __name__ == "__main__":
    main()

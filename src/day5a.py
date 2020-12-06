#!/usr/bin/env /usr/bin/python36
import re

input_data_file = "day5.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Three parameters
        a list of lists which is the representation of the input data
        the number of lines in the file
        the number of columns in the file
    """

    with open(input_file) as f:
        my_list = f.read().rsplit("\n")

    return my_list


def decode_bsp(bsp):
    """
    Decode a seat according to the rules of Day 5 of Advent Of Code 2020
    Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified
    like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
    (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the
    whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back
     64 through 127). The next letter indicates which half of that region the seat is in, and so on until
     you're left with exactly one row.

    For example, consider just the first seven characters of FBFBBFFRLR:

        Start by considering the whole range, rows 0 through 127.
        F means to take the lower half, keeping rows 0 through 63.
        B means to take the upper half, keeping rows 32 through 63.
        F means to take the lower half, keeping rows 32 through 47.
        B means to take the upper half, keeping rows 40 through 47.
        B keeps rows 44 through 47.
        F keeps rows 44 through 45.
        The final F keeps the lower of the two, row 44.

    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the
    plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps.
    L means to keep the lower half, while R means to keep the upper half.

    :param bsp: binary space partitioning of a seat
    :return: seat number
    """

    return 4711


def get_highest_seat(all_bsp):

    maximum_seat = 0
    for current_bsp in all_bsp:
        current_seat = decode_bsp(current_bsp)
        if current_seat > maximum_seat:
            maximum_seat = current_seat
    return maximum_seat


def main():

    # read the input data
    # input_data_file = "day5_test.data"
    all_bsp = slurp_input(input_data_file)
    print(all_bsp)

    highest_seat = get_highest_seat(all_bsp)

    print("Highest seat number: {}".format(highest_seat))



if __name__ == "__main__":
    main()

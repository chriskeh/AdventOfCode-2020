#!/usr/bin/env /usr/bin/python36

input_data_file = "day14.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of tupels. Each tupel represents a line from the file.
    One of these tupels is either
    - 2 elements: A mask, e.g. ('mask', 'XXX00010101010XX01XX')
    - or 3 elements: a store command ('store', <address>, <value>)
      e.g. ('store', '1', '4711') or in other words: put 4711 into address 1)


    """
    my_commands = []
    with open(input_file, 'r') as f:
        while True:
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()
            left, equal_sign, right = line.split(' ')
            if left == "mask":
                my_commands.append((left, right))
            else:
                nothing, location = left.split('[')
                location = location.rstrip(']')
                my_commands.append(("store", location, right))

    return my_commands


def mask_and_value(current_mask, value):
    """
    apply the rules of Day14a AoC2020
    :param current_mask: A mask read from the input file
    :param value: a decimal number
    :return: the calculated number
    """
    bin_value = bin(value)[2:].zfill(len(current_mask))
    list_of_chars = []      # A list that holds chars, "0" or "1" representing a binary number
    for (char1, char2) in zip(current_mask, bin_value):
        if char1 == "X":
            list_of_chars.append(char2)
        else:
            list_of_chars.append(char1)
    result = ''.join(list_of_chars)     # make a single string from the list of "0" and "1"

    return int(result, 2)           # return the integer that was represented by the string of "0" and "1"


def run_program(input_data):
    """
    walk over the list of tupels that was created from the input file
    Either set the new mask or calculate the value and store it into the right address
    :param input_data: the list of tuples
    :return: a dictionary representing the memory state at the end
    e.g. {7: 101, 8: 64}  (== Address 7 holds 101, address 8 holds 64)
    """
    my_memory = dict()
    for zeile in input_data:
        if zeile[0] == "mask":
            current_mask = zeile[1]
        elif zeile[0] == "store":
            my_memory[int(zeile[1])] = mask_and_value(current_mask, int(zeile[2]))
    return my_memory


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day14_test.data"

    all_input = slurp_input(input_data_file)

    memory = run_program(all_input)

    total = 0
    for number in memory.values():
        total += int(number)

    print("Total: {}".format(total))    # 14925946402938


if __name__ == "__main__":
    main()

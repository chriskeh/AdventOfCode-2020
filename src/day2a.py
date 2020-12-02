#!/usr/bin/env /usr/bin/python36

input_data_file = "day2.data"


def slurp_input(input_file):
    """
    Read the input file. It contains one number per line.
    Reading it in the with-statement creates a list of strings, not numbers.
    So a second command is necessary, which applies the function 'int' to the iterable 'my_list' which
    converts each element of the iterable into an int and then create a list from that again.  Et voila!
    :param input_file:
    :return: list of integers
    """

    my_list = []
    with open(input_file, 'r') as f:
        for line in f:
            my_list.append(line.rstrip('\n'))
    return my_list


def count_valid_passwords_a(input_data_list):
    """
    Find the number of matching passwords as described in day2a of Advent Of Code 2020
    :param input_data_list: list read from the file.
        Each elem is a list of three elements: e.g. [ '1-3', 'l', 'abcdel' ]
    :return: number of elements in the list that match
    """
    valids = 0
    for elem in input_data_list:
        raw_list = elem.split(' ')
        raw_range = raw_list[0]
        raw_char = raw_list[1]
        password = raw_list[2]

        lower_limit, upper_limit = raw_range.split('-')
        key_char = raw_char[0]

        result = len([x for x in password if x == key_char])
        if int(lower_limit) <= result <= int(upper_limit):
            valids += 1

    return valids


def count_valid_passwords_b(input_data_list):
    """
    Find the number of matching passwords as described in day2b of Advent Of Code 2020
    :param input_data_list: list read from the file.
        Each elem is a list of three elements: e.g. [ '1-3', 'l', 'abcdel' ]
    :return: number of elements in the list that match
    :param input_data_list:
    :return:
    """
    valids = 0
    for elem in input_data_list:
        raw_list = elem.split(' ')
        raw_range = raw_list[0]
        raw_char = raw_list[1]
        password = raw_list[2]

        pos1, pos2 = raw_range.split('-')
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1

        key_char = raw_char[0]

        if password[pos1] == key_char:
            if password[pos2] != key_char:
                valids += 1
        else:
            if password[pos2] == key_char:
                valids += 1

    return valids


def main():
    input_data_list = slurp_input(input_data_file)

    print("Valid passwords (a): {}".format(count_valid_passwords_a(input_data_list)))
    print("Valid passwords (b): {}".format(count_valid_passwords_b(input_data_list)))


if __name__ == "__main__":
    main()

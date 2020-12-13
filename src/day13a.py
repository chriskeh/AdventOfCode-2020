#!/usr/bin/env /usr/bin/python36
from pprint import pprint

input_data_file = "day13.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two values:
        1) the earliest departure
        2) A list of sets. Each set represents the given answers in a group.
    """

    with open(input_file, 'r') as f:
        point_in_time = int(f.readline().rstrip())
        lines_raw = f.readline().rstrip()
        elems = lines_raw.split(',')
        elems = list(set(elems))
        elems.remove('x')
        elems = [int(x) for x in elems]

    return point_in_time, elems


def slurp_input_b(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A dict of offsets for each bus
    """
    offset = dict()
    index = 0
    with open(input_file, 'r') as f:
        ignore = int(f.readline().rstrip())
        lines_raw = f.readline().rstrip()
        elems = lines_raw.split(',')
        for elem in elems:
            if elem != 'x':
                offset[int(elem)] = index
            index += 1

    return int(elems[0]), offset

def calculate_departure(moment, list_of_lines):
    """
    Calculate the bus line and the waiting time for this line.
    Advent of Code, Day 13a
    :param moment: A timestamp in seconds where you could leave
    :param list_of_lines: The bus lines
    :return: two values:
        1) the number of the busline that arrives next
        2) the waiting time for this busline
    """
    shortest_waittime = 20000000000
    my_line = 0
    waittime = dict()
    for bus in list_of_lines:
        missed = moment % bus
        waittime[bus] = bus - missed
        if waittime[bus] < shortest_waittime:
            shortest_waittime = waittime[bus]
            my_line = bus
    # return 4711, 10
    return my_line, shortest_waittime


def calculate_day13b(first_bus, start_in_time, offsets):
    """
    Method for Day13 b

    :param first_bus: The number of the first bus
    :param start_in_time: The starting point (this is handy for testing vs production)
    :param offsets: the dictionary that holds the offsets for all given busses
                The bus numbe is the key and the offset is its value
    :return: The first point in time that matches
    """

    current_time = start_in_time
    while True:
        match = True
        for key, value in offsets.items():
            if (current_time + value) % key != 0:
                match = False
                break
        if match:
            return(current_time)

        current_time += first_bus


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day13_test.data"


    # earliest_time_to_leave, all_buslines = slurp_input(input_data_file)
    #
    # line_id, waittime = calculate_departure(earliest_time_to_leave, all_buslines)
    # result = line_id * waittime
    # print("Bus: {}, waittime: {}, result: {}".format(line_id, waittime, result))

    first_bus, offsets = slurp_input_b(input_data_file)
    pprint(offsets)

    start_in_time = 100000000000000
    # start_in_time = 0

    timestamp = calculate_day13b(first_bus, start_in_time, offsets)
    print(timestamp)
    # print("Total: {}".format(total))


if __name__ == "__main__":
    main()

#!/usr/bin/env /usr/bin/python36

input_data_file = "day13.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two values:
        1) the earliest departure
        2) A list of sets. Each set represents the given answers in a group.
    """
    my_answers = []
    this_answer = set()

    with open(input_file, 'r') as f:
        point_in_time = int(f.readline().rstrip())
        lines_raw = f.readline().rstrip()
        elems = lines_raw.split(',')
        elems = list(set(elems))
        elems.remove('x')
        elems = [int(x) for x in elems]

    return point_in_time, elems

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


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day13_test.data"


    earliest_time_to_leave, all_buslines = slurp_input(input_data_file)

    line_id, waittime = calculate_departure(earliest_time_to_leave, all_buslines)
    result = line_id * waittime
    print("Bus: {}, waittime: {}, result: {}".format(line_id, waittime, result))

    # print("Total: {}".format(total))


if __name__ == "__main__":
    main()

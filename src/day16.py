#!/usr/bin/env /usr/bin/python36
from pprint import pprint

from ranges import RangeSet, Range

input_data_file = "day16.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    bereiche = RangeSet()
    with open(input_file, 'r') as f:
        while True:
            # Read a line.
            line = f.readline()
            line = line.strip()

            if line != "":
                ignore, r1, or_ignore, r2 = line.split(" ")

                temp_low, temp_high = r1.split("-")
                neu = Range(start=int(temp_low), end=int(temp_high), include_end=True)
                bereiche = bereiche.union(neu)

                temp_low, temp_high = r2.split("-")
                neu = Range(start=int(temp_low), end=int(temp_high), include_end=True)
                bereiche = bereiche.union(neu)

            else:
                # The line is empty.
                break

        line = f.readline()     # ignore the empty line
        line = f.readline()     # ignore the line "your ticket:"
        my_ticket = f.readline()
        line = line.strip()
        my_ticket = line.split(',')
        my_ticket = [int(i) for i in my_ticket]


        ignore = f.readline()
        ignore = f.readline()

        ticket_liste = []
        while True:
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()
            new = line.split(',')
            new = [int(i) for i in new]
            ticket_liste.append(new)

    return bereiche, my_ticket, ticket_liste


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day16_test.data"

    bereiche, my_ticket, list_of_nearby_tickets = slurp_input(input_data_file)
    # print(bereiche)

    error_rate = 0
    for ticket in list_of_nearby_tickets:
        for number in ticket:
            check = Range(start=number, end=number, include_start=True, include_end=True)
            if bereiche.isdisjoint(check):
                # print(number)
                error_rate += number
    # print(my_ticket)
    # print(list_of_nearby_tickets)

    print("Error Rate: {}".format(error_rate))


if __name__ == "__main__":
    main()

#!/usr/bin/env /usr/bin/python36
from pprint import pprint

input_data_file = "day11.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of lists. Each list is a row of seats.
    """
    my_seat_map = []

    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            # row = line.strip()
            row = ".{}.".format(line.strip())
            my_seat_map.append(list(row))

    # Now pimp the seat_plan with a leading and a trailing row of floor
    floor_row = ['.'] * len(row)
    my_seat_map.insert(0, floor_row)
    my_seat_map.append(floor_row)

    return my_seat_map


def play_once(local_seat_map):
    """
    Just make one iteration of the game of seats
    :param local_seat_map:
    :return: new seat_map
    """
    # print("Play Once")
    new_map = []
    # It's not enough to create a copy of the list of lists. It would just create a new list that holds the
    # same pointers to the rows. So we have to create a copy of each row and append those new copies again to
    # a new list of lists.
    for line in local_seat_map:
        new_map.append(line.copy())

    for i_index in range(1, len(local_seat_map) - 1):
        row = local_seat_map[i_index]
        for j in range(1, len(row) - 1):
            # If the current location is floor, nothing to do
            if row[j] == '.':
                continue
                
            if row[j] == 'L':
                surrounding_empty = True
                for x_index in range(i_index - 1, i_index + 2):
                    for y_index in range(j - 1, j + 2):
                        if local_seat_map[x_index][y_index] == '#':
                            surrounding_empty = False
                if surrounding_empty:
                    new_map[i_index][j] = "#"

            elif row[j] == '#':
                occupied_seats = 0
                for x_index in range(i_index - 1, i_index + 2):
                    for y_index in range(j - 1, j + 2):
                        # ignore the seat itself
                        if x_index == i_index and y_index == j:
                            continue

                        if local_seat_map[x_index][y_index] == '#':
                            occupied_seats += 1

                if occupied_seats >= 4:
                    new_map[i_index][j] = 'L'

    return new_map


def play_seat_game_of_life(seat_map):
    """
    For a given seat_map run the rules of Day11 of Advent Of Code until the seating doesn't change anymore
    :param seat_map: A list of lists representing the seat plan
    :return: the new seat_map
    """
    count = 0   # A safety net to not run forever
    while True:
        new_seat_map = play_once(seat_map)

        if seat_map == new_seat_map:
            return new_seat_map
        else:
            seat_map = new_seat_map

        if count > 1000:
            return []
        count += 1


def count_occupied_seats(local_seat_map):
    """
    Count all occupied seats in the given seatmap

    :param local_seat_map:
    :return: number of occ. seats
    """
    occupied = 0
    for i_index in range(1, len(local_seat_map) - 1):
        row = local_seat_map[i_index]
        for j in range(1, len(row) - 1):
            # If the current location is floor, nothing to do
            if row[j] == '#':
                occupied += 1

    return occupied


def main():

    # uncomment the next line to read the input data from the test file
    input_data_file = "day11.data"

    seat_map = slurp_input(input_data_file)

    stable_seat_map = play_seat_game_of_life(seat_map)
    # stable_seat_map = play_once(seat_map)

    # pprint(stable_seat_map)

    total = count_occupied_seats(stable_seat_map)

    print("Total: {}".format(total))


if __name__ == "__main__":
    main()

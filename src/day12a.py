#!/usr/bin/env /usr/bin/python36
from pprint import pprint

input_data_file = "day12.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    my_answers = []
    this_answer = set()

    my_commands=[]
    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()
            my_commands.append(line)

    return my_commands


def get_degree_from_direction(wohin):
    """

    :param wohin: given direction could be N, E, S, W
    :return: would be 0, 90, 180, 270
    """
    if wohin == "N":
        return 0
    elif wohin == "E":
        return 90
    elif wohin == "S":
        return 180
    elif wohin == "W":
        return 270
    return 42


def get_direction_from_degree(new_degree):
    """
    Make a direction from a given value in degree
    E.g. 90 ==> E
    0 == N
    180 == S
    -90 == W
    :param new_degree:
    :return:
    """
    while new_degree > 270:
        new_degree -= 360

    while new_degree < -270:
        new_degree += 360
    new_dir = "X"
    if new_degree == 0:
        new_dir = "N"
    elif new_degree == 90 or new_degree == -270:
        new_dir = "E"
    elif new_degree == 180 or new_degree == -180:
        new_dir = "S"
    elif new_degree == 270 or new_degree == -90:
        new_dir = "W"
    return new_dir


def new_direction(wohin, degree):
    """
    Make a rotation and calculate new direction.
    E.g. wohin == "E" and degree = 180, then return W
    E.g. wohin == "N" and degree = -90, then return W
    E.g. wohin == "S" and degree = 270, then return E
    :param wohin: current direction, e.g. N, E, S, W
    :param degree: how much to turn
    :return:
    """
    current = get_degree_from_direction(wohin)
    new_degree = current + degree

    return get_direction_from_degree(new_degree)


def walk_a_bit(walking_direction, e_w_position, n_s_position, count):

    if walking_direction == "N":
        n_s_position += count
    elif walking_direction == "S":
        n_s_position -= count
    elif walking_direction == "E":
        e_w_position += count
    elif walking_direction == "W":
        e_w_position -= count

    return e_w_position, n_s_position


def do_one_step(command, wohin, e_w, n_s):
    exec = command[0]
    count = int(command[1:])
    if exec == "F":
        e_w, n_s = walk_a_bit(wohin, e_w, n_s, count)
    elif exec == "R":
        wohin = new_direction(wohin, count)
    elif exec == "L":
        wohin = new_direction(wohin, -count)
    else:
        # Now we have N, E, S or W and a number
        e_w, n_s = walk_a_bit(exec, e_w, n_s, count)

    return wohin, e_w, n_s


def sail_the_ship(list_commands, face, e_w, n_s):
    
    for command in list_commands:
        # print("Blick: {}, command: {}, Position: {}, {}".format(face, command, e_w, n_s))
        face, e_w, n_s = do_one_step(command, face, e_w, n_s)
        # print("New: Blick: {}, Position: {}, {}".format(face, e_w, n_s))
    
    return face, e_w, n_s
    pass


def main():

    # uncomment the next line to read the input data from the test file
    input_data_file = "day12.data"

    all_commands = slurp_input(input_data_file)
    
    start_direction = "E"
    new_direction, east_west, north_south = sail_the_ship(all_commands, start_direction, 0, 0)
    
    print("Manhattan distance: ({} + {}) {}".format(east_west, north_south, abs(east_west) + abs(north_south)))


if __name__ == "__main__":
    main()

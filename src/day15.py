#!/usr/bin/env /usr/bin/python36

def play_game_and_return_nth_number(start_numbers, nth_number):
    """
    Play game according the rules of AoC2020, Day15a
    :param start_numbers: the list of starting numbers
    :param nth_number: how many iterations?
    :return: the value of the nth iteration
    """
    previous = dict()
    pre_previous = dict()
    turn = 1
    for nr in start_numbers:
        previous[nr] = turn
        last_spoken = nr
        turn += 1

    while turn <= nth_number:
        if not last_spoken in pre_previous.keys():
            last_spoken = 0
            if last_spoken in previous.keys():
                pre_previous[last_spoken] = previous[last_spoken]
            previous[last_spoken] = turn
        else:
            if not last_spoken in previous.keys():
                # first time we see this number
                # let's store in which turn we saw it
                previous[last_spoken] = turn
                last_spoken = 0
            else:
                last_spoken = previous[last_spoken] - pre_previous[last_spoken]
                if not last_spoken in previous.keys():
                    previous[last_spoken] = turn
                else:
                    pre_previous[last_spoken] = previous[last_spoken]
                    previous[last_spoken] = turn

        turn += 1

    return last_spoken


def main():

    # uncomment the next line to read the input data from the test file
    input_data = [0, 14, 6, 20, 1, 4]

    result = play_game_and_return_nth_number(input_data, 2020)
    print("Result a: {}".format(result))

    result = play_game_and_return_nth_number(input_data, 30000000)
    print("Result b: {}".format(result))


if __name__ == "__main__":
    main()

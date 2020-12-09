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

    for i in range(index, index + preamble_count - 1):
        for j in range(i + 1, index + preamble_count):
            # print("In check_sum: i={}".format(i))
            foo = nrs[i] + nrs[j]
            if foo == current:
                return True
    return False


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day9_test.data"
    # preamble_count = 5
    preamble_count = 25

    all_numbers = slurp_input(input_data_file)
    # print(all_numbers)

    preamble_index = 0
    while True:
        current_index = preamble_index + preamble_count
        current_nr = all_numbers[current_index]
        # print("current_index: {} ({})".format(current_index, current_nr))
        if current_index == len(all_numbers):
            # Oops end of numbers reached
            current_nr = -1
            print("End Of Numbers reached")
            break

        if not check_sum(all_numbers, current_nr, preamble_index, preamble_count):
            break

        preamble_index += 1

    if current_nr== -1:
        # All numbers matched, so we didn't find a number that broke us
        print("Sorry nothing found")
    else:
        print("Your result: {}".format(current_nr))



if __name__ == "__main__":
    main()

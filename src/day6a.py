#!/usr/bin/env /usr/bin/python36
import re

input_data_file = "day6.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    my_answers = []
    this_answer = set()

    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                my_answers.append(this_answer)
                break

            line = line.strip()
            if line != "":
                for answer in line:
                    this_answer.add(answer)
            else:
                # The line is empty.
                # Prepare for next block: Add this_passport to the list, empty this_passport and increase passport_index.
                my_answers.append(this_answer)
                this_answer = set()
                continue

    return my_answers


def slurp_input_b(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of lists of sets. Each list is a group and each set represents the given answers per person
    """
    my_answers = []
    this_group = []
    this_answer = set()

    with open(input_file, 'r') as f:
        while True:
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                my_answers.append(this_group)
                break

            line = line.strip()
            if line != "":
                this_person = set()
                for answer in line:
                    this_person.add(answer)     # a set with answers of this person
                this_group.append(this_person)  # add that set to the list for this group
            else:
                # The line is empty.
                # Prepare for next block: Add this_group to the list, empty this_group
                my_answers.append(this_group)
                this_group = []
                continue

    return my_answers


def main():

    # read the input data
    # input_data_file = "day6_test.data"

    all_answers = slurp_input(input_data_file)

    total = 0
    for elem in all_answers:
        total += len(elem)

    print("Total: {}".format(total))

    all_everyone = slurp_input_b(input_data_file)

    total = 0
    for group in all_everyone:
        valid_answers = group[0]
        for i in range(1, len(group)):
            # print("valid_answers: {}; group[{}]: {}".format(valid_answers, i, group[i]))
            valid_answers = valid_answers.intersection(group[i])
        total += len(valid_answers)

    print("Total: {}".format(total))

if __name__ == "__main__":
    main()

#!/usr/bin/env /usr/bin/python36

input_data_file = "day4.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Three parameters
        a list of lists which is the representation of the input data
        the number of lines in the file
        the number of columns in the file
    """

    my_passports = []
    this_passport = {}
    passport_index = 0
    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # print("Line is: {}".format(line))
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                my_passports.append(this_passport)
                break

            line = line.strip()
            # print("Passport Index: {}".format(passport_index))
            if line != "":
                # print("WORK")
                for elem in line.split(" "):
                    key, value = elem.split(":")
                    this_passport[key] = value
            else:
                # The line is empty.
                # Prepare for next block: Add this_passport to the list, empty this_passport and increase passport_index.
                # print("::EMPTY LINE::")
                # print("passport Index {}, Passport: {}".format(passport_index, this_passport))
                my_passports.append(this_passport)
                this_passport = {}
                passport_index += 1
                continue

    return my_passports



def calculate_valid_passports(all_passports):
    """
    Gets a list of dictionaries that represent all passports.
    Validates if passports are valid according to AdventOfCode 2020 Day 4
    :param all_passports:
    :return: just the number of valid passports
    """
    my_valids = 0
    for my_passport in all_passports:
        if len(my_passport.keys()) == 8:
            # 8 fields is perfect
            print("Valid (8 keys): {}".format(my_passport))
            my_valids += 1
        elif len(my_passport.keys()) == 7:
            if not "cid" in my_passport.keys():
                # only cid is missing: OK
                print("Valid (7 keys without cid): {}".format(my_passport))
                my_valids += 1

    return my_valids


def main():

    # read the input data
    # input_data_file = "day4_test.data"
    all_passports = slurp_input(input_data_file)
    # print(all_passports)

    number_of_valid_passports = calculate_valid_passports(all_passports)

    print("Total: {}".format(number_of_valid_passports))



if __name__ == "__main__":
    main()

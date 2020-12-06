#!/usr/bin/env /usr/bin/python36
import re

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
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                my_passports.append(this_passport)
                break

            line = line.strip()
            if line != "":
                for elem in line.split(" "):
                    key, value = elem.split(":")
                    this_passport[key] = value
            else:
                # The line is empty.
                # Prepare for next block: Add this_passport to the list, empty this_passport and increase passport_index.
                my_passports.append(this_passport)
                this_passport = {}
                passport_index += 1
                continue

    return my_passports


def is_year_in_range(value, minimum, maximum):
    """
    given datum has to be >= minimum and <= maximum
    """
    if minimum <= int(value) <= maximum:
        return True

    return False


def is_valid_height(height):
    # a number followed by either cm or in:
    #
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    if len(height) < 4:
        return False

    size_num = int(height[:-2])
    units = height[-2:]

    if units == "in":
        return is_year_in_range(size_num, 59, 76)
    elif units == "cm":
        return is_year_in_range(size_num, 150, 193)
    else:
        return False


def is_valid_haircolor(color):
    # a # followed by exactly six characters 0-9 or a-f
    result = re.match("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", color)
    if result:
        return True
    else:
        return False
    return True


def is_valid_eyecolor(color):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def is_valid_passport_id(passport_id):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    result = re.match("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", passport_id)
    if result:
        return True
    else:
        return False


def validate_field_of_passport(key, value):
    """
    Validate a single field of the passport.

    :param key:
    :param value:
    :return:
    """
    if key == "byr":
        # byr (Birth Year) - four digits; at least 1920 and at most 2002
        return is_year_in_range(value, 1920, 2002)
    elif key == "iyr":
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return is_year_in_range(value, 2010, 2020)
    elif key == "eyr":
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
        return is_year_in_range(value, 2020, 2030)
    elif key == "hgt":
        return is_valid_height(value)
    elif key == "hcl":
        return is_valid_haircolor(value)
    elif key == "ecl":
        return is_valid_eyecolor(value)
    elif key == "pid":
        return is_valid_passport_id(value)
    elif key == "cid":
        return True
    else:
        print("ERROR: Invalid field: {}".format(key))
        return False


def all_fields_are_OK(one_passport):
    """
    Validate all rules from Day4 of AdventOfCode 2020

    :param one_passport: A dictionary representing a passport
    :return: True or False
    """
    state = True
    for key,value in one_passport.items():
        state &= validate_field_of_passport(key, value)

    return state


def calculate_valid_passports(all_passports):
    """
    Gets a list of dictionaries that represent all passports.
    Validates if passports are valid according to AdventOfCode 2020 Day 4
    :param all_passports:
    :return: just the number of valid passports
    """
    my_valids = 0
    for my_passport in all_passports:
        if len(my_passport.keys()) == 8 or (len(my_passport.keys()) == 7 and not "cid" in my_passport.keys()):
            if all_fields_are_OK(my_passport):
                my_valids += 1

    return my_valids


def main():

    # read the input data
    # input_data_file = "day4_test.data"
    all_passports = slurp_input(input_data_file)

    number_of_valid_passports = calculate_valid_passports(all_passports)

    print("Total: {}".format(number_of_valid_passports))



if __name__ == "__main__":
    main()

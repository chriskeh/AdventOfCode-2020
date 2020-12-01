#!/usr/bin/env /usr/bin/python36

input_data_file = "day1a.data"

def slurp_input(input_file):
    """
    Read the input file. It contains one number per line.
    Reading it in the with-statement creates a list of strings, not numbers.
    So a second command is necessary, which applies the function 'int' to the iterable 'my_list' which
    converts each element of the iterable into an int and then create a list from that again.  Et voila!
    :param input_file:
    :return: list of integers
    """
    with open(input_file) as f:
        my_list = list(f)
    my_list = list(map(int, my_list))
    return my_list


def multiply_sum_2020(input_list):
    """
    Find the two values in the given list that sum up to 2020. Then multiply those two values and return the product.
    :param input_list: A list with integers.
    :return: The product of those two numbers that add up to 2020
             Or -1 if none of the numbers sum up to 2020.
    """
    for pos1 in range(0, len(input_list) - 1):
        for pos2 in range(pos1 + 1, len(input_list)):
            sum = input_list[pos1] + input_list[pos2]
            if sum == 2020:
                print("Values are: {} and {}".format(input_list[pos1], input_list[pos2]))
                product = input_list[pos1] * input_list[pos2]
                return product

    return -1



input_data_list = slurp_input(input_data_file)
final_product = multiply_sum_2020(input_data_list)

print("The product is: {}".format(final_product))



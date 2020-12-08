#!/usr/bin/env /usr/bin/python36
import re

input_data_file = "day7.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: 1)  a list of all found colors
             2) a dict of lists. Key is a color, the list for a color are those colors that
                contain a bag with the key color

    """
    found_colors = []
    hold_dict = {}

    with open(input_file, 'r') as f:
        while True:
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()

            start = re.sub(" bags contain .*", "", line)
            # print("Start: X {} X".format(start))
            found_colors.append(start)

            # m = re.search('.* bags contain (.*$)', line)
            # remaining = m.group(1)
            remaining = re.sub(".* bags contain ", "", line)
            # print("Remaining: X {} X".format(remaining))

            if remaining != "no other bags.":
                rest_colors = remaining.split(",")
                # print("Rest: {}".format(rest_colors))
                for elem in rest_colors:
                    elem = re.sub("\s*[0-9]+ ", "", elem)
                    elem = re.sub(" bag.*", "", elem)
                    # print("Elem: X{}X".format(elem))
                    try:
                        hold_dict[elem].append(start)
                    except:
                        hold_dict[elem] = [start]

    return found_colors, hold_dict


def main():

    # uncomment the next line to read the input data from the test file
    input_data_file = "day7_test.data"

    all_colors, holder = slurp_input(input_data_file)

    # create a dict that holds True or False to keep track if a color has been checked already
    status = {}
    for color in all_colors:
        status[color] = False

    # print("Status: {}".format(status))
    # print("Holder: {}".format(holder))

    found_colors = holder["shiny gold"]
    while True:
        # for each iteration we need to see, if all colors have been checked
        # so let's set this to True.  When we worked on a color further down in the for-loop, we AND this and the
        # status of the color
        check_exit = True
        for color in found_colors:

            try:
                # append the colors that contain the current color to the list of found colors
                found_colors.extend(holder[color])
                # make sure that the list is unique (convert to set and then to list again)
                myset = set(found_colors)
                found_colors = list(myset)
                # and set check_exit
                check_exit &= status[color]
            except KeyError:
                # This happens when trying to access holder[color] for a color that is not in the dict 'holder'
                # In that case no other color holds this color, so we have nothing more to do here
                # print("Nothing to do for {}".format(color))
                pass

            # store that we dealt with this color (to not revisit and count a color multiple times)
            status[color] = True

        # check_ext will be True, when we run the for-loop above and all colors in the list found_colors have been
        # already handled. That means for all colors we already found the containing bags.
        # If one color in found_colors has not been yet handled, check_exit will be flipped to False and we
        # run another iteration of the while-loop
        if check_exit:
            break

    print("Result: {} colors : {}".format(len(found_colors), found_colors))


if __name__ == "__main__":
    main()

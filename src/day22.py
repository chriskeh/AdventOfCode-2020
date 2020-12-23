#!/usr/bin/env /usr/bin/python36

input_data_file = "day22.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    my_answers = []
    this_answer = set()

    player1 = []
    player2 = []
    with open(input_file, 'r') as f:
        f.readline()    # read "Player 1:"
        while True:
            # Read a line.
            line = f.readline().strip()
            if line != "":
                player1.append(int(line))
            else:
                break

        f.readline()    # read "Player 2:"
        while True:
            # Read a line.
            line = f.readline().strip()
            if line != "":
                player2.append(int(line))
            else:
                break

    return player1, player2


def play(player1, player2):

    while player1 and player2:
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
        else:
            player2.append(player2[0])
            player2.append(player1[0])

        player1 = player1[1:]
        player2 = player2[1:]

    if player1:
        return player1
    else:
        return player2



def calculate_winners_cards(winners_cards):
    result = 0
    multiplicator = 1
    for nr in winners_cards[::-1]:
        result += nr * multiplicator
        multiplicator += 1

    return result


def main():

    # uncomment the next line to read the input data from the test file
    input_data_file = "day22.data"

    player1, player2 = slurp_input(input_data_file)

    winners_cards = play(player1, player2)

    total = calculate_winners_cards(winners_cards)

    print("Total: {}".format(total))


if __name__ == "__main__":
    main()

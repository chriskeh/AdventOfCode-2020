#!/usr/bin/env /usr/bin/python36

input_data_file = "day22.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two lists, one for each player
    """
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
    """
    PLay a game of combat, AoC2020 Day22a
    :param player1:
    :param player2:
    :return: the deck of the winner
    """
    while player1 and player2:
        if player1[0] > player2[0]:
            # player1 wins, add his and the other card to the bottom of the deck
            player1.append(player1[0])
            player1.append(player2[0])
        else:
            # player2 wins, add his and the other card to the bottom of the deck
            player2.append(player2[0])
            player2.append(player1[0])

        # need to remove the first card for each player, copy the slice from listitem1 to the end for each list
        player1 = player1[1:]
        player2 = player2[1:]

    # return the winners cards
    if player1:
        return player1
    else:
        return player2


def calculate_winners_cards(winners_cards):
    """
    Calculate the final sum. Last card in deck times 1, second last card times 2, ....
    Let's reverse the list, then we can iterate over the range and just do the math.
    :param winners_cards:
    :return:
    """
    result = 0
    liste = winners_cards[::-1]
    for i in range(0, len(liste)):
        result += liste[i] * (i + 1)

    return result


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day22_test.data"

    player1, player2 = slurp_input(input_data_file)
    winners_cards = play(player1, player2)
    total = calculate_winners_cards(winners_cards)
    print("Total: {}".format(total))


if __name__ == "__main__":
    main()

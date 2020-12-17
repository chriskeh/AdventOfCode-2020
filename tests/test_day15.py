import pytest

from src.day15 import play_game_and_return_nth_number


@pytest.mark.parametrize("starting_numbers, expected",
                         [
                             ([0, 3, 6], 436),
                             ([1, 3, 2], 1),
                             ([2, 1, 3], 10),
                             ([1, 2, 3], 27),
                             ([2, 3, 1], 78),
                             ([3, 2, 1], 438),
                             ([3, 1, 2], 1836),
                          ]
                         )
def test__play_game_and_return_202th_number(starting_numbers, expected):
    result = play_game_and_return_nth_number(starting_numbers, 2020)
    assert result == expected

@pytest.mark.parametrize("starting_numbers, expected",
                         [
                             ([0, 3, 6], 436),
                             ([1, 3, 2], 1),
                             ([2, 1, 3], 10),
                             ([1, 2, 3], 27),
                             ([2, 3, 1], 78),
                             ([3, 2, 1], 438),
                             ([3, 1, 2], 1836),
                          ]
                         )
def test__play_game_and_return_30000000th_number(starting_numbers, expected):
    result = play_game_and_return_nth_number(starting_numbers, 30000000)
    assert result == expected
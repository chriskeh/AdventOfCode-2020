import pytest

from src.day13a import calculate_day13b

@pytest.mark.parametrize("start, my_dict, expected",
                         [
                            (17, {17: 0, 13: 2, 19: 3}, 3417),
                            (67, {67: 0, 7: 1, 59: 2, 61: 3}, 754018),
                            (67, {67: 0, 7: 2, 59:3, 61:4}, 779210),
                             (67, {67: 0, 7: 1, 59: 3, 61: 4}, 1261476),
                             (1789, {1789: 0, 37: 1, 47: 2, 1889: 3}, 1202161486),

                         ]
                         )
def test_calculate_day13b(start, my_dict, expected):
    # my_dict = {17: 0, 13: 2, 19:3}
    # expected = 3417
    result = calculate_day13b(start, 0, my_dict)
    print("Result: {}".format(result))
    assert result == expected


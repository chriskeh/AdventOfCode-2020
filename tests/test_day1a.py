import pytest

from src.day1a import multiply_sum_2020, multiply_sum_2020_three


@pytest.mark.parametrize("input_list, expected",
                         [([2000, 11, 12, 1999, 21], 41979),
                          ([2,9,10,3,2,3,11,0,99,30,40,50], -1)],
                         )
def test_multiply_sum_2020(input_list, expected):

    result = multiply_sum_2020(input_list)

    assert result == expected

@pytest.mark.parametrize("input_list, expected",
                         [([2000, 11, 9, 1999, 21], 198000),
                          ([2,9,10,3,2,3,11,0,99,30,40,50], -1)],
                         )
def test_multiply_sum_2020_three(input_list, expected):

    result = multiply_sum_2020_three(input_list)

    assert result == expected

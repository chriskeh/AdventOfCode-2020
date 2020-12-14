import pytest

from src.day14a import mask_and_value


@pytest.mark.parametrize("mask, value, expected",
                         [
                             ("XXXXXXXX", "67", 67),
                             ("XXXXXXXX", "3", 3),
                             ("XXXXXX0X", "3", 1),
                             ("XXXXXXX0", "3", 2),
                             ("XXXXXX1X", "3", 3),
                             ("XXXXX1XX", "3", 7),
                          ]
                         )
def test__mask_and_value(mask, value, expected):
    result = mask_and_value(mask, value)
    assert result == expected

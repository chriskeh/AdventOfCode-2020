import pytest

from src.dayx import your_method_here


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
def test__your_method_here(mask, value, expected):
    result = your_method_here(mask, value)
    assert result == expected

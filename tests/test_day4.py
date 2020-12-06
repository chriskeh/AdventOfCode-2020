import pytest

from src.day4a import is_valid_passport_id, is_valid_haircolor, is_valid_height


@pytest.mark.parametrize("passport_id, expected",
                         [("012345678", True),
                          ("000000000", True),
                          ("01234567890", False),
                          ("000000---0", False),
                          ("abcdefghij", False),
                          ("012", False)],
                         )
def test_is_valid_passport_id(passport_id, expected):

    result = is_valid_passport_id(passport_id)

    assert result == expected


@pytest.mark.parametrize("color, expected",
                         [("#aaaaaa", True),
                          ("#012345", True),
                          ("0123456", False),
                          ("#00000", False),
                          ("#abcdex", False),
                          ("#123abz", False),
                          ("123abc", False),
                          ("012", False)],
                         )
def test_is_valid_haircolor(color, expected):

    result = is_valid_haircolor(color)

    assert result == expected


@pytest.mark.parametrize("height, expected",
                         [("60in", True),
                          ("190cm", True),
                          ("190in", False),
                          ("190", False),
                          ("84", False),
                          ("190xy", False),
                          ("200cm", False),
                         ]
                        )
def test_is_valid_height(height, expected):

    result = is_valid_height(height)

    assert result == expected
import pytest

from src.day12a import get_direction_from_degree, new_direction, do_one_step


@pytest.mark.parametrize("degree, direction",
                         [(0, "N"),
                          (-90, "W"),
                          (180, "S"),
                          (90, "E"),
                          ]
                         )
def test_get_direction_from_degree(degree, direction):
    result = get_direction_from_degree(degree)
    assert result == direction


@pytest.mark.parametrize("wohin, degree, new_wohin",
                         [("N", 0, "N"),
                          ("W", 0, "W"),
                          ("N", 90, "E"),
                          ("N", 180, "S"),
                          ("N", -180, "S"),
                          ("N", -90, "W"),
                          ("W", -270, "N"),
                          ("N", 270, "W"),
                          ]
                         )
def test_new_direction(wohin, degree, new_wohin):
    result = new_direction(wohin, degree)
    assert result == new_wohin\

@pytest.mark.parametrize("command, face, e_w, n_s, expected_face, expected_e_w, expected_n_s",
                         [("F10", "E", 0, 0, "E", 10, 0),
                          ("F10", "S", 0, 0, "S", 0, -10),
                          ("N10", "W", 0, 0, "W", 0, 10),
                          ("W10", "W", 0, 0, "W", -10, 0),
                          ("R180", "W", 0, 0, "E", 0, 0),
                          ("R270", "W", 0, 0, "S", 0, 0),
                          ("R90", "W", 0, 0, "N", 0, 0),
                          ("R90", "E", 0, 0, "S", 0, 0),
                          ("L90", "N", 0, 0, "W", 0, 0),
                          ("L90", "W", 0, 0, "S", 0, 0),
                          ("L90", "S", 0, 0, "E", 0, 0),
                          ("L90", "E", 0, 0, "N", 0, 0),

                          ]
                         )
def test__do_one_step(command, face, e_w, n_s, expected_face, expected_e_w, expected_n_s):

    face, e_w, n_s = do_one_step(command, face, e_w, n_s)
    assert face == expected_face
    assert e_w == expected_e_w
    assert n_s == expected_n_s

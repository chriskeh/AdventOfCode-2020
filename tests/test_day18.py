import pytest

from src.day18 import calculate


@pytest.mark.parametrize("equation, expected",
                         [
                             ("2*(2+(3*3))", 22),
                             ("(2*3)*(4+8)", 72),
                             ("2+(2*3)", 8),
                             ("2+(2+3*3)", 17),
                             ("2*3+(4*5)", 26),
                             ("5+(8*3+9+3*4*3)", 437),
                             ("5*9*(7*3*3+9*3+(8+6*4))", 12240),
                             ("1+2", 3),
                             ("2*2", 4),
                             ("2*2+1", 5),
                             ("2*2*3", 12),
                             ("2+2*3", 12),
                             ("2+(2*3)", 8),
                             ("((2+4*9)*(6+9*8+6)+6)+2+4*2", 13632),
                          ]
                         )
def test__calculate(equation, expected):
    nix, result = calculate(equation)
    assert result == expected
    assert nix == ''


def test__calculate2():
    nix, result = calculate("(2*3)*(4+8)")
    assert result == 72
    assert nix == ''

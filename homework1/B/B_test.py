import B
import pytest


@pytest.mark.parametrize("firstScore,secondScore,gameSign,expected", [
    ((0,0), (0,0), 1, 1),
    ((0,0), (0,0), 2, 1),
    ((0,2), (0, 3), 1, 5),
    ((0,2), (0, 3), 2, 6),
    ((3,2), (0, 1), 2, 0),
    ((3,2), (0, 2), 2, 1),
    ((3,2), (3, 2), 2, 0),
    ((3,2), (3, 2), 1, 0),
    ((0,1), (1,0), 1, 1),
    ((0,1), (1,0), 2, 1),
    ((4, 5), (2, 3), 1, 3),
    ((0,1), (0,0), 1, 2),
    ((0,1), (0,0), 2, 2),
    ((2,2), (1,1), 2, 0),
    ((1,1), (1, 4), 1, 3)])
def test_getsRequiredGoals(firstScore, secondScore, gameSign, expected):
    assert B.getRequiredGoals(firstScore, secondScore, gameSign) == expected
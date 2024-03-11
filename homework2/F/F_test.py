import F
import pytest

@pytest.mark.parametrize("prizes, minAngleSpeed, maxAngleSpeed, speedReduction, expected", [
    ([707, 805, 279, 713, 584, 352, 923, 1000, 237], 29, 38, 1, 1000),
    ([1, 2, 3, 4, 5], 3, 5, 2, 5),
    ([1, 2, 3, 4, 5], 15, 15, 2, 4),
    ([5, 4, 3, 2, 1], 2, 5, 2, 5),
    ([1, 2, 3, 4, 5], 1, 1, 1, 1),
    ([56, 1000, 528, 720, 895, 209, 805, 65, 370, 923, 541, 431, 528, 778, 670, 761, 794, 49, 488, 171, 438, 325, 57, 717, 293, 847, 535, 306, 398, 757, 888, 56, 916, 999], 391, 901, 26, 1000)
    ]
    )
def test_returnMaxprize(prizes, minAngleSpeed, maxAngleSpeed, speedReduction, expected):
    assert F.getBestprize(prizes, minAngleSpeed, maxAngleSpeed, speedReduction) == expected
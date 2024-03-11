import E
import pytest

@pytest.mark.parametrize("berries, expected", [
    ([(1, 5), (8, 2), (4, 4)], (10, [2, 3, 1])),
    ([(7, 6), (7, 4)], (10, [2, 1]))
    ])
def test_returnSegments(berries, expected):
    assert E.getMaxHeight(berries) == expected
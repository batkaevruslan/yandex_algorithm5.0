import G
import pytest

@pytest.mark.parametrize("numbers, expected", [
    ([1, 3, 3, 3, 2], [1, 3, 1]),
    ([1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9], [1, 6, 9]),
    ([7, 2, 3, 4, 3, 2, 7], [2, 3, 2]),
    ([1], [1]),
    ([2, 1], [1, 1])
    ])
def test_returnSegments(numbers, expected):
    assert G.getSegments(numbers) == expected
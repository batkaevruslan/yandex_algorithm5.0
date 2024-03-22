import G
import pytest
from G import Point

@pytest.mark.parametrize("points, expected", [
    (
        [Point(0, 1), Point(1, 0)], 
        [Point(0, 0), Point(1, 1)]
    ),
    (
        [Point(0, 0), Point(1, 1)],
        [Point(0, 1), Point(1, 0)]
    ),
    (
        [Point(0, 2), Point(2, 0), Point(2, 2)],
        [Point(0, 0)]
    ),
    (
        [Point(-1, 1), Point(1, 1), Point(-1, -1), Point(1, -1)],
        []
    ),
    (
        [Point(0, 1), Point(0, 3)], 
        [Point(-1, 2), Point(1, 2)]
    ),
    (
        [Point(0, 0)],
        [Point(1, 0), Point(0, 1), Point(1, 1)]
    ),
    (
        [Point(-2, -2)],
        [Point(-2, -1), Point(-1, -2), Point(-1, -1)]
    ),
    (
        [Point(3, 2), Point(5, 2)],
        [Point(4, 1), Point(4, 3)]
    ),
    (
        [Point(4, 1),Point(3, 2), Point(5, 2)],
        [Point(4, 3)]
    )
])
def test_findsMissingPoints(points, expected):
    result = G.findMissingPoints(points)
    assert set(result) == set(expected)
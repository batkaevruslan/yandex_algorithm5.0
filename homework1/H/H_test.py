import H
import pytest


@pytest.mark.parametrize("l, x1, v1, x2, v2, expected", [
    (6, 3, 1, 1, 1, ("yes", float(1))),
    (12, 8, 10, 5, 20, ("yes", 0.3)),
    (5, 0, 0, 1, 2, ("yes", float(2))),
    (10, 7, -3, 1, 4, ("yes", 0.8571428571)),
    (6, 1, 0, 1, 0, ("yes", 0)),
    (6, 1, 0, 2, 0, ("no", -1)),
    (615143346, 79387687, -80123649, 306422480, -80123649, ("yes", 2.4075923389))
])
def test_getMinimumTime(l, x1, v1, x2, v2, expected):
    answer, time = H.getMinimumTime(l, x1, v1, x2, v2)
    assert answer == expected[0]
    assert abs(time - expected[1]) / max(1, expected[1]) <= pow(10, -9)
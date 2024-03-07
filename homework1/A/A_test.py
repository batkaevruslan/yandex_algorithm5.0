import A    # The code to test
# content of test_expectation.py
import pytest


@pytest.mark.parametrize("p,v,q,m,expected", [
    (0, 7, 12, 5, 25),
    (100, 0, 0, 0, 2),
    (10, 1, 8, 6, 13),
    (8, 6, 10, 1, 13)
    ])
def test_eval(p, v, q, m, expected):
    assert A.getTotalTreeCount(p, v, q, m) == expected

# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
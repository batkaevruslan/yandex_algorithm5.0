import F
import pytest


@pytest.mark.parametrize("nums,expected", [
    ([5, 7, 2], "x+"),
    ([0, 1], "+"),
    ([0, 1, 1], "+x"),
    ([0, 2, 1], "++"),
    ([0, 2, 1, 3], "++x"),
    ([0, 2, 1, 3, 4], "++x+"),
    ([1,1], "x"),
    ([1,1,2], "x+"),
    ([4, -5], "+"),
    ([1, 3, 2, 3, 5], "x+xx"),
    ([2, 2, 1, 3, 2, 3], "++x+x")])
def test_getSignSequence(nums, expected):
    assert F.getSignSequence(nums) == expected
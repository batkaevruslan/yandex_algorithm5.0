import I
import pytest

@pytest.mark.parametrize("board, expected", [
    ([
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ], 3),
    #2
    ([
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ], 0),
    #3
    ([
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ], 5),
    #4
    ([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ], 0),
    #5
    ([
        [1]
    ], 0),
    #6
    ([
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0]
    ], 32),
    #
    ([
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ], 4)
    ])
def test_returnSegments(board, expected):
    assert I.getMinMoveCount(board, len(board)) == expected
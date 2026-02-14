import pytest
from matrix_operations import (
    is_symmetric,
    is_square,
    trace
)


def test_trace_basic():
    assert trace([[1, 2], [3, 4]]) == 5
    assert trace([[5]]) == 5
    assert trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15

def test_trace_not_square():
    with pytest.raises(ValueError):
        trace([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError):
        trace([[1, 2, 3], [4, 5, 6]])

# ----------------------------------------------------------

def test_is_square_true():
    assert is_square([[1, 2], [3, 4]]) is True
    assert is_square([[5]]) is True
    assert is_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) is True

def test_is_square_false():
    assert is_square([[1, 2], [3, 4], [5, 6]]) is False   # 3x2
    assert is_square([[1, 2, 3], [4, 5, 6]]) is False     # 2x3
    assert is_square([]) is False

# ----------------------------------------------------------

def test_is_symmetric_true():
    assert is_symmetric([[1, 2], [2, 3]]) is True
    assert is_symmetric([[5]]) is True
    assert is_symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) is True

def test_is_symmetric_false():
    assert is_symmetric([[1, 2], [3, 4]]) is False
    assert is_symmetric([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) is False

def test_is_symmetric_not_square():
    with pytest.raises(ValueError):
        is_symmetric([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError):
        is_symmetric([[1, 2, 3], [4, 5, 6]])
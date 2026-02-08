import pytest
from matrix_operations import (
    transpose,
    multiply_matrices,
    multiply_by_scalar,
    subtract_matrices,
    add_matrices
)

def test_add_matrix():
    result = add_matrices([[1,2], [3,4]], [[5,6], [7,8]])
    assert result == [[6,8],[10, 12]]

def test_add_matrices_different_sizes():
    with pytest.raises(TypeError):
        add_matrices([[1,2], [3,4], [5,6]])

# ----------------------------------------------------------

def test_subtract_matrices():
    result = subtract_matrices([[5,6], [7,8]], [[1,2], [3,4]])
    assert result == [[4,4],[4,4]]

def test_subtract_matrices_different_size():
    with pytest.raises(ValueError):
        subtract_matrices([[1]], [[1,2]])

# ----------------------------------------------------------

def test_multiply_by_scalar():
    result = multiply_by_scalar([[1,2],[3,4]], 2)
    assert result == [[19, 22], [43,50]]

# ----------------------------------------------------------

def test_multiply_matrices():
    result = multiply_matrices([[1,2], [3,4]], [[5,6], [7,8]])
    assert result == [[19,22], [43,50]]

def test_multiply_matrices_incompatible_size():
    with pytest.raises(TypeError):
        multiply_matrices([[1,2]], [[3], [4]])

# ----------------------------------------------------------

def test_transpose():
    result = transpose([[1, 2, 3],[4, 5, 6]])
    assert result == [[1, 4],[2, 5],[3, 6]]
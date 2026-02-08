import pytest
from matrix_operations import (
    print_matrix,
    matrix_to_list,
    get_cols,
    get_rows,
    set_element,
    get_element
)


def test_get_element_basic():
    matrix = [[1,2], [3,4]]
    element = get_element(matrix, 0, 1)
    assert element == 2

def test_get_element_invalid_index():
    matrix = [[1,2], [3,4]]
    with pytest.raises(IndexError):
        get_element(matrix, 5,5)

# ------------------------------------------

def test_set_element_basic():
    matrix = [[1,2], [3,4]]
    set_element(matrix, 0, 1, 5)
    assert matrix[0][1] == 5
    
# ------------------------------------------

def test_get_rows_basic():
    matrix = [[1,2], [3,4], [5,6]]
    rows = get_rows(matrix)
    assert rows == 3

# ------------------------------------------

def test_get_cols_basic():
    matrix = [[1,2,3], [4,5,6]]
    cols = get_cols(matrix)
    assert cols == 3

# ------------------------------------------

def test_matrix_to_list_basic():
    original = [[1,2], [3,4]]
    copy = matrix_to_list(original)
    assert copy == original
    assert copy is not original
    
    copy[0][0] = 100
    assert original[0][0] == 1

# ------------------------------------------

def test_print_matrix_basic(capsys):
    matrix = [[1,2], [3,4]]
    print_matrix(matrix)
    captured = capsys.readouterr()

    assert "1" in captured.out
    assert "2" in captured.out
    assert "3" in captured.out
    assert "4" in captured.out
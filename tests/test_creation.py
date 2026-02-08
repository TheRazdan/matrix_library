import pytest
import random
from matrix_operations import (
    create_matrix,
    create_matrix_from_list,
    create_random_matrix,
    create_zero_matrix,
    create_iden_matrixtity
)


def test_create_matrix_basic():
    m = create_matrix(2, 3, 0)
    assert len(m) == 2
    assert len(m[0]) == 3

def test_create_matrix_invalid_size():
    with pytest.raises(ValueError):
        create_matrix(0, 5)

# ----------------------------------    

def test_create_identity_matrix_basic():
    """Тест создания базовой единичной матрицы"""
    m = create_iden_matrixtity(3)
    assert len(m) == 3
    assert len(m[0]) == 3

def test_create_identity_matrix_invalid_size():
    """Тест с недопустимым размером"""
    with pytest.raises(ValueError):
        create_iden_matrixtity(0)

# ----------------------------------    

def test_create_zero_matrix_basic():
    """Тест создания базовой нулевой матрицы"""
    m = create_zero_matrix(2, 3)
    assert len(m) == 2
    assert len(m[0]) == 3

def test_create_zero_matrix_invalid_size():
    """Тест с недопустимым размером"""
    with pytest.raises(ValueError):
        create_zero_matrix(0, 5)

# ----------------------------------    

def test_create_random_matrix_basic():
    """Тест создания базовой случайной матрицы"""
    m = create_random_matrix(2, 3, 1, 10)
    assert len(m) == 2
    assert len(m[0]) == 3

def test_create_random_matrix_invalid_size():
    """Тест с недопустимым размером"""
    with pytest.raises(ValueError):
        create_random_matrix(0, 5, 1, 10)

def test_create_random_matrix_invalid_range():
    """Тест с недопустимым диапазоном значений"""
    with pytest.raises(ValueError):
        create_random_matrix(2, 3, 10, 1)

# ---------------------------------- 

def test_create_matrix_from_list_basic():
    """Тест создания матрицы из списка"""
    data = [[1, 2], [3, 4]]
    m = create_matrix_from_list(data)
    assert len(m) == 2
    assert len(m[0]) == 2

def test_create_matrix_from_list_empty():
    """Тест с пустым списком"""
    with pytest.raises(ValueError):
        create_matrix_from_list([])

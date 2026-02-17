from .creation import create_zero_matrix

def add_matrices(matrix1, matrix2):
    """
    Суммирует две матрицы одинакового размера.

    Args:
        matrix1: Первая матрица.
        matrix2: Вторая матрица.

    Returns:
        Сумма матриц.

    Raises:
        ValueError: Если матрицы имеют разные размеры.
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError(f"Матрицы имеют разные размеры: "
                         f"первая {rows1}x{cols1}, вторая {rows2}x{cols2}")
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result


def subtract_matrices(matrix1, matrix2):
    """
    Вычитает вторую матрицу из первой.

    Args:
        matrix1: Матрица, из которой вычитают.
        matrix2: Матрица, которую вычитают.

    Returns:
        Разность матриц.

    Raises:
        ValueError: Если матрицы имеют разные размеры.
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError(f"Матрицы имеют разные размеры: "
                         f"первая {rows1}x{cols1}, вторая {rows2}x{cols2}")
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result


def multiply_by_scalar(matrix, scalar):
    """
    Умножает матрицу на скаляр (числовое значение).

    Args:
        matrix: Исходная матрица.
        scalar: Число, на которое умножается матрица.

    Returns:
        Матрица, умноженная на скаляр.
    """
    rows, cols = len(matrix), len(matrix[0])

    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] * scalar)
        result.append(row)

    return result


def multiply_matrices(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Умножает две матрицы A и B.
    
    Параметры:
        A (list[list[float]]): первая матрица (m x n)
        B (list[list[float]]): вторая матрица (n x p)
    
    Возвращает:
        list[list[float]]: результирующая матрица (m x p)
    
    Исключения:
        ValueError: если матрицы пустые или их размеры несовместимы для умножения
    """
    # Проверка на пустые матрицы
    if not A or not B:
        raise ValueError("Empty matrix")
    
    rows_A = len(A)
    cols_A = len(A[0]) if rows_A > 0 else 0
    rows_B = len(B)
    cols_B = len(B[0]) if rows_B > 0 else 0
    
    if not all(len(row) == cols_A for row in A):
        raise ValueError("Invalid matrix A: rows have different lengths")
    if not all(len(row) == cols_B for row in B):
        raise ValueError("Invalid matrix B: rows have different lengths")
    
    if cols_A != rows_B:
        raise ValueError(f"Incompatible dimensions for multiplication: A columns ({cols_A}) != B rows ({rows_B})")
    
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Умножение матриц
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0.0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    
    return result


def transpose(matrix):
    """
    Выполняет транспонирование матрицы (меняет строки и столбцы местами).

    Args:
        matrix: Исходная матрица.

    Returns:
        Транспонированная матрица.
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Создаем транспонированную матрицу
    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)
    
    return transposed
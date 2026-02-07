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


def multiply_matrices(matrix1, matrix2):
    """
    Перемножает две матрицы (стандартное матричное умножение).

    Args:
        matrix1: Первая матрица.
        matrix2: Вторая матрица.

    Returns:
        Результат умножения матриц.

    Raises:
        ValueError: При несоответствии размеров.
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError(f"Несоответствие размеров для умножения матриц: "
                         f"количество столбцов первой ({cols1}) должно равняться "
                         f"количеству строк второй ({rows2})")
    
    result = create_zero_matrix(rows1, cols2)
    
    for i in range(rows1):
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            result[i][j] = sum_val
    
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
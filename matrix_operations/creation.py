import random

def create_matrix(rows, cols, default_value=0):
    """
    Создаёт матрицу заданного размера, заполняя её указанным значением.

    Args:
        rows: Количество строк.
        cols: Количество столбцов.
        default_value: Значение для заполнения матрицы (по умолчанию 0).

    Returns:
        Созданная матрица.

    Raises:
        ValueError: Если rows ≤ 0 или cols ≤ 0.
    """
    if rows <= 0:
        raise ValueError(f"Количество строк должно быть положительным, получено: {rows}")
    if cols <= 0:
        raise ValueError(f"Количество столбцов должно быть положительным, получено: {cols}")
    
    return [[default_value for _ in range(cols)] for _ in range(rows)]


def create_identity_matrix(n):
    """
    Создаёт единичную матрицу заданного размера.

    Args:
        n: Размер квадратной матрицы (n × n).

    Returns:
        Единичная матрица.

    Raises:
        ValueError: Если n ≤ 0.
    """
    if n <= 0:
        raise ValueError(f"Размер матрицы должен быть положительным, получено: {n}")
    
    matrix = create_zero_matrix(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def create_zero_matrix(rows, cols):
    """
    Создаёт нулевую матрицу заданного размера.

    Args:
        rows: Количество строк.
        cols: Количество столбцов.

    Returns:
        Нулевая матрица.

    Raises:
        ValueError: Если rows ≤ 0 или cols ≤ 0.
    """
    return create_matrix(rows, cols, 0)


def create_random_matrix(rows, cols, min_val, max_val):
    """
    Создаёт матрицу со случайными значениями в указанном диапазоне.

    Args:
        rows: Количество строк.
        cols: Количество столбцов.
        min_val: Минимальное значение (включительно).
        max_val: Максимальное значение (включительно).

    Returns:
        Матрица со случайными значениями.

    Raises:
        ValueError: При неправильном размере или диапазоне.
    """
    if rows <= 0:
        raise ValueError(f"Количество строк должно быть положительным, получено: {rows}")
    if cols <= 0:
        raise ValueError(f"Количество столбцов должно быть положительным, получено: {cols}")
    if min_val > max_val:
        raise ValueError(f"Минимальное значение ({min_val}) не может быть больше максимального ({max_val})")
    
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def create_matrix_from_list(data):
    """
    Создаёт матрицу из готового списка списков, проверяя корректность данных.

    Args:
        data: Список списков целых чисел.

    Returns:
        Корректная матрица.

    Raises:
        ValueError: При неправильных размерах или пустом списке.
    """
    if not data:
        raise ValueError("Список данных не может быть пустым")
    
    if not all(isinstance(row, list) for row in data):
        raise ValueError("Все элементы данных должны быть списками")
    
    rows_count = len(data)
    if rows_count == 0:
        raise ValueError("Матрица должна содержать хотя бы одну строку")
    
    cols_count = len(data[0])
    if cols_count == 0:
        raise ValueError("Строки матрицы должны содержать хотя бы один элемент")

    if not all(len(row) == cols_count for row in data):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if not isinstance(element, int):
                raise ValueError(f"Элемент в позиции [{i}][{j}] должен быть целым числом, получено: {type(element)}")
    
    return [row[:] for row in data]
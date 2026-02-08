def get_element(matrix: list[list[int]], row: int, col: int) -> int:
    """
    Получает элемент матрицы по указанным координатам.

    Args:
        matrix: Матрица в виде списка списков.
        row: Индекс строки (начинается с 0).
        col: Индекс столбца (начинается с 0).

    Returns:
        Значение элемента матрицы по указанным координатам.

    Raises:
        IndexError: Если координаты выходят за пределы матрицы.
    """
    
    if not 0 <= row < len(matrix):
        raise IndexError(f"Индекс строки {row} выходит за пределы матрицы (0-{len(matrix)-1})")
    
    if not 0 <= col < len(matrix[0]):
        raise IndexError(f"Индекс столбца {col} выходит за пределы матрицы (0-{len(matrix[0])-1})")
    
    return matrix[row][col]


def set_element(matrix: list[list[int]], row: int, col: int, value: int) -> None:
    """
    Устанавливает значение элемента матрицы по указанным координатам.

    Args:
        matrix: Матрица в виде списка списков.
        row: Индекс строки (начинается с 0).
        col: Индекс столбца (начинается с 0).
        value: Новое значение элемента.

    Raises:
        IndexError: Если координаты выходят за пределы матрицы.
    """
    
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        raise IndexError(f"Индекс ({row},{col} выходят за границы матрицы {len(matrix)} x {len(matrix[0])})")
    
    matrix[row][col] = value
    

def get_rows(matrix: list[list[int]]) -> int:
    """
    Возвращает количество строк в матрице.

    Args:
        matrix: Матрица в виде списка списков.

    Returns:
        Количество строк в матрице.
    """
    return len(matrix)



def get_cols(matrix: list[list[int]]) -> int:
    """
    Возвращает количество столбцов в матрице.

    Args:
        matrix: Матрица в виде списка списков.

    Returns:
        Количество столбцов в матрице.
    """
    return len(matrix[0]) if matrix else 0


def matrix_to_list(matrix: list[list[int]]) -> list[list[int]]:
    """
    Создаёт глубокую копию матрицы.

    Args:
        matrix: Исходная матрица в виде списка списков.

    Returns:
        Глубокая копия матрицы.
    """
    return [row[:] for row in matrix]


def print_matrix(matrix: list[list[int]]) -> None:
    """
    Выводит матрицу на экран построчно.

    Args:
        matrix: Матрица в виде списка списков.
    """
    for row in matrix:
        print(row)
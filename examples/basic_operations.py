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
    
    if not 0 <= row < len(matrix):
        raise IndexError(f"Индекс строки {row} выходит за пределы матрицы (0-{len(matrix)-1})")
    
    if not 0 <= col < len(matrix[0]):
        raise IndexError(f"Индекс столбца {col} выходит за пределы матрицы (0-{len(matrix[0])-1})")
    
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


# Арифметические операции
def add_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
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
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
    
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]


def subtract_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
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
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры для вычитания")
    
    return [
        [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]


def multiply_by_scalar(matrix: list[list[int]], scalar: int) -> list[list[int]]:
    """
    Умножает матрицу на скаляр.

    Args:
        matrix: Исходная матрица.
        scalar: Число, на которое умножается матрица.

RAZDAN, [24.01.2026 15:29]
Returns:
        Матрица, умноженная на скаляр.
    """
    return [[element * scalar for element in row] for row in matrix]


def multiply_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Перемножает две матрицы (стандартное матричное умножение).

    Args:
        matrix1: Первая матрица размером m×n.
        matrix2: Вторая матрица размером n×p.

    Returns:
        Результат умножения матриц размером m×p.

    Raises:
        ValueError: Если количество столбцов первой матрицы не равно количеству строк второй матрицы.
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError(
            f"Количество столбцов первой матрицы ({cols1}) должно быть равно "
            f"количеству строк второй матрицы ({rows2})"
        )
    
    # Создаем матрицу результатов размером rows1 x cols2, заполненную нулями
    result = [[0] * cols2 for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Выполняет транспонирование матрицы.

    Args:
        matrix: Исходная матрица размером m×n.

    Returns:
        Транспонированная матрица размером n×m.
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def get_element(matrix: list[list[int]],row: int,col: int) -> int:

    """
    Получает элемент матрицы по указанным координатам.

    Args:
        matrix: Матрица в виде списка списков.
        row: Индекс строки (начинается с 0).SS
        col: Индекс столбца (начинается с 0).

    Returns:
        Значение элемента матрицы по указанным координатам.

    Raises:
        IndexError: Если координаты выходят за пределы матрицы.
    """

    if not 0 <= row < len(matrix):
        raise IndexError(f"""RU: Индекс строки {row} выходит за пределы матрицы
                         EN: The row index {row} is outside the matrix""")
    
    if not 0 <= col < len(matrix[0]):
        raise IndexError(f"""RU: Индекс столбца {col} выходит за пределы матрицы
                    EN: The column index {col} is outside the matrix""")

    return matrix[row][col]


def set_element(matrix: list[list[int]], row: int,col: int,value: int) -> None:
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

    if not 0 <= row < len(matrix):
        raise IndexError(f"""RU: Индекс строки {row} выходит за пределы матрицы
                         EN: The row index {row} is outside the matrix""")
    
    if not 0 <= col < len(matrix):
        raise IndexError(f"""RU: Индекс столбца {col} выходит за пределы матрицы
                         EN: The column index {col} is outside the matrix""")
    
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
        print(*row)
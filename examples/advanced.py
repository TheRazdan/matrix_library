def is_square(matrix: list[list[float]]) -> bool:
    """
    Проеряет,является ли матрица квадратной. Пусая матрица 
    считается как 0 x 0 и считается квадратной"""

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True

def trace(matrix: list[list[float]]) -> float:
    """
    Возращаем след квадратной матрицы
    
    выбрасывает ValueError, если матрица не квадратная"""
    
    if not is_square(matrix):
        raise ValueError("Матрица не квадратная")
    return sum(matrix[i][i] for i in range(len(matrix)))
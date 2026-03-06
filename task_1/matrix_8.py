__author__ = "Саргсян Татев ИВТ-23"
import numpy as np
# Задание №678

def transform_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Преобразование матрицы: последнюю строку и последний столбец меняет местами.
    """
    result = matrix.copy()
    idx = matrix.shape[0] - 1

    last_row = matrix[idx, :].copy()
    last_col = matrix[:, idx].copy()

    result[:, idx] = last_row
    result[idx, :] = last_col

    return result


def print_matrix(matrix: np.ndarray):
    n = matrix.shape[0]
    for i in range(n):
        print("  " + " ".join(f"{matrix[i][j]:8.2f}" for j in range(n)))


def main():
    print("Задание 8 | Преобразование матрицы:")
    n = int(input("  Введите порядок матрицы n: "))

    print("  Введите элементы матрицы:")
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            x = float(input(f"    a[{i + 1}][{j + 1}] = "))
            row.append(x)
        rows.append(row)

    matrix = np.array(rows, dtype=float)

    print("\n  Исходная матрица:")
    print_matrix(matrix)

    matrix = transform_matrix(matrix)

    print("\n  Преобразованная матрица:")
    print_matrix(matrix)
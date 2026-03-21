__author__ = "Саргсян Татев ИВТ-23"

import numpy as np

def generate_matrix(n: int) -> np.ndarray:
    """
    Генерирует случайную матрицу размера n x n
    :param n: размер матрицы
    :return: numpy array
    """
    return np.random.rand(n, n)

def solve_linear_system(A: np.ndarray) -> np.ndarray:
    """
    Решает систему Ax = b
    :param A: матрица коэффициентов
    :return: решение x
    """
    n = A.shape[0]
    b = np.random.rand(n)

    x = np.linalg.solve(A, b)

    print("Матрица A:\n", A)
    print("Вектор b:\n", b)
    print("Решение x:\n", x)

    return x


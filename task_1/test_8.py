__author__ = "Саргсян Татев ИВТ-23"

import numpy as np
from task_1.matrix_8 import transform_matrix


def arrays_equal(result: np.ndarray, expected: list) -> bool:
    return np.array_equal(result, np.array(expected, dtype=float))


# ТЕСТ 1: Матрица 1x1 (граничный случай)
m = np.array([[42]], dtype=float)
assert arrays_equal(transform_matrix(m), [[42]]), "Тест 1 провален"
print("Тест 1 пройден: матрица 1x1")

# ТЕСТ 2: Матрица 2x2
# last_row=[3,4], last_col=[2,4]
# новый столбец 2=[3,4], новая строка 2=[2,4]
m = np.array([[1, 2],
              [3, 4]], dtype=float)
assert arrays_equal(transform_matrix(m), [[1, 3],
                                           [2, 4]]), "Тест 2 провален"
print("Тест 2 пройден: матрица 2x2")

# ТЕСТ 3: Матрица 3x3
# last_row=[7,8,9], last_col=[3,6,9]
# новый столбец 3=[7,8,9], новая строка 3=[3,6,9]
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)
assert arrays_equal(transform_matrix(m), [[1, 2, 7],
                                           [4, 5, 8],
                                           [3, 6, 9]]), "Тест 3 провален"
print("Тест 3 пройден: матрица 3x3")

# ТЕСТ 4: Матрица 4x4
# last_row=[13,14,15,16], last_col=[4,8,12,16]
# новый столбец 4=[13,14,15,16], новая строка 4=[4,8,12,16]
m = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12],
              [13, 14, 15, 16]], dtype=float)
assert arrays_equal(transform_matrix(m), [[ 1,  2,  3, 13],
                                           [ 5,  6,  7, 14],
                                           [ 9, 10, 11, 15],
                                           [ 4,  8, 12, 16]]), "Тест 4 провален"
print("Тест 4 пройден: матрица 4x4")

# ТЕСТ 5: Нулевая матрица
m = np.zeros((3, 3), dtype=float)
assert arrays_equal(transform_matrix(m), [[0, 0, 0],
                                           [0, 0, 0],
                                           [0, 0, 0]]), "Тест 5 провален"
print("Тест 5 пройден: нулевая матрица")

# ТЕСТ 6: Отрицательные числа
# last_row=[-7,-8,-9], last_col=[-3,-6,-9]
m = np.array([[-1, -2, -3],
              [-4, -5, -6],
              [-7, -8, -9]], dtype=float)
assert arrays_equal(transform_matrix(m), [[-1, -2, -7],
                                           [-4, -5, -8],
                                           [-3, -6, -9]]), "Тест 6 провален"
print("Тест 6 пройден: отрицательные числа")

# ТЕСТ 7: Дробные числа
# last_row=[7.7,8.8,9.9], last_col=[3.3,6.6,9.9]
m = np.array([[1.1, 2.2, 3.3],
              [4.4, 5.5, 6.6],
              [7.7, 8.8, 9.9]], dtype=float)
assert arrays_equal(transform_matrix(m), [[1.1, 2.2, 7.7],
                                           [4.4, 5.5, 8.8],
                                           [3.3, 6.6, 9.9]]), "Тест 7 провален"
print("Тест 7 пройден: дробные числа")

# ТЕСТ 8: Единичная матрица (симметричная — должна остаться неизменной)
m = np.eye(3, dtype=float)
assert arrays_equal(transform_matrix(m), [[1, 0, 0],
                                           [0, 1, 0],
                                           [0, 0, 1]]), "Тест 8 провален"
print("Тест 8 пройден: единичная матрица")

# ТЕСТ 9: Матрица с одинаковыми элементами (должна остаться неизменной)
m = np.full((3, 3), 5, dtype=float)
assert arrays_equal(transform_matrix(m), [[5, 5, 5],
                                           [5, 5, 5],
                                           [5, 5, 5]]), "Тест 9 провален"
print("Тест 9 пройден: матрица с одинаковыми элементами")

# ТЕСТ 10: Исходная матрица не изменяется (функция не меняет оригинал)
original = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]], dtype=float)
m = original.copy()
transform_matrix(m)
assert np.array_equal(m, original), "Тест 10 провален"
print("Тест 10 пройден: исходная матрица не изменяется")

# ТЕСТ 11: Нули и отрицательные числа вместе
# last_row=[6,-7,0], last_col=[2,-5,0]
m = np.array([[ 0, -1,  2],
              [-3,  0, -5],
              [ 6, -7,  0]], dtype=float)
assert arrays_equal(transform_matrix(m), [[ 0, -1,  6],
                                           [-3,  0, -7],
                                           [ 2, -5,  0]]), "Тест 11 провален"
print("Тест 11 пройден: нули и отрицательные числа")

# ТЕСТ 12: Большие числа
# last_row=[7,8,10**9], last_col=[3,6,10**9]
m = np.array([[10**6, 2,     3    ],
              [4,     5,     6    ],
              [7,     8,     10**9]], dtype=float)
assert arrays_equal(transform_matrix(m), [[10**6, 2,     7    ],
                                           [4,     5,     8    ],
                                           [3,     6,     10**9]]), "Тест 12 провален"
print("Тест 12 пройден: большие числа")

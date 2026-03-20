__author__ = "Саргсян Татев ИВТ-23"

"""
1. [ + ] создать случайную матрицу numpy array
2. [ + ] решить СЛАУ (numpy)
3. [ + ] построить тепловую карту на основе созданной матрицы
4. [ + ] превратить матрицу в массив, построить гистограмму (seaborn)
5. [ + ] построить график любой сложной функции. построить график этой 
    же функции с добавлением шума (numpy, matplotlib); не забудьте подписи 
    к подписи к осям, заголовок графика, легенду, координатную сетку
6. дополнительно: постройте графики выявленных заражений COVID-19 и смертности 
    для нескольких стран данные 
    https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths
    подсказка: используете библиотеку pandas
    можно предложить свой набор данных для графика
"""

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


__author__ = "Саргсян Татев ИВТ-23"

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Строит тепловую карту матрицы
    :param matrix: numpy array
    """
    plt.figure()
    sns.heatmap(matrix, annot=False)
    plt.title("Heatmap матрицы")
    plt.show()


def plot_histogram(matrix: np.ndarray) -> None:
    """
    Строит гистограмму значений матрицы
    :param matrix: numpy array
    """
    data = matrix.flatten()

    plt.figure()
    sns.histplot(data, bins=20)
    plt.title("Гистограмма значений матрицы")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.show()


def plot_functions() -> None:
    """
    Строит функцию и ту же функцию с шумом
    """
    x = np.linspace(0, 10, 100)

    # базовая функция
    y = np.sin(x) * np.exp(-x / 5)

    # добавление шума
    noise = np.random.normal(0, 0.1, size=x.shape)
    y_noise = y + noise

    plt.figure()

    plt.plot(x, y, label="Оригинальная функция")
    plt.plot(x, y_noise, label="С шумом")

    plt.title("Функция и функция с шумом")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


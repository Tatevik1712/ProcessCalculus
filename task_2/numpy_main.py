__author__ = "Саргсян Татев ИВТ-23"

from numpy_graphic import*
from numpy_task import*

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

def main():
    """
    Главная функция
    """
    n = 5

    # 1. Генерация матрицы
    matrix = generate_matrix(n)
    # 2. Решение СЛАУ
    solve_linear_system(matrix)
    # 3. Heatmap
    plot_heatmap(matrix)
    # 4. Histogram
    plot_histogram(matrix)
    # 5. Функции
    plot_functions()

if __name__ == "__main__":
    main()
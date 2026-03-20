__author__ = "Саргсян Татев ИВТ-23"
import math
# Задание №336а

def compute_sum(n: int, x: float) -> float:
    result = 0
    for k in range(1, n + 1):
        numerator = math.factorial(2 * k) + abs(x) # оптимизация факториала
        denominator = math.factorial(k ** 2)
        result += numerator / denominator
    return result


def main():
    print("Задание 7 | Вычисление суммы ряда:")
    n = int(input("  Введите n: "))
    x = float(input("  Введите x: "))

    result = compute_sum(n, x)
    print(f"  Результат суммы: {result}")
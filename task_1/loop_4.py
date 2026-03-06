__author__ = "Саргсян Татев ИВТ-23"
#Задание №115б

def sum_inverse_fifth_power(n: int) -> float:
    """
    Вычисляет сумму: S = Σ 1/k^5, k от 1 до n
    """
    result = 0.0
    for k in range(1, n + 1):
        result += 1 / (k ** 5)
    return result


def main():
    print("Задание 4 | Сумма 1/k^5 от k=1 до n:")
    n = int(input("  Введите натуральное число n: "))

    if n < 1:
        print("  Ошибка: n должно быть натуральным числом (>= 1).")
        return

    result = sum_inverse_fifth_power(n)
    print(f"  S = Σ 1/k^5 (k=1..{n}) = {result:.10f}")
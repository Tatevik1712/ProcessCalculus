__author__ = "Саргсян Татев ИВТ-23"
# Задание №181а

def sum_divisible_by_5(a: list) -> float:
    result = 0
    for x in a:
        if x % 5 == 0:
            result += x
    return result


def main():
    print("Задание 6 | Сумма элементов массива, кратных 5:")
    a = [1, 5, 10, 3, 15, 7, 20, 2, 25, 4] + [0] * 40  # 50 чисел
    print(f"  Список (первые 10): {a[:10]}...")
    print(f"  Сумма кратных 5: {sum_divisible_by_5(a)}")
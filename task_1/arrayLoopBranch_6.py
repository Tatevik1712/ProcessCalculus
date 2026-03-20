__author__ = "Саргсян Татев ИВТ-23"
# Задание №181а


def sum_divisible_by_n(a: list, n: int) -> float:
    """
    Нахождение суммы элементов массива, кратных числу n
    """
    result = 0
    for element in a:
        if element % n == 0:
            result += element
    return result


def main():
    n = int(input("Введите число, относительно которого будут находиться кратные ему числа n: "))
    print(f"Задание 6 | Сумма элементов массива, кратных {n}:")
    a = [1, 5, 10, 3, 15, 7, 20, 2, 25, 4] + [0] * 40  # 50 чисел
    print(f"  Список (первые 10): {a[:10]}...")
    print(f"  Сумма кратных {n}: {sum_divisible_by_n(a, n)}")


if __name__ == "__main__":
    main()
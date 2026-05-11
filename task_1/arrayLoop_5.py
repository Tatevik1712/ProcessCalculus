__author__ = "Саргсян Татев ИВТ-23"
# Задание №136ж

def alternating_sum(a: list) -> float:
    """
    Вычисляет знакочередующуюся сумму элементов списка.
    Формула: a[0] - a[1] + a[2] - a[3] + ...

    :param a: список числовых значений
    :return: знакочередующаяся сумма, округлённая до 2 знаков
    """
    result = 0
    for i in range(len(a)):
        result += ((-1) ** i) * a[i]   # чётный индекс → «+», нечётный → «−»
    return result


def input_array(n: int) -> list:
    """
    Список формируется через list comprehension — компактный способ создания
    списка из n

    :param n: количество элементов
    :return: список вещественных чисел длиной n
    """
    return [float(input(f"  a[{i + 1}] = ")) for i in range(n)]


def main():
    print("Задание 5 | Знакочередующаяся сумма массива:")

    n = int(input("  Введите n: "))

    # Заполняем массив через отдельную функцию:
    # это чище, чем городить цикл прямо внутри main().
    a = input_array(n)

    result = alternating_sum(a)
    print(f"  Результат: {result:.2f}")


if __name__ == "__main__":
    main()
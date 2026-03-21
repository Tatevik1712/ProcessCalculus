__author__ = "Саргсян Татев ИВТ-23"

"""
Генераторная версия программы

Задача:
Дано n. Получить последовательность:
b_i = (2^i) / (i!), i = 1..n
"""

def sequence_generator(n: int):
    """
    Генератор последовательности b_i = (2^i) / (i!)
    :param n: количество элементов
    :yield: очередной элемент последовательности
    """
    term = 2.0  # b1 = 2^1 / 1! = 2

    for i in range(1, n + 1):
        if i == 1:
            yield term
        else:
            # рекуррентная формула:
            # b_i = b_(i-1) * 2 / i
            term = term * 2 / i
            yield term


def main():
    """
    Главная функция
    """
    n = int(input("Введите n: "))
    print(f"Последовательность b_i для n = {n}:")

    for i, value in enumerate(sequence_generator(n), start=1):
        print(f"b{i} = {value}")


if __name__ == "__main__":
    main()
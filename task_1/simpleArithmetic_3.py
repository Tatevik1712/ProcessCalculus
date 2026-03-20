__author__ = "Саргсян Татев ИВТ-23"
# Задание №73


def replace_numbers(k: int, l: int) -> tuple:
    """
    Если k != l — заменяет оба числа бо́льшим из них.
    Если k == l — заменяет оба числа нулями.
    """
    if k != l:
        if k > l:
            l = k
        else:
            k = l
    else:
        k = l = 0
    return k, l


def main():
    print("Задание 3 | Введите два целых числа:")
    k = int(input("  k = "))
    l = int(input("  l = "))

    new_k, new_l = replace_numbers(k, l)
    maximum = k if k > l else l

    print(f"  Исходные значения: k = {k}, l = {l}")
    if k != l:
        print(f"  Числа не равны → заменяем оба на max({k}, {l}) = {maximum}")
    else:
        print("  Числа равны → заменяем оба на 0")
    print(f"  Результат: k = {new_k}, l = {new_l}")


if __name__ == "__main__":
    main()
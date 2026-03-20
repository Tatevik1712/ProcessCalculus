__author__ = "Саргсян Татев ИВТ-23"
# Задание №35б

def compute(x: float, y: float, z: float) -> float:
    """
    Вычисляет: max²(a = x + y + z/2, b = xyz) + 1
    """
    a = x + y + z / 2
    b = x * y * z
    if a > b:
        return a ** 2 + 1
    else:
        return b ** 2 + 1


def main():
    print("Задание 2 | Введите x, y, z:")
    x = float(input("  x = "))
    y = float(input("  y = "))
    z = float(input("  z = "))

    a = x + y + z / 2
    b = x * y * z
    maximum = a if a > b else b

    print(f"  x + y + z/2 = {a}")
    print(f"  xyz         = {b}")
    print(f"  max         = {maximum}")
    print(f"  Результат   = {compute(x, y, z)}")


if __name__ == "__main__":
    main()
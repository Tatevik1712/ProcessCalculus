__author__ = "Саргсян Татев ИВТ-23"
import math
# Задание №10

def fall_time(h: float) -> float:
    """
    Вычисляет время падения камня с высоты h.
    Формула: h = g * t² / 2  =>  t = sqrt(2h / g)
    """
    g = 9.81
    if h < 0:
        raise ValueError("Высота не может быть отрицательной.")
    return math.sqrt(2 * h / g)


def main():
    h = float(input("Задание 1 | Введите высоту (м): "))
    t = fall_time(h)
    print(f"  Высота: {h} м")
    print(f"  Время падения: {t:.4f} с")
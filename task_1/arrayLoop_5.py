__author__ = "Саргсян Татев ИВТ-23"
# Задание №136ж

def alternating_sum(a: list) -> float:
    result = 0
    for i in range(len(a)):
        result += ((-1) ** i) * a[i]
    return result


def main():
    print("Задание 5 | Знакочередующаяся сумма массива:")
    n = int(input("  Введите n: "))
    a = []
    for i in range(n):
        x = float(input(f"  a[{i + 1}] = "))
        a.append(x)

    result = alternating_sum(a)
    print(f"  Результат: {result}")
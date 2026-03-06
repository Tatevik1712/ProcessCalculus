__author__ = "Саргсян Татев ИВТ-23"

from task_1 import (
    arithmetic_1,
    branches_2,
    simpleArithmetic_3,
    loop_4,
    arrayLoop_5,
    arrayLoopBranch_6,
    loopIter_7,
    matrix_8,
)

TASKS = {
    "1": ("Арифметика. Время падения камня",          arithmetic_1.main),
    "2": ("Ветвления. Вычисление max²(a,b) + 1",      branches_2.main),
    "3": ("Простая арифметика. Замена чисел",          simpleArithmetic_3.main),
    "4": ("Цикл. Сумма 1/k^5 от k=1 до n",             loop_4.main),
    "5": ("Массив + цикл. Знакочередующаяся сумма",    arrayLoop_5.main),
    "6": ("Массив + ветвление. Сумма кратных 5",       arrayLoopBranch_6.main),
    "7": ("Итерационный цикл. Сумма ряда",             loopIter_7.main),
    "8": ("Матрица. Перестановка строки и столбца",    matrix_8.main),
}


def print_menu():
    print("\n" + "=" * 50)
    print("       МЕНЮ ЗАДАЧ — Саргсян Татев ИВТ-23")
    print("=" * 50)
    for key, (title, _) in TASKS.items():
        print(f"  {key}. {title}")
    print("  0. Выход")
    print("=" * 50)


def run_all():
    """Запускает все задачи по очереди."""
    for key, (title, func) in TASKS.items():
        print(f"\n{'=' * 50}")
        print(f"  ЗАДАНИЕ {key}: {title}")
        print("=" * 50)
        try:
            func()
        except Exception as e:
            print(f"  [Ошибка]: {e}")


def main():
    while True:
        print_menu()
        print("  A. Запустить все задачи подряд")
        choice = input("\nВыберите задание: ").strip().upper()

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "A":
            run_all()
        elif choice in TASKS:
            title, func = TASKS[choice]
            print(f"\n{'=' * 50}")
            print(f"  ЗАДАНИЕ {choice}: {title}")
            print("=" * 50)
            try:
                func()
            except Exception as e:
                print(f"  [Ошибка]: {e}")
        else:
            print("  Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
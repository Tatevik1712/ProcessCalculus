__author__ = "Саргсян Татев ИВТ-23"

from arrayLoop_5 import *
from arrayLoopBranch_6 import *
from loopIter_7 import *
from matrix_8 import *

# Тесты для alternating_sum
def test_alternating_sum():
    # Случай 1: Пустой список
    # Граничный случай: нет элементов — ожидаем 0.
    assert alternating_sum([]) == 0, "Пустой список должен давать 0"

    # Случай 2: Один элемент
    # Вырожденный случай: единственный элемент имеет знак «+».
    assert alternating_sum([7]) == 7, "Один элемент: сумма равна самому элементу"
    assert alternating_sum([-3]) == -3, "Один отрицательный элемент: сумма = -3"

    # Случай 3: Два элемента
    # a[0] - a[1] = 10 - 4 = 6
    assert alternating_sum([10, 4]) == 6, "Два элемента: 10 - 4 = 6"

    # Случай 4: Чётное количество элементов (4 элемента)
    # 1 - 2 + 3 - 4 = -2
    assert alternating_sum([1, 2, 3, 4]) == -2, "Чётное кол-во: 1-2+3-4 = -2"

    # Случай 5: Нечётное количество элементов (5 элементов)
    # 1 - 2 + 3 - 4 + 5 = 3
    assert alternating_sum([1, 2, 3, 4, 5]) == 3, "Нечётное кол-во: 1-2+3-4+5 = 3"

    # Случай 6: Список с отрицательными числами
    # (-1) - (-2) + (-3) = -1 + 2 - 3 = -2
    assert alternating_sum([-1, -2, -3]) == -2, "Отрицательные: -1+2-3 = -2"

    # Случай 7: Числа с плавающей точкой
    # 0.1 - 0.2 + 0.3 ≈ 0.2, результат должен быть округлён до 2 знаков
    result = alternating_sum([0.1, 0.2, 0.3])
    assert result == round(0.1 - 0.2 + 0.3, 2), "Плавающая точка: 0.1-0.2+0.3 округлить до 2 знаков"

    # Случай 8: Все элементы одинаковы (нечётное количество)
    # 5 - 5 + 5 = 5
    assert alternating_sum([5, 5, 5]) == 5, "Все одинаковы, нечётное кол-во: 5-5+5 = 5"

    # Случай 9: Все нули
    assert alternating_sum([0, 0, 0, 0]) == 0, "Все нули: сумма = 0"


# Тесты для sum_divisible_by_n
def test_sum_divisible_by_n():

    # Случай 1: Пустой список
    assert sum_divisible_by_n([], 3) == 0, "Пустой список: сумма = 0"

    # Случай 2: Нет кратных элементов
    # Ни один из [1, 2, 4, 5] не кратен 3
    assert sum_divisible_by_n([1, 2, 4, 5], 3) == 0, "Нет кратных 3: сумма = 0"

    # Случай 3: Все элементы кратны n
    # [3, 6, 9], n=3: 3+6+9 = 18
    assert sum_divisible_by_n([3, 6, 9], 3) == 18, "Все кратны 3: 3+6+9 = 18"

    # Случай 4: Частичная кратность
    # [1, 2, 3, 4, 5, 6], n=2: 2+4+6 = 12
    assert sum_divisible_by_n([1, 2, 3, 4, 5, 6], 2) == 12, "Чётные: 2+4+6 = 12"

    # Случай 5: n = 1 — все числа кратны 1
    # Сумма должна совпадать с суммой всего списка
    data = [7, 13, 22, -5]
    assert sum_divisible_by_n(data, 1) == sum(data), "n=1: сумма всех элементов"

    # Случай 6: Отрицательные числа кратные n
    # [-6, -3, 1, 2], n=3: -6 + -3 = -9
    assert sum_divisible_by_n([-6, -3, 1, 2], 3) == -9, "Отрицательные кратные 3: -9"

    # Случай 7: Ноль в списке (0 кратен любому n)
    # [0, 1, 2, 3], n=5: кратные 5 → только 0 → сумма = 0
    assert sum_divisible_by_n([0, 1, 2, 3], 5) == 0, "Ноль в списке: только 0 кратно 5"
    # [0, 5, 10], n=5: 0+5+10 = 15
    assert sum_divisible_by_n([0, 5, 10], 5) == 15, "Ноль + кратные 5: 0+5+10=15"

    # Случай 8: n больше всех элементов — нет кратных
    assert sum_divisible_by_n([1, 2, 3, 4], 100) == 0, "n=100, нет кратных: сумма = 0"


# Тесты для compute_sum
def test_compute_sum():

    # Вспомогательная функция для ручного расчёта одного слагаемого
    def term(k, x):
        return (math.factorial(2 * k) + abs(x)) / math.factorial(k ** 2)

    # Случай 1: n=1, x=0
    # Слагаемое: (2! + 0) / (1^2)! = 2 / 1 = 2.0
    expected_n1_x0 = term(1, 0)
    assert math.isclose(compute_sum(1, 0), expected_n1_x0, rel_tol=1e-9), \
        f"n=1, x=0: ожидается {expected_n1_x0}"

    # Случай 2: n=1, x=3.0
    # Слагаемое: (2! + 3) / 1! = (2+3)/1 = 5.0
    expected_n1_x3 = term(1, 3.0)
    assert math.isclose(compute_sum(1, 3.0), expected_n1_x3, rel_tol=1e-9), \
        f"n=1, x=3: ожидается {expected_n1_x3}"

    # Случай 3: Симметрия по знаку x — |x| делает знак несущественным
    # compute_sum(n, x) должно равняться compute_sum(n, -x)
    for n, x in [(1, 5.0), (2, 10.0), (3, 2.5)]:
        assert math.isclose(compute_sum(n, x), compute_sum(n, -x), rel_tol=1e-12), \
            f"Симметрия нарушена для n={n}, x={x}"

    # Случай 4: n=2, x=0 — ручной расчёт двух слагаемых
    # k=1: (2! + 0) / (1)! = 2/1 = 2
    # k=2: (4! + 0) / (4)! = 24/24 = 1
    # Итого: 3.0
    expected_n2_x0 = term(1, 0) + term(2, 0)
    assert math.isclose(compute_sum(2, 0), expected_n2_x0, rel_tol=1e-9), \
        f"n=2, x=0: ожидается {expected_n2_x0}"

    # Случай 5: n=2, x=6
    expected_n2_x6 = term(1, 6) + term(2, 6)
    assert math.isclose(compute_sum(2, 6), expected_n2_x6, rel_tol=1e-9), \
        f"n=2, x=6: ожидается {expected_n2_x6}"

    # Случай 6: Монотонность — добавление слагаемых только увеличивает сумму
    # (все слагаемые > 0, так как факториал и |x| неотрицательны)
    prev = compute_sum(1, 1.0)
    for n in range(2, 5):
        curr = compute_sum(n, 1.0)
        assert curr > prev, f"Монотонность нарушена: compute_sum({n}) <= compute_sum({n-1})"
        prev = curr

    # Случай 7: Результат всегда строго положителен при любых n >= 1
    for n, x in [(1, 0), (1, 100), (3, -50)]:
        assert compute_sum(n, x) > 0, f"Результат должен быть > 0 при n={n}, x={x}"


# Тесты для transform_matrix
def test_transform_matrix():
    # Случай 1: Матрица 1×1 (вырожденный случай)
    # Единственный элемент — он одновременно последняя строка и последний столбец.
    m = np.array([[42]])
    result = transform_matrix(m)
    assert result[0, 0] == 42, "1×1: единственный элемент не должен меняться"

    # Случай 2: Матрица 2×2
    # Исходная: Ожидаемая:
    # 1 2        1 3
    # 3 4        2 4
    # last_row = [3, 4], last_col = [2, 4]
    # Новый последний столбец ← [3, 4]
    # Новая последняя строка  ← [2, 4]
    m2 = np.array([[1, 2],
                   [3, 4]])
    r2 = transform_matrix(m2)
    expected2 = np.array([[1, 3],
                           [2, 4]])
    assert np.array_equal(r2, expected2), f"2×2: ожидается\n{expected2}\nполучено\n{r2}"

    # Случай 3: Матрица 3×3
    # Исходная:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # last_row = [7, 8, 9], last_col = [3, 6, 9]
    # Новый последний столбец ← [7, 8, 9]
    # Новая последняя строка  ← [3, 6, 9]
    m3 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    r3 = transform_matrix(m3)
    expected3 = np.array([[1, 2, 7],
                           [4, 5, 8],
                           [3, 6, 9]])
    assert np.array_equal(r3, expected3), f"3×3: ожидается\n{expected3}\nполучено\n{r3}"

    # Случай 4: Матрица с отрицательными значениями
    m4 = np.array([[-1, -2, -3],
                   [-4, -5, -6],
                   [-7, -8, -9]])
    r4 = transform_matrix(m4)
    expected4 = np.array([[-1, -2, -7],
                           [-4, -5, -8],
                           [-3, -6, -9]])
    assert np.array_equal(r4, expected4), "3×3 с отрицательными: неверное преобразование"

    # Случай 5: Иммутабельность — исходная матрица не должна изменяться
    m5 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    original_copy = m5.copy()
    _ = transform_matrix(m5)
    assert np.array_equal(m5, original_copy), "Исходная матрица не должна меняться"

    # Случай 6: Последняя строка совпадает с последним столбцом (симметричная матрица)
    # После обмена матрица должна остаться неизменной.
    m6 = np.array([[1, 2, 3],
                   [2, 5, 6],
                   [3, 6, 9]])
    # last_row = [3, 6, 9], last_col = [3, 6, 9] — они одинаковы
    r6 = transform_matrix(m6)
    assert np.array_equal(r6, m6), "Симметричная матрица после обмена не должна меняться"

    # Случай 7: Матрица из нулей — результат тоже должен быть нулевым
    m7 = np.zeros((4, 4), dtype=int)
    r7 = transform_matrix(m7)
    assert np.array_equal(r7, m7), "Нулевая матрица: после трансформации тоже нули"

    # Случай 8: Проверка угловых элементов матрицы 4×4
    # Угловой элемент [3,3] принадлежит и последней строке, и последнему столбцу,
    # поэтому он должен остаться на месте.
    m8 = np.arange(1, 17).reshape(4, 4)
    r8 = transform_matrix(m8)
    idx = 3
    assert r8[idx, idx] == m8[idx, idx], \
        "Угловой элемент [n-1, n-1] должен остаться неизменным"


if __name__ == "__main__":
    test_alternating_sum()
    print("test_alternating_sum    — OK")

    test_sum_divisible_by_n()
    print("test_sum_divisible_by_n — OK")

    test_compute_sum()
    print("test_compute_sum        — OK")

    test_transform_matrix()
    print("test_transform_matrix   — OK")

    print("\nВсе тесты прошли успешно ✓")
__author__ = "Саргсян Татев ИВТ-23"

"""
Сравниваются:
1. NumPy (CPU)
2. PyTorch (CPU)
3. PyTorch (GPU, CUDA)

Показать ускорение при использовании GPU и оптимизированных библиотек
"""

import time
import numpy as np
import torch

def average_time_cpu(func, *args, repeats=5):
    """
    Среднее время выполнения на CPU
    :param repeats: количество повторов
    """
    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)

    return sum(times) / len(times)


def average_time_gpu(func, *args, repeats=5):
    """
    Среднее время выполнения на GPU
    """
    times = []

    for _ in range(repeats):
        torch.cuda.synchronize()
        start = time.perf_counter()
        func(*args)

        torch.cuda.synchronize()
        end = time.perf_counter()

        times.append(end - start)

    return sum(times) / len(times)


def main():
    """
    Главная функция:
    1. Генерирует матрицы
    2. Выполняет умножение разными способами
    3. Сравнивает время
    """

    # Размер матриц (можно менять)
    n = 2000

    print(f"Размер матрицы: {n}x{n}")

    # =========================
    # NumPy (CPU)
    # =========================

    # Генерация случайных матриц
    A_np = np.random.rand(n, n)
    B_np = np.random.rand(n, n)

    print("\n[1] NumPy (CPU)")


    # t_numpy = average_time_cpu(np.dot, A_np, B_np, repeats=5)
    # t_torch_cpu = average_time_cpu(torch.matmul, A_torch, B_torch, repeats=5)
    # t_torch_gpu = average_time_gpu(torch.matmul, A_gpu, B_gpu, repeats=5)



    # Умножение матриц через NumPy
    t_numpy = average_time_cpu(np.dot, A_np, B_np, repeats=5)
    print(f"Время NumPy: {t_numpy:.4f} сек")

    # =========================
    # PyTorch (CPU)
    # =========================

    # Преобразуем numpy массивы в torch tensor
    A_torch = torch.tensor(A_np, dtype=torch.float32)
    B_torch = torch.tensor(B_np, dtype=torch.float32)
    print("\n[2] PyTorch (CPU)")

    # Умножение матриц на CPU
    t_torch_cpu = average_time_cpu(torch.matmul, A_torch, B_torch, repeats=5)
    print(f"Время Torch CPU: {t_torch_cpu:.4f} сек")

    # =========================
    # PyTorch (GPU)
    # =========================

    print("\n[3] PyTorch (GPU)")

    # Проверяем доступность CUDA
    if torch.cuda.is_available():
        # Выбираем устройство GPU
        device = torch.device("cuda")

        # Переносим данные на GPU
        A_gpu = A_torch.to(device)
        B_gpu = B_torch.to(device)

        # Вывод информации о GPU
        print("Используется GPU:", torch.cuda.get_device_name(0))

        # Замер времени выполнения на GPU
        t_torch_gpu = average_time_gpu(torch.matmul, A_gpu, B_gpu, repeats=5)

        print(f"Время Torch GPU: {t_torch_gpu:.4f} сек")

    else:
        print("GPU недоступен")


if __name__ == "__main__":
    main()
__author__ = "Саргсян Татев"

from brute_force import brute_force_chunk
import multiprocessing
import sys
import time


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
# длина пароля
PASSWORD_LENGTH = 7
# хэш SHA-512
TARGET_HASH = (
    "6e9564685eb16c0c516ff1210dc6e94dc183faf1a1026116fccddb4d215e8df8eb82"
    "440d2bbbf4ee5d605edef87db7ce602eeb0bf0b8000b063753b8996e2ae3")


def main():
    """Управляющая функция для инициализации и контроля процесса брутфорса.
    Определяет аппаратные возможности системы (кол-во ядер CPU), разбивает
    общую задачу перебора на независимые сегменты (задачи) по первому символу,
    инициирует пул параллельных процессов и динамически обрабатывает их результаты.
    """
    print(f"Целевой хэш: {TARGET_HASH}")
    print(f"Алфавит: {ALPHABET} (длина: {len(ALPHABET)})")
    print(f"Длина пароля: {PASSWORD_LENGTH}")

    # Автоматически определяем количество логических ядер CPU (включая Hyper-Threading).
    # На основе этого числа Python создаст оптимальное количество параллельных воркеров.
    num_cores = multiprocessing.cpu_count()
    print(f"Задействовано ядер процессора: {num_cores}")

    # Разделение пространства поиска (Chunking / Map-Reduce подход).
    # Создаем список задач (tasks). Каждая задача — это кортеж параметров для brute_force_chunk.
    # Так как в ALPHABET 36 символов, мы получаем ровно 36 уникальных задач.
    # Задача 1 начнется с '0', Задача 2 — с '1', ..., Задача 36 — с 'z'.
    tasks = [(char, TARGET_HASH, PASSWORD_LENGTH, ALPHABET) for char in ALPHABET]

    # Фиксируем время старта для последующего замера производительности
    start_time = time.time()

    # Создаем пул процессов. Контекстный менеджер 'with' гарантирует корректное
    # закрытие пула и освобождение системных ресурсов после завершения блока кода.
    with multiprocessing.Pool(processes=num_cores) as pool:
        # pool.imap_unordered лениво передает задачи из списка tasks свободным процессам.
        # В отличие от обычного map, он возвращает результат мгновенно, как только ХОТЬ ОДИН
        # процесс завершит работу (порядок завершения задач не важен). Это критично для брутфорса.
        for result in pool.imap_unordered(brute_force_chunk, tasks):
            # Если brute_force_chunk вернул строку (пароль), а не None:
            if result:
                end_time = time.time()
                print("\n" + "=" * 40)
                print(f"ПАРОЛЬ НАЙДЕН: {result}")
                print(f"Затраченное время: {end_time - start_time:.2f} сек.")
                print("=" * 40)

                # Поскольку нужный пароль уже найден, продолжать вычисления на других ядрах
                # нет смысла. Принудительно уничтожаем (terminate) все оставшиеся активные процессы в пуле.
                pool.terminate()
                # Немедленно завершаем работу всего скрипта с кодом 0 (успех)
                sys.exit(0)

    # Если пул обработал абсолютно все 36 задач и ни разу не сработал `if result:`
    print("\nПароль не найден во всем пространстве поиска.")


if __name__ == "__main__":
    main()
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
    print(f"Целевой хэш: {TARGET_HASH}")
    print(f"Алфавит: {ALPHABET} (длина: {len(ALPHABET)})")
    print(f"Длина пароля: {PASSWORD_LENGTH}")

    # определяем количество ядер CPU
    # Python создаст оптимальное количество параллельных воркеров
    num_cores = multiprocessing.cpu_count()
    print(f"Задействовано ядер процессора: {num_cores}")

    # Создаем список задач (tasks). Каждая задача — это кортеж параметров для brute_force_chunk.
    # Так как в ALPHABET 36 символов -> 36 задач.
    # Задача 1 начнется с '0', Задача 2 — с '1', ...
    tasks = [(char, TARGET_HASH, PASSWORD_LENGTH, ALPHABET) for char in ALPHABET]

    start_time = time.time()

    # Создаем пул процессов
    with multiprocessing.Pool(processes=num_cores) as pool:
        # pool.imap_unordered передает задачи из списка tasks свободным процессам.
        # возвращает результат мгновенно, как только хоть один процесс завершит работу
        for result in pool.imap_unordered(brute_force_chunk, tasks):
            # Если brute_force_chunk вернул строку (пароль), а не None:
            if result:
                end_time = time.time()
                print("\n" + "=" * 40)
                print(f"ПАРОЛЬ НАЙДЕН: {result}")
                print(f"Затраченное время: {end_time - start_time:.2f} сек.")
                print("=" * 40)

                #Принудительно уничтожаем (terminate) все активные процессы в пуле
                pool.terminate()
                # Немедленно завершаем работу
                sys.exit(0)

    print("\nПароль не найден во всем пространстве поиска.")


if __name__ == "__main__":
    main()
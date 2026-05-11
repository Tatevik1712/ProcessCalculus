import hashlib
import string
import itertools
import threading
import time


# Глобальный флаг остановки
found = False
result = None

# Алфавит: цифры + маленькие буквы
alphabet = string.digits + string.ascii_lowercase


def sha512_hash(s: str) -> str:
    """
    Возвращает sha512-хеш строки
    """
    return hashlib.sha512(s.encode()).hexdigest()


def worker(start_chars: str, target_hash: str):
    """
    Поток перебирает пароли, начинающиеся с заданных символов
    """
    global found, result

    for prefix in start_chars:
        if found:
            return

        # перебор оставшихся 6 символов
        for combo in itertools.product(alphabet, repeat=6):
            if found:
                return

            password = prefix + ''.join(combo)
            hash_value = sha512_hash(password)

            if hash_value == target_hash:
                found = True
                result = password
                print(f"\nНАЙДЕН ПАРОЛЬ: {password}")
                return


def split_alphabet(n_threads: int):
    """
    Делит алфавит на части для потоков
    """
    chunk_size = len(alphabet) // n_threads
    return [
        alphabet[i * chunk_size:(i + 1) * chunk_size]
        for i in range(n_threads - 1)
    ] + [alphabet[(n_threads - 1) * chunk_size:]]


def brute_force(target_hash: str, n_threads: int = 4):
    """
    Запускает многопоточный перебор
    """
    threads = []
    parts = split_alphabet(n_threads)

    start_time = time.time()

    for part in parts:
        t = threading.Thread(target=worker, args=(part, target_hash))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    if result:
        print(f"Пароль найден: {result}")
    else:
        print("Пароль не найден")

    print(f"Время: {end_time - start_time:.2f} сек")


def main():
    """
    Вставь сюда свой хеш из hashes.md
    """
    target_hash = "6e9564685eb16c0c516ff1210dc6e94dc183faf1a1026116fccddb4d215e8df8eb82440d2bbbf4ee5d605edef87db7ce602eeb0bf0b8000b063753b8996e2ae3"

    brute_force(target_hash, n_threads=4)

if __name__ == "__main__":
    main()
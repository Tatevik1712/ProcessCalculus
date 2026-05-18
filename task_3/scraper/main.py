"""Создайте программу, которая записывает заголовки новостей (публикаций, постов)
с выбранного вами сайта (например Новости ЗабГУ или Хабр).

 - [ + ] Программа должна просматривать несколько десятков страниц сайта.
 - [ + ] Напишите комментарии, документацию
 - [ + ] разбейте программу на функции
 - [ + ] сохраняете данные в Pandas DataFrame
 - [ + ] программа сохраняет дату и теги новости +1
 - [ + ] программа сохраняет текст новости +1
"""

import time
import random
import pandas as pd
from config import HABR_PAGES_URL, MIN_DELAY, MAX_DELAY
from network import get_html
from parser_habr import parse_habr_page


def run_scraper(max_pages: int = 3) -> pd.DataFrame:
    """
    Основной цикл скрапера, обходящий страницы
    """
    all_results = []

    for page in range(1, max_pages + 1):
        print(f"\n--- Обработка страницы {page} ---")
        url = HABR_PAGES_URL.format(page)

        html = get_html(url)
        if not html:
            print(f"Пропуск страницы {page} из-за ошибки доступа.")
            continue

        page_data = parse_habr_page(html)
        all_results.extend(page_data)

        # Рандомная пауза между страницами
        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        print(f"Ожидание {delay:.2f} сек. перед следующей страницей...")
        time.sleep(delay)

    # Создание Pandas DataFrame
    df = pd.DataFrame(all_results)
    return df


if __name__ == "__main__":
    print("Запуск сбора новостей")

    # Собираем данные (для теста выставим 2 страницы)
    result_df = run_scraper(max_pages=2)

    if not result_df.empty:
        print(f"\nСбор завершен. Всего записей: {len(result_df)}")
        print(result_df.head(2))

        # Сохранение результатов
        result_df.to_csv("habr_extended_news.csv", index=False, encoding="utf-8-sig")
        print("Данные успешно сохранены в 'habr_extended_news.csv'")
    else:
        print("Не удалось собрать данные.")
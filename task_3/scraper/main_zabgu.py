"""
Главный файл для запуска скрапера новостей ЗабГУ
"""
import time
import random
import pandas as pd
from config import START_URL, MIN_DELAY, MAX_DELAY
from network import get_html
from parser_zabgu import parse_zabgu_page


def run_scraper(max_pages: int = 3) -> pd.DataFrame:
    """
    Основной цикл обхода страниц новостной ленты ЗабГУ
    """
    all_results = []

    for page in range(1, max_pages + 1):
        print(f"\nОБРАБОТКА СТРАНИЦЫ ЛЕНТЫ {page} из {max_pages}")
        url = f"{START_URL}{page}"

        html = get_html(url)
        if not html:
            print(f"Пропуск страницы {page} из-за ошибки сети.")
            continue

        page_data = parse_zabgu_page(html)
        all_results.extend(page_data)

        # Случайная пауза между страницами (Задание №1)
        if page < max_pages:
            delay = random.uniform(MIN_DELAY, MAX_DELAY)
            print(f"Ожидание {delay:.2f} сек. перед переходом на следующую страницу...")
            time.sleep(delay)

    return pd.DataFrame(all_results)


if __name__ == "__main__":
    print("Второй алгоритм скрапер")

    # Настраиваем глубину парсинга (например, 2 страницы для проверки)
    df_result = run_scraper(max_pages=2)

    print("\nсбор данных завершен ")
    if not df_result.empty:
        print(f"Всего успешно спарсено новостей: {len(df_result)}")
        print("\nПервые строки Pandas DataFrame:")
        print(df_result.head(2))

        # Сохранение результатов с поддержкой кириллицы (utf-8-sig)
        output_file = "zabgu_news_structured.csv"
        df_result.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\nДанные сохранены в файл '{output_file}'")
    else:
        print("Данные не собраны. Проверьте структуру сайта или сетевое соединение.")
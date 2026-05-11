"""Создайте программу, которая записывает заголовки новостей (публикаций, постов)
с выбранного вами сайта (например Новости ЗабГУ или Хабр).

 - [ + ] Программа должна просматривать несколько десятков страниц сайта.
 - [ + ] Напишите комментарии, документацию
 - [ + ] разбейте программу на функции
 - [ + ] сохраняете данные в Pandas DataFrame
 - [ + ] программа сохраняет дату и теги новости +1
 - [ + ] программа сохраняет текст новости +1

Для получения данных со страницы используйте библиотеку requests"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def get_html(url: str) -> str:
    """
    Отправляет GET-запрос и возвращает HTML страницы.
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        return ""


def parse_article_page(url: str) -> str:
    """
    Получает текст конкретной статьи.
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    article = soup.find("div", class_="tm-article-body")

    if article:
        return article.get_text(strip=True)
    return ""


def parse_page(html: str) -> list:
    """
    Парсит одну страницу со списком статей.
    Возвращает список словарей с данными.
    """
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article")

    data = []

    for article in articles:
        try:
            # Заголовок
            title_tag = article.find("a", class_="tm-title__link")
            title = title_tag.text.strip()
            link = "https://habr.com" + title_tag.get("href")

            # Дата
            time_tag = article.find("time")
            date = time_tag.get("datetime") if time_tag else None

            # Теги
            tags = article.find_all("a", class_="tm-publication-hub__link")
            tags_list = [tag.text.strip() for tag in tags]

            # Текст статьи (доп. задание)
            text = parse_article_page(link)

            data.append({
                "title": title,
                "date": date,
                "tags": tags_list,
                "text": text,
                "link": link
            })

            print(f"Спарсено: {title}")

        except Exception as e:
            print("Ошибка парсинга статьи:", e)

    return data


def scraper(pages: int = 3) -> pd.DataFrame:
    """
    Основная функция парсинга.
    Проходит по нескольким страницам.
    """
    all_data = []

    for page in range(1, pages + 1):
        url = f"https://habr.com/ru/all/page{page}/"
        print(f"Обрабатывается страница {page}")

        html = get_html(url)
        if not html:
            continue

        page_data = parse_page(html)
        all_data.extend(page_data)

        time.sleep(1)  # чтобы не перегружать сервер

    df = pd.DataFrame(all_data)
    return df


def main():
    df = scraper(pages=3)

    print("\nРезультат:")
    print(df.head())

    # Сохранение в файл
    df.to_csv("habr_news.csv", index=False)
    print("\nДанные сохранены в habr_news.csv")


if __name__ == "__main__":
    main()
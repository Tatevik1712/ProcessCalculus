"""
Модуль парсинга структуры сайта Хабр
"""
from bs4 import BeautifulSoup
from network import get_html
from config import HABR_BASE_URL


def parse_article_body(url: str) -> str:
    """
    Заходит на страницу статьи и забирает полный текст.
    Ищет строго в двух местах. Он проверяет класс tm-article-body,
    а если его нет — article-formatted-body
    """
    html = get_html(url)
    if not html:
        return "Не удалось загрузить страницу"

    soup = BeautifulSoup(html, "html.parser")
    # BeautifulSoup(...): Конструктор класса, который принимает HTML-контент и создает объект для его анализа
    # html: Первый аргумент — это переменная, содержащая HTML-код (обычно текст, полученный через библиотеку requests).
    # "html.parser": Второй аргумент указывает метод (парсер), который будет использоваться для разбора.

    # На Хабре текст статьи обычно лежит в одном из этих классов (в зависимости от типа публикации)
    article_body = soup.find("div", class_="tm-article-body")
    # "div": Первый аргумент указывает тип HTML-тега, который мы ищем. В данном случае — <div> (блок).
    # class_="tm-article-body": Это критерий поиска — атрибут тега.
    # Мы ищем <div>, у которого CSS-класс равен "tm-article-body".

    if not article_body:
        article_body = soup.find("div", class_="article-formatted-body")

    if article_body:
        return article_body.get_text(separator="\n", strip=True)
    return "Текст новости не найден"


def parse_habr_page(html: str) -> list:
    """
    Парсит превью-страницу со списком статей
    """
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article")
    page_data = []

    for article in articles:
        try:
            # Заголовок и ссылка
            title_tag = article.find("a", class_="tm-title__link")
            if not title_tag:
                continue

            title = title_tag.text.strip()
            link = HABR_BASE_URL + title_tag.get("href")

            # Дата публикации
            time_tag = article.find("time")
            date = time_tag.get("datetime") if time_tag else None

            # Теги (хабы)
            tags_elements = article.find_all("a", class_="tm-publication-hub__link")
            tags_list = [tag.text.replace("*", "").strip() for tag in tags_elements]

            # Парсинг полного текста статьи (теперь работает!)
            text = parse_article_body(link)

            page_data.append({
                "title": title,
                "date": date,
                "tags": tags_list,
                "text": text,
                "link": link
            })
            print(f"Спарсено: {title[:40]}...")

        except Exception as e:
            print(f"[Ошибка парсинга элемента]: {e}")

    return page_data
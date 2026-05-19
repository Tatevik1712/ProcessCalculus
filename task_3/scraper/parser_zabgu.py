"""
Модуль парсинга страниц и новостей сайта ЗабГУ
"""
from bs4 import BeautifulSoup
from network import get_html
from config import BASE_URL, MIN_DELAY, MAX_DELAY
import time
import random

def parse_article_text(article_url: str) -> str:
    """
    Переходит на страницу новости и извлекает полный текст публикации.
    Ищет гораздо шире. Он перебирает не только разные классы (news-text,
    content), но и разные типы тегов: блоки <div>, ячейки таблиц <td>,
    а также поиск по уникальному идентификатору id="content"
    """
    html = get_html(article_url)
    if not html:
        return "Не удалось загрузить страницу"

    soup = BeautifulSoup(html, "html.parser")

    # Расширенный поиск текстового блока (проверяем все возможные теги)
    content_div = (
        soup.find("div", class_="news-text") or
        soup.find("div", class_="content") or
        soup.find("td", class_="news-text") or
        soup.find("div", id="content")
    )

    if content_div:
        return content_div.get_text(separator=" ", strip=True)

    # Если точечные селекторы не сработали, забираем текст из тегов абзацев
    paragraphs = soup.find_all("p")
    if paragraphs:
        return " ".join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 20])

    return "Текст новости не найден"

def parse_zabgu_page(html: str) -> list:
    """
    Парсит списочную страницу новостей, извлекая метаданные и инициируя сбор текста.
    """
    soup = BeautifulSoup(html, "html.parser")
    page_data = []

    # Сначала собирает вообще все ссылки на странице. Ищем ссылки на новости. На ЗабГУ ссылки на полные новости обычно
    # содержат в URL подстроку "news.php?id=" или "category="
    all_links = soup.find_all("a")
    valid_news_links = []

    for a in all_links:
        href = a.get("href", "")
        # Фильтруем ссылки, чтобы брать только ведущие на конкретные новости
        if "news.php?id=" in href or "news.php?category=" in href and href not in valid_news_links:
            # Убираем дубликаты и ссылки-пустышки без текста
            if len(a.text.strip()) > 10:
                valid_news_links.append(a)

    # Если по ссылкам ничего найти не удалось, ищем старым блочным методом
    if not valid_news_links:
        news_items = soup.find_all("div", class_="news-item") or soup.find_all("div", class_="news")
        for item in news_items:
            link_tag = item.find("a")
            if link_tag:
                valid_news_links.append(link_tag)

    # Обработка собранных элементов
    for title_tag in valid_news_links:
        try:
            title = title_tag.text.strip()
            href = title_tag.get("href")
            link = href if href.startswith("http") else BASE_URL + href

            # Пытаемся найти дату рядом со ссылкой (в родительском элементе)
            parent = title_tag.find_parent()
            date = "Без даты"
            if parent:
                date_tag = parent.find("span", class_="news-date") or parent.find("div", class_="date")
                if date_tag:
                    date = date_tag.text.strip()

            category_tag = title_tag.find_next("span", class_="news-category")
            tags = [category_tag.text.strip()] if category_tag else ["Общие новости"]

            # Парсинг тела новости
            print(f"Сбор текста. Переход по ссылке: {title[:40]}...")
            text = parse_article_text(link)

            page_data.append({
                "title": title,
                "date": date,
                "tags": tags,
                "text": text,
                "link": link
            })

            # пауза между статьями
            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

        except Exception as e:
            print(f"Ошибка парсинга элемента: {e}")

    return page_data
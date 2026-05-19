"""
Модуль для работы с сетью
"""
import requests
from config import HEADERS

def get_html(url: str) -> str:
    """
    Отправляет GET-запрос по указанному URL и возвращает HTML-код страницы
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка. Статус ответа: {response.status_code} для URL: {url}")
            return ""
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return ""
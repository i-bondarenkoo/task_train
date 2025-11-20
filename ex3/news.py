from dataclasses import dataclass


@dataclass
class News:
    # заголовок
    header: str
    # описание новости
    description: str
    # источник новости
    origin_news: str
    # ссылка на оригинал
    url: str
    # автор
    author: str

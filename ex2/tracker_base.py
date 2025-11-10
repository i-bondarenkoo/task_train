from abc import ABC, abstractmethod


class Tracker(ABC):
    def __init__(self, base_url: str):
        Tracker.validate_url(base_url)
        # адрес апи для запроса
        self.url = base_url

    @classmethod
    def validate_url(cls, url: str):
        if not isinstance(url, str):
            raise TypeError("Ссылка должна передаваться как строка")

    # возвращает цену в USD
    @abstractmethod
    def get_price(self, coin: str) -> float:
        pass

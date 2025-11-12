from abc import ABC, abstractmethod


class QuoteBase(ABC):
    def __init__(self, base_url_api: str):
        self.base_url_api = base_url_api

    # абстрактный метод, который будем реализовывать в наследнике
    @abstractmethod
    def get_quote(self):
        pass

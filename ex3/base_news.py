from abc import ABC, abstractmethod


class BaseNewsSource(ABC):
    def __init__(self, api_url: str):
        self.api_url = api_url

    @abstractmethod
    def get_news(self):
        pass

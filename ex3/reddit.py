from base_news import BaseNewsSource
from client import Client
from news import News


class HackerNews(BaseNewsSource):
    def __init__(self, api_url):
        super().__init__(api_url)
        self.list_news: list[News] = []
        self.client: Client = Client()

    def get_list_ids(self):
        response: list[int] = self.client.get_request(
            url="https://hacker-news.firebaseio.com",
            path="/v0/newstories.json",
        )
        return response

    def get_news_with_id(self, id: int):
        response = self.client.get_request(
            url="https://hacker-news.firebaseio.com",
            path=f"/v0/item/{id}.json",
        )

    def __str__(self):
        return "\n".join(str(news) for news in self.list_news)

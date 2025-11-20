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

    def get_news(self, limit: int = 5):
        response_list_id: list[int] = self.get_list_ids()
        for value in response_list_id[:limit]:
            response = self.client.get_request(
                url="https://hacker-news.firebaseio.com",
                path=f"/v0/item/{value}.json",
            )
            news: News = self._convert_dict_to_news_object(response)
            self.list_news.append(news)

        return self.list_news

    def _convert_dict_to_news_object(self, response: dict):

        news: News = News(
            header=response["title"],
            description=response.get("description", "описание отсутствует"),
            origin_news="Hacker",
            url=response.get("url", "ссылка не найдена"),
            author=response["by"],
        )
        return news

    def __str__(self):
        return "\n".join(
            f"Header:{news.header}\nDescription: {news.description}\nOrigin_news: {news.origin_news}\nUrl: {news.url}\nAuthor: {news.author}\n----"
            for news in self.list_news
        )

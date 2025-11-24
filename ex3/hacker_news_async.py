from base_news import BaseNewsSource
from async_client import AsyncClient
from news import News
from dec import count_time


class HackerNewsAsync(BaseNewsSource):
    def __init__(
        self,
        api_url: str,
    ):
        super().__init__(api_url)
        self.list_news_async: list[int] = []
        self.async_client = AsyncClient()

    async def get_list_ids(
        self,
    ):
        response: list[int] = await self.async_client.get_request(
            url="https://hacker-news.firebaseio.com",
            path="/v0/newstories.json",
        )
        return response

    @count_time
    async def get_news(self, limit: int = 5):
        response_list_id: list[int] = await self.get_list_ids()
        for r in response_list_id[:limit]:
            response = await self.async_client.get_request(
                url="https://hacker-news.firebaseio.com",
                path=f"/v0/item/{r}.json",
            )
            news: News = self._convert_dict_to_news_object(response)
            self.list_news_async.append(news)

        return self.list_news_async

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
            for news in self.list_news_async
        )

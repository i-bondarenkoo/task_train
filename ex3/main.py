from client import Client
from hacker_news import HackerNews
from news import News
from hacker_news_async import HackerNewsAsync
import asyncio


async def main():
    hacker_news = HackerNews("https://hacker-news.firebaseio.com")
    # hacker_news.get_news(5)
    hacker_news.get_news(5)
    print(hacker_news)
    hacker_news_async = HackerNewsAsync("https://hacker-news.firebaseio.com")
    await hacker_news_async.async_client.create_session()
    await hacker_news_async.get_news(5)
    print(hacker_news_async)
    await hacker_news_async.async_client.close()


if __name__ == "__main__":
    asyncio.run(main())

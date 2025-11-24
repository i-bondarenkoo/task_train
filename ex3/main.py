from client import Client
from hacker_news import HackerNews
from news import News
from hacker_news_async import HackerNewsAsync

if __name__ == "__main__":
    hacker_news = HackerNews("https://hacker-news.firebaseio.com")
    # print(hacker_news.get_list_ids())
    # print("-----")
    hacker_news.get_news(25)
    print(hacker_news)
    hacker_news_async = HackerNewsAsync("https://hacker-news.firebaseio.com")
    hacker_news_async.get_news(25)
    print(hacker_news_async)

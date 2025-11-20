from client import Client
from hacker_news import HackerNews
from news import News

if __name__ == "__main__":
    hacker_news = HackerNews("https://hacker-news.firebaseio.com")
    print(hacker_news.get_list_ids())
    print("-----")
    hacker_news.get_news(25)
    print(hacker_news)

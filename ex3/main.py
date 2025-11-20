from client import Client
from reddit import RedditNews
from news import News

if __name__ == "__main__":
    reddit1 = RedditNews("https://www.reddit.com")
    reddit1.get_news(limit=2)
    print(reddit1)

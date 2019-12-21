import requests
from bs4 import BeautifulSoup
import feedparser


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")


def get_articles():
    url = "https://fedoramagazine.org/feed/"
    feed = feedparser.parse(url)
    Dict = {}
    for entry in feed['entries']:
        Dict[entry['title']] = entry.link
    return Dict


def main():
    Dict = get_articles()
    print(Dict)


if __name__ == '__main__':
    main()
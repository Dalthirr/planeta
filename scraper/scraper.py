from requests import get
from bs4 import BeautifulSoup
from random import choice
from .data.article import Article
from .exceptions import InvalidStatusCode, NoArticlesFound


class PlanetaScraper:

    def __init__(self):
        self.content = None
        self.articles = None

    def _get_content(self):
        page = get('http://www.planeta.pl')

        if page.status_code == 200:
            self.content = BeautifulSoup(page.content, "html.parser")

        else:
            raise InvalidStatusCode(f"Unfortunately we could not load Planeta content due to {page.status_code} error")

    def get_articles(self):
        self._get_content()

        self.articles = [article for article in self.content.find_all("div", class_="image")
                         if 'image' in article.contents[1].attrs['class']]

        if not self.articles:
            raise NoArticlesFound("Scraper could not found any articles, please find out if method is not obsolete.")

    def get_random_article(self):
        data = choice(self.articles)
        # Add verification if title is not the same as subtitle and retry on scraping
        return Article(data=data)

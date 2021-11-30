from requests import get
from bs4 import BeautifulSoup
from random import choice
from .urls import main_page
from .data.article import Article
from .exceptions import InvalidStatusCode, EmptyContent


class PlanetaScraper:

    def __init__(self):
        self.content = None
        self.articles = None
        self.random_article = None

    def _get_content(self):
        page = get(main_page)

        if page.status_code == 200:
            self.content = BeautifulSoup(page.content, "html.parser")

        else:
            raise InvalidStatusCode(f"Unfortunately we could not load Planeta content due to {page.status_code} error")

    def get_articles(self):
        self._get_content()
        # bug - not div class=image is not only the articles!
        self.articles = [article for article in self.content.find_all("div", class_="image")
                         if 'image' in article.contents[1].attrs['class']]

    def get_random_article(self):
        data = choice(self.articles)
        return Article(data=data)

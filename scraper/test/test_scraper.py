from scraper.scraper import PlanetaScraper
from mock import Mock, patch
from pytest import raises


def test_scraper_instance_initializes_without_content():
    instance = PlanetaScraper()
    assert not instance.content


def test_scraper_instance_initializes_without_articles():
    instance = PlanetaScraper()
    assert not instance.articles


def test_get_content_sets_content_attribute():
    pass


def test_get_content_raises_invalid_status_code_while_not_200():
    pass


def test_get_articles():
    pass


def test_get_articles_raises_error_when_no_articles_could_be_found():
    pass


def test_get_random_article():
    pass


def test_get_random_article_retries_while_title_and_subtitle_the_same():
    pass

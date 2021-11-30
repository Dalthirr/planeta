class InvalidStatusCode(Exception):
    """ Raised when get status code is other than ok (200) """


class NoArticlesFound(Exception):
    """ Raised when no articles could be found by scraper """

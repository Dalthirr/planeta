class InvalidStatusCode(Exception):
    """ Raised when get status code is other than ok (200) """


class EmptyContent(Exception):
    """ Raised when user is trying to get anything from empty content """

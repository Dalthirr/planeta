class Article:
    """ Class for Planeta's article representation with most important attributes """

    def __init__(self, data):
        self._data = data

    @property
    def image_url(self) -> str:
        return 'mock'

    @property
    def link(self) -> str:
        link = self._data.find('a', href=True)
        return link['href']

    @property
    def subtitle(self) -> str:
        return self._get_title(subtitle=True)

    @property
    def title(self) -> str:
        return self._get_title(subtitle=False)

    def _get_title(self, subtitle: bool) -> str:
        """
        Gets article's title or subtitle

        :param subtitle: 0 if subtitle should be read, 1 if main title.
        :return: title or subtitles of Planeta's article.
        """
        text = self._data.text.strip("\n").split("\n")
        idx = 0 if subtitle else 1

        try:

            if text[idx]:
                return text[idx]

            else:
                return self.__get_href_title()

        except IndexError:
            return self.__get_href_title()

    def __get_href_title(self) -> str:
        """
        Gets article title hidden in article link.

        :return: Link title.
        """
        img_title = self._data.find('a', class_="image")
        return img_title['title']

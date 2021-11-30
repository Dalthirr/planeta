class Article:
    def __init__(self, data):
        self.data = data
        self.image_url = None
        self.link = self._get_link()
        self.subtitle = self._get_article_subtitle()
        self.title = self._get_article_title()

    def _get_link(self):
        link = self.data.find('a', href=True)
        return link['href']

    def _get_article_subtitle(self):
        text = self.data.text.strip("\n").split("\n")

        try:
            return text[0]

        except IndexError:
            return self.__get_image_title_if_no_text()

    def _get_article_title(self):
        text = self.data.text.strip("\n").split("\n")

        try:
            return text[1]

        except IndexError:
            return self.__get_image_title_if_no_text()

    def __get_image_title_if_no_text(self):
        img_title = self.data.find('a', class_="image")
        return img_title['title']

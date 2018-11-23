from com.ms.driver.engine import Engine
import re


class MangakakalotEngine(Engine):
    """
        Engine for download through the mangakakalot site
        I hope I am not committing a crime here
        Don't ban me google, Please
    """
    def __int__(self, manga_name):
        self.manga_name = manga_name
        self.url = "https://mangakakalot.com/search/" + re.sub(r"\s+", '_', manga_name.lower())

    def download(self):
        pass

    def crawl(self, links):
        pass

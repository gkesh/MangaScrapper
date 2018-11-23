import re
import requests as rq
from bs4 import BeautifulSoup as bs
from com.ms.driver.driver import Driver
from com.ms.driver.engine import Engine


class KissMangaEngine(Engine):
    """
        This engine is designed and will be modified
        to match the requirements of a typical kissmanga
        format
    """

    def __int__(self, manga_name):
        self.manga_name = manga_name
        self.url = "https://www.kissmanga.com/Manga/"+re.sub(r"\s+", '-', manga_name.title())

    def download(self):
        page = bs(Driver.get_page_by_class(self.url, "listing"), 'lxml')
        table = page.find('table')
        del page
        links = ["https://www.kissmanga.com" + item['href'] for item in table.find_all('a')]
        # titles = [item['title'] for item in table.find_all('a')]
        # dates = [item.select('td:nth-of-type(2)')[0].get_text(strip=True) for item in table.find_all('tr') if
        #          item.select('td:nth-of-type(2)')]
        # build_dataframe(titles, links, dates) # Support for csv based data cache for added features
        self.crawl(links[0:1])

    def crawl(self, links):
        for link in links:
            try:
                div_img = Driver.get_element_by_id(link, 'divImage')
                images = bs(div_img.get_attribute('innerHTML'), 'html.parser')
                images = [item.select('img')[0]['src'] for item in images.find_all('p') if item.select('img')]
                counter = 0
                for img_url in images:
                    img = rq.get(img_url)
                    print(type(img))
                    filename = "e:/Manga/page" + repr(counter) + ".png"
                    try:
                        with open(filename, 'wb') as image:
                            image.write(img.content)
                        counter += 1
                    except IOError:
                        print("Error Occurred During File Download..")
                    else:
                        print("Download Completed Successfully...")

            except TimeoutError:
                print('Requested Manga Timed Out. Try Again')


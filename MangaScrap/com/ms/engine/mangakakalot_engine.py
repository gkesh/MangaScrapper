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
        browser = wd.PhantomJS()
	    browser.get(self.url)
	    try:
	    	element = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "daily-update")))
	    except TimeoutException:
	        print("Request Timeout")
	        raise TimeoutError
		element = bs(element[0].get_attribute('innerHTML'), 'html.parser')
		element = [item.select("span > a") for item in element]
		[print(item) for item in element]

    def crawl(self, links):
        pass

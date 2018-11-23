import requests
import re
"""
  This is just something i had lying in my computer so i decided to put it in here
  For no reason at all
  It doesn't use CSRF tokens so no private accounts I'm afriad
  But if you wanna just download pictures from public account scrap away
"""

class InstaScrapper:
    """This is an instagram image scrapper
        It uses regex and request
    """

    def __init__(self, username):
        self.url = "https://www.instagram.com/" + username

    def download(self):
        req = requests.get(self.url)
        pattern = r"https://(.*?).jpg"
        counter = 0

        for img_url in re.findall(pattern, req.text):
            img = requests.get("https://" + img_url + ".jpg")
            filename = "image" + repr(counter) + ".jpg"
            try:
                with open(filename, 'wb') as image:
                    image.write(img.content)
                counter += 1
            except IOError:
                print("Error Occurred During File Download..")
            else:
                print("Download Completed Successfully...")

    @staticmethod
    def run():
        user = input("Enter a Username --> ")
        insta_scrapper = InstaScrapper(user)
        insta_scrapper.download()

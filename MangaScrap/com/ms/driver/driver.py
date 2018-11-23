from selenium import webdriver as wd
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Driver:
    """
        Driver file for manga scrapper engines
        New scrapper engines can be added 
    """

    @staticmethod
    def get_page_by_id(url, eid):
        browser = wd.PhantomJS()
        browser.get(url)
        try:
            WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.ID, eid)))
        except TimeoutException:
            print("Request Timeout")
            raise TimeoutError
        else:
            return browser.page_source

    @staticmethod
    def get_page_by_class(url, cl):
        browser = wd.PhantomJS()
        browser.get(url)
        try:
            WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.CLASS_NAME, cl)))
        except TimeoutException:
            print("Request Timeout")
            raise TimeoutError
        else:
            return browser.page_source

    @staticmethod
    def get_element_by_class(url, cl):
        browser = wd.PhantomJS()
        browser.get(url)
        try:
            element = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.CLASS_NAME, cl)))
        except TimeoutException:
            print("Request Timeout")
            raise TimeoutError
        else:
            return element

    @staticmethod
    def get_element_by_id(url, eid):
        browser = wd.PhantomJS()
        browser.get(url)
        try:
            element = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.ID, eid)))
        except TimeoutException:
            print("Request Timeout")
            raise TimeoutError
        else:
            return element

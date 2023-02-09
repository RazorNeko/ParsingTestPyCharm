import scrapy
from scrapy.http import HtmlResponse
from scrapy import Selector
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get('https://www.ozon.ru/category/smartfony-15502/?rating=t')
time.sleep(2)

driver.execute_script("window.scrollTo(0,400)")

driver.execute_script("window.scrollTo(0,4000)")
time.sleep(2)


driver.execute_script("window.scrollTo(0,400)")


html = driver.page_source

with open('TestScrapy/TestScrapy/myfile.html', 'w', encoding='utf-8') as f:
    f.write(html)

f.close()





class ProgHubParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_test_page()
        slide_elems = self.driver.find_elements(By.CLASS_NAME, "site-heading")

        print('hui')

        for elem in slide_elems:
            print(elem.text)

            # print(elem.get_attribute("href"))

            print(elem.find_element(By.TAG_NAME, 'a').get_attribute("href"))

            print('**************************')

    def go_to_test_page(self):
        self.driver.get('https://webscraper.io/test-sites')


def main():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, 'python')
    parser.parse()


if __name__ == 'main':
    main()

main()


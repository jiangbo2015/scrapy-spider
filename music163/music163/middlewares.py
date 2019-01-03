# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException


class Music163DownloaderMiddleware(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.wait = ui.WebDriverWait(self.driver, 3)

    def __del__():
        self.driver.close()


    def process_request(self, request, spider):
        try:
            self.driver.get(request.url)
            self.driver.switch_to.frame('g_iframe')            
            if self.wait.until(EC.presence_of_element_located((By.ID, 'm-pl-container'))):
                body = self.driver.page_source
                return HtmlResponse(url=request.url, body=body, encoding='utf-8', request=request, status=200)

        except TimeoutException:
            print('timeout')
            return HtmlResponse(url=request.url, request=request, encoding='utf-8', status=500)

import scrapy
from scrapy.http import HtmlResponse
from scrapy import Selector
import requests
from scrapy.crawler import CrawlerProcess



class ProxyList(scrapy.Spider):
    name = "proxy"
    allowed_domains = ["free-proxy-list.net"]
    start_urls = ['https://free-proxy-list.net/']

    def parse(self, response):
        # item = ProxyItem()

        table_rows = response.xpath(".//*[@class='table table-striped table-bordered']/"
                                    "tbody/tr")

        for row in table_rows:
            yield {'ip': row.xpath('./td/text()').extract_first(),
                   'port': row.xpath('./td[2]/text()').extract_first(),
                   'last_checked' : row.xpath('./td[8]/text()').extract_first(),

                   }
#Pizdagit
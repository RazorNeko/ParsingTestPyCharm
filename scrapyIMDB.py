import scrapy
from scrapy.http import HtmlResponse
from scrapy import Selector
import requests

class ImdbSpider(scrapy.Spider):
  name = "imdb"
  allowed_domains = ["imdb.com"]
  start_urls = ['http://www.imdb.com/chart/top']

  def parse (self, response):
    # nonweeme mad-mus co crpoxam, xapaxrepusynww Ton-(prams:
    table_rows = response.xpath(
    './/*[@class="chart full-width" and @data-caller-name="chart-top250movie"]/'
    'tbody[@class="lister-list"]/tr'
    )

    for row in table_rows:
      yield {"title" : row.xpath("./td[@class='titleColumn']/a/text() ").extract_first(),
               "year": row.xpath("./td[@class='titleColumn']/span/text()").extract_first().strip("() "),
               "rating": row.xpath("./td[@class='ratingColumn imdbRating']/strong/text()").extract_first(),
               }

from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings={
    "FEEDS": {
        "output_imdb.csv": {"format": "csv"},
    },
})


process.crawl(ImdbSpider)
process.start()


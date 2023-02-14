import scrapy
from scrapy.http import HtmlResponse
from scrapy import Selector
import requests

class MovieItem(scrapy.Item):
  title = scrapy.Field()
  rating = scrapy.Field()
  summary = scrapy.Field()
  year = scrapy.Field()
  genre = scrapy.Field()
  runtime = scrapy.Field()
  directors = scrapy.Field()
  writers = scrapy.Field()
  cast = scrapy.Field()

class ActorItem(scrapy.Item):
  actor_name = scrapy.Field()
  character = scrapy.Field()

class ImdbSpider_2(scrapy.Spider):
  name = "imdb"
  allowed_domains = ["imdb.com"]
  base_url = 'https://imdb.com'
  start_urls = ['http://www.imdb.com/chart/top']

  def parse(self, response):
    table_rows = response.xpath(
        './/*[@class="chart full-width" and @data-caller-name="chart-top250movie"]/'
    'tbody[@class="lister-list"]/tr'
    )

    for row in table_rows:
      rating = row.xpath("./td[@class='ratingColumn imdbRating']/strong/text()").extract_first()
      ret_url = row.xpath("td[@class='titleColumn']/a/@href").extract_first().strip()
      row_url = self.base_url + ret_url
      yield scrapy.Request(row_url, callback=self.parseOneMovie, meta={'rating':rating})

  def parseOneMovie(self, response):
    item = MovieItem()

    item['rating'] = response.meta['rating'][0]
    item['title'] = response.xpath('.//*/div[@class="sc-80d4314-1 fbQftq"]/h1/text()').extract_first().strip()
    item['title'] = response.xpath(".//*/div[@class='title_wrapper']/h1/text()").extract_first().strip()
    item['year'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/span/text()').extract()[0]

    print('Debug output')

    item['summary'] = response.xpath(".//*/div[@class='summary_text']/text()").extract_first().strip()
    item['directors'] = response.xpath('.//*/div[@class="credit_summary_item"]/a/text()').extract_first.strip()
    item['writers'] = response.xpath('.//*/div[@class="credit_summary_item"]/a/text()').extract()[1].strip()

    item['cast'] = list()

    for cast in response.xpath(".//table[@class='cast_list]/tr")[1:]:
      actor = ActorItem()

      actor['actor_name'] = cast.xpath("./td[2]/a/text()").extract_first().strip()
      actor['character'] = cast.xpath("./td[@class='character']/a/text()").extract_first()

      item['cast'].append(actor)

    return item

from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings={
    "FEEDS": {
        "../Output/output_imdb2.csv": {"format": "csv"},
    },
})

process.crawl(ImdbSpider_2)
process.start()

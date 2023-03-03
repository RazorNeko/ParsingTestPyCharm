import scrapy

class BookSpider(scrapy.Spider):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) 2AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    name = 'book24'
    start_urls = ['https://book24.ru/knigi-bestsellery/']
    def parse(self, response):
        for link in response.css('div.product-card__image-holder a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response):
        yield{
            'name':response.css('h1.product-detail-page__title::text').get()
        }


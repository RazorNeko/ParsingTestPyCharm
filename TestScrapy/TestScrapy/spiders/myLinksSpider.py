import scrapy

with open('urls.TXT') as f:
    lines = f.readlines()
print(lines)
list = []
for line in lines:
    list.append(line[:-1])
print(list)
html_list = []



class BookSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://xxx24.tv/post/worship-your-goddess-18329059']

    def parse(self, response):
        for l in html_list:
            yield response.follow(l, callback=self.parse_page)

    def parse_page(self, response):
        yield {
            'img': response.css('video.video-post--video::attr(poster)').get(),
        }
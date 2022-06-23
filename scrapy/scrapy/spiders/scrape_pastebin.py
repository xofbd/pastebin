import scrapy

class  PastebinSpider(scrapy.Spider):
    name = 'posts'
    def start_requests(self):
        url= 'https://pastebin.com/archive'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for tag in response.css('td.status -public'):
            yield {
                'title': tag.css('a::text').get(),
                'url': tag.css('a::attr(href)').get(),
            }

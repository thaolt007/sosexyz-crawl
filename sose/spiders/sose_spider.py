import scrapy
from sose.items import SoseItem


class SoseSpider(scrapy.Spider):
    name = "sose"

    def start_requests(self):
        url = 'http://sose.xyz/page/'
        for num in range(1, 2340):
            link = url + str(num)
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        images = SoseItem()
        for item in response.css('#homePage #grid .gridItem.gridphoto'):
            #images['imgid'] = item.css('::attr(data-identifier)').extract_first()
            images['url'] = item.css('::attr(data-photo-high)').extract_first()
            yield images


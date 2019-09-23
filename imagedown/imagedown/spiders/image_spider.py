import scrapy
from ..items import ImagedownItem


class image_Spider(scrapy.spiders.Spider):
    name = "imagedown"
    start_urls = ["https://www.mzitu.com/japan/"]

    def parse(self, response):        
        item = ImagedownItem()
        image_urls = response.css('.lazy::attr(data-original)').extract()
        item['image_urls'] = image_urls
        yield item
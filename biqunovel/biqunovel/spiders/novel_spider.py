import scrapy
from ..items import BiqunovelItem


class biqu_Spider(scrapy.spiders.Spider):
    name = "biqu"
    start_urls = ["http://www.biquge.se/24901/41015693.html"]

    def parse(self, response):
        items = BiqunovelItem()
        title = response.css("h1::text").extract()
        title = response.xpath("//h1/text()").extract()
        content = response.css("#content::text").extract()
        
        items['title'] = title
        items['content'] = content

        yield items

        

        next = response.css("div.bottem2 a").xpath("@href").extract()[3]
        if next is not None:
            urllink = response.urljoin(next)
        yield scrapy.Request(url=urllink, callback=self.parse)

        

        
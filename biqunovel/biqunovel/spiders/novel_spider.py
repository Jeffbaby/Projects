import scrapy
from ..items import BiqunovelItem


class biqu_Spider(scrapy.spiders.Spider):
    name = "biqu"
    start_urls = ["http://www.biquge.se/24901/41015693.html"]

    def parse(self, response):
        item = BiqunovelItem()
        title = response.css("h1::text").extract_first()
        #title = response.xpath("//h1/text()").extract()
        content = str(''.join(response.css("#content::text").extract())).strip()
        print(content)
        item['title'] = title
        item['content'] = content
        yield item

        next = response.css("div.bottem2 a").xpath("@href").extract()[3]
        if next is not None:
            urllink = response.urljoin(next)
        yield scrapy.Request(url=urllink, callback=self.parse)

        

        
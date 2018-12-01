#-*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import ProjectItem

class Dyh(CrawlSpider):
    name = "dyh"
    allowed_domains =[]
    start_urls =[
    "http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF"
    ]

    rules = (
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+", ),follow=True),
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/\d{6}\.html",restrict_css="h1.entry-title a"),callback="parse_item",follow=False),)
    def parse_item(self, response):
        # print(response.url)
        sel = Selector(response)
        try:
            if sel.xpath("//h1[@class='entry-title']/text()").extract_first():
                title = sel.xpath("//h1[@class='entry-title']/text()").extract_first()
                print(title)
            else:
                title =""
                print(response.url)
                raise Exception("ID is null")


            if sel.xpath("//time[@class='entry-date']/text()").extract_first():
                time = sel.xpath("//time[@class='entry-date']/text()").extract_first()
                print(time)
            else:
                time =""
                raise Exception("time is null")

            if sel.xpath("//*[@id='menu-%e5%af%bc%e8%88%aa%e8%8f%9c%e5%8d%95']//text()").extract_first():
                daodu = sel.xpath("//*[@id='menu-%e5%af%bc%e8%88%aa%e8%8f%9c%e5%8d%95']//text()").extract_first()
                print(daodu)
            else:
                daodu =""
                raise Exception("daodu is null")

            if sel.xpath("//div[@class='entry-content']/p/text()").extract_first():
                zhengwen = sel.xpath("//div[@class='entry-content']/p/text()").extract_first()
                print(zhengwen)
            else:
                zhengwen =""
                raise Exception("zhengwen is null")

            if sel.xpath("//div/p/text()").extract()[-1]:
                laiyuan = sel.xpath("//div/p/text()").extract()[-1]
                print(laiyuan)
            else:
                laiyuan =""
                raise Exception("laiyuan is null")

            if sel.xpath("//footer/a/text()").extract()[-1]:
                zuozhe = sel.xpath("//footer/a/text()").extract()[-1]
                print(zuozhe)
            else:
                zuozhe =""
                raise Exception("zuozhe is null")

            if sel.xpath("//p//img/@src").extract():
                tupian = sel.xpath("//p//img/@src").extract()
                print(tupian)
            else:
                tupian =""
                raise Exception("tupian is null")

            item = ProjectItem()
            item['title'] = title
            item['time'] = time
            item['daodu'] = daodu
            item['zhengwen'] = zhengwen
            item['laiyuan'] = laiyuan
            item['zuozhe'] = zuozhe
            item['tupian'] = tupian
            yield item
        finally:
            pass



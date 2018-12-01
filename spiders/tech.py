# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class Tech(CrawlSpider):
    name = 'tech'
    allowed_domains = []
    start_urls=  [
        "http://tech.ailab.cn/?page=1"
    ]
    rules = (
        Rule(LinkExtractor(allow="http://tech.ailab.cn/?page=\d+"),follow=True),
        Rule(LinkExtractor(allow="http://tech.ailab.cn/article-\d{5}.html",restrict_css="ul.list_jc a"),callback="parse_item",follow=False)

    )
    def parse_item(self,response):
        print(response.url)
        # sel = Selector(response)
        # try:
        #     if sel.xpath("//h1/text()").extract_first():
        #         title = sel.xpath("//h1/text()").extract_first()
        #         print(title)
        #     else:
        #         raise Exception("title is null")
        #     if sel.xpath("//h1/div/text()").extract():
        #         source = sel.xpath("//h1/div/text()").extract()
        #         print(source)
        #     else:
        #         raise Exception("source is null")
        # except:
        #     pass


# -*- coding: utf-8 -*-
import scrapy,re
from newspaper import Article
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

class RengongwSpider(scrapy.Spider):
    name = 'rengongw'
    # allowed_domains = ['http://ai.ailab.cn/?page=2']
    start_urls = ['http://ai.ailab.cn/?page=2/']
    # time.sleep(3)
    # rules = (
    #     Rule(LinkExtractor(allow='http://ai.ailab.cn/?page=2'),follow=True),
    #     Rule(LinkExtractor(allow='http://ai.ailab.cn/article-(.*?).html'),follow=False,callback='parse_item'),
    # )
    defalt = True
    defaults = True
    def start_requests(self):
        for i in range(2):
            url = "http://www.ailab.cn/?page="+str(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        if self.default:
            self.default = False
            yield scrapy.Request(url=response.url,callback=self.parse)

        else:
            link = response.xpath("//ul[@class='list_jc']/li/a[@class='title']/@href").extract()
            for i in link:
                print(i)
                urls = i
                print(type(urls),'-==============================')
                yield scrapy.Request(url=urls,callback=self.parse_1)

    def parse_1(self, response):
        # new = Article(url=response.url,language='zh')
        # new.download()
        # new.parse()
        if self.defaults:
            self.defaults = False
            print(type(response.url),'==============================================')
            yield scrapy.Request(url=response.url,callback=self.parse_1)

        else:
            if re.findall("<title>(.*?)</title>",response.text):
                title = re.findall("<title>(.*?)</title>",response.text)
                print(title)

            else:
                title = "没有标题"
                print(title)

            if response.xpath("//div/p/text()").extract():
                neirong = response.xpath("//div/p/text()").extract()
                print(neirong)

            else:
                neirong = "没有内容"
                print(neirong)

            if response.xpath("//div[@id='mainDiv']//img/@src").extract():
                img_url = response.xpath("//div[@id='mainDiv']//img/@src").extract()
                print(img_url)

            else:
                img_url = "没有图片"
                print(img_url)
            if response.xpath("//div[@class='xg_rc']/p[@id='itag']/a/text()").extract():
                keysword = response.xpath("//div[@class='xg_rc']/p[@id='itag']/a/text()").extract()
                print(keysword)

            else:
                keysword = "没有关键字"
                print(keysword)

            if response.xpath('//meta[@name="keywords"]/@content').extract():
                data_time = response.xpath("//div[@class='box']/h1[@class='h1']/div[@class='p']/text()").extract()
                print(data_time)

            else:
                data_time = "没有时间"
                print(data_time)

            if response.xpath('//meta[@name="description"]/@content').extract():
                description = response.xpath('//meta[@name="description"]/@content').extract()
                print(description)

            else:
                description = "没有导读"
                print(description)


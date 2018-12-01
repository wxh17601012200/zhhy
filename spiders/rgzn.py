# -*- coding: utf-8 -*-
import scrapy


class RgznSpider(scrapy.Spider):
    name = 'rgzn'
    # allowed_domains = ['www.wang.com']
    # start_urls = ['http://www.wang.com/']
    def start_requests(self):
        for i in range(1,3):
            url='http://www.ailab.cn/?page='+str(i)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        hrefs = response.xpath("//li/a[@class='title']/@href").extract()
        for href in hrefs:
            yield scrapy.Request(url=href,callback=self.parse1)
    def parse1(self,response):
        try:
            if  response.xpath("//h3/text()").extract():
                title = response.xpath("//h3/text()").extract()
                print(title)
            else:
                raise Exception('title is null')
            if response.xpath("//p/span[@class='spanimg3']/text()").extract_first():
                time = response.xpath("//p/span[@class='spanimg3']/text()").extract_first()
                print(time)
            else:
                raise Exception('time is null')
        except:
            pass




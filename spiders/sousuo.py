# -*- coding: utf-8 -*-
import scrapy
import requests
from readability import Document

class SousuoSpider(scrapy.Spider):
    name = 'sousuo'
    # allowed_domains = ['www.sousuo.com']
    start_urls = ['http://search.people.com.cn/cnpeople/search.do?pageNum=1&keyword=%D0%C2%CE%C5&siteName=news&facetFlag=true&nodeType=belongsId&nodeId=0']
    # def start_requests(self):
    #     for i in range(1,6):
    #         url = 'http://search.people.com.cn/cnpeople/search.do?pageNum='+str(i)+'&keyword=%D0%C2%CE%C5&siteName=news&facetFlag=true&nodeType=belongsId&nodeId=0'
    #         yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        hrefs = response.xpath("//li/b/a/@href").extract()
        # print(len(hrefs))
        for href in hrefs:
            yield scrapy.Request(url=href,callback=self.parse1)
    def parse1(self,response):
        title = response.xpath("//h1/text()").extract()
        author = response.xpath("//p[@class='sou1']/text()").extract()
        print(title,author)


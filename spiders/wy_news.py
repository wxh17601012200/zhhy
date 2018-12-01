# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
class Wynews(CrawlSpider):
    name = 'wynews'
    allowed_domains = []
    start_urls = ['http://tech.163.com/gd/']

    rules = (
        Rule(LinkExtractor(allow="http://tech.163.com/special/gd2016_0\d+/"),follow=True),
        Rule(LinkExtractor(allow="http://tech.163.com/(.*?).html",restrict_css="h3.bigsize a"),
             callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        se1 = Selector(response)
        try:
            if se1.xpath("//div[@id='epContentLeft']/h1/text()"):#标题
                title = se1.xpath("//div[@id='epContentLeft']/h1/text()").extract_first()
                print(title)
            else:
                raise Exception("title is null")
            if se1.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/text()"):#时间
                time =se1.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/text()").extract_first()
                print(time[:26])
            else:
                raise Exception("time is null")
            if se1.xpath("//div[@class='post_body']/div[@id='endText']/p/text()"):#正文
                zhenwen =se1.xpath("//div[@class='post_body']/div[@id='endText']/p/text()").extract()
            else:
                zhenwen = ''
            print(zhenwen)
            if se1.xpath("//div[@class='post_time_source']/a[@id='ne_article_source']/text()"):#来源
                laiyuan =se1.xpath("//div[@class='post_time_source']/a[@id='ne_article_source']/text()").extract_first()
            else:
                laiyuan = ''
            print(laiyuan)
            if se1.xpath("//div[@class='ep-source cDGray']/span[@class='ep-editor']/text()"):#作者
                zuozhe = se1.xpath("//div[@class='ep-source cDGray']/span[@class='ep-editor']/text()").extract_first()
            else:
                zuozhe = ''
            print(zuozhe)
            if re.findall('<meta name="keywords" content="(.*?)"/>',response.text):#关键字
                gjz = re.findall('<meta name="keywords" content="(.*?)"/>',response.text)[0]
            else:
                gjz = ''
            print(gjz)
            if re.findall('<meta name="description" content="(.*?)"/>',response.text):#导读
                dao = re.findall('<meta name="description" content="(.*?)"/>',response.text)[0]
            else:
                dao = ''
            print(dao)
        except:
            pass


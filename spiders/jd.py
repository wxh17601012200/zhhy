# -*- coding: utf-8 -*-
import scrapy,time


class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['www.jd.com']
    # start_urls = ['http://www.jd.com/']
    def start_requests(self):
        t = round(time.time(),5)
        urls=[
            'https://search.jd.com/Search?keyword=%E5%A4%A7%E5%9C%B0%E7%93%9C&enc=utf-8&pvid=5e74b46443d644d6a7883a48d51e4ff3',
            'https://search.jd.com/s_new.php?keyword=%E5%A4%A7%E5%9C%B0%E7%93%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1&page=2&s=30&scrolling=y&log_id='+str(t)
        ]
        # for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)
    # def parse(self, response):
    #     print(response.url)


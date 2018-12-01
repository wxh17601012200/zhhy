# -*- codeing:utf-8 -*-


import scrapy,re




class RenGongZhiNeng(scrapy.Spider):
    name = 'rgzn'
    allower_domains = []
    # start_urls = ['http://www.ailab.cn/?page=1']

    def start_requests(self):
        for i in range(1,3):
            url='http://www.ailab.cn/?page='+str(i)
            yield scrapy.Request(url,self.parse)
    def parse(self, response):
        hrefs=response.xpath("//li/a[@class='title']/@href").extract()
        for href in hrefs:
            # print(href)
            yield scrapy.Request(href,self.parse1)
    def parse1(self, response):
        try:
            if response.xpath("//div[@class='listltitle']/h3/text()").extract():
                title=response.xpath("//div[@class='listltitle']/h3/text()").extract_first()
                print(title)
            else:
                title=''
                # print(response.url)
                # raise Exception('title is none')
            if response.xpath("//p/span[@class='spanimg2']/text()").extract()[0]:
                laiyuan=response.xpath("//p/span[@class='spanimg2']/text()").extract()[0]
                print(laiyuan)
            else:
                laiyuan=''
            if response.xpath("//p/span[@class='spanimg3']/text()").extract()[0]:
                time=response.xpath("//p/span[@class='spanimg3']/text()").extract()[0]
                print(time)
            else:
                time=''
            article=response.xpath("//div[@id='mainDiv']/p/text()").extract()
            # for art in article:
            #     print('正文：'+art)
            keywords=re.findall('<meta name="keywords" content="(.*?)"/>',response.text)[0]
            print(keywords)
            description=re.findall('<meta name="description" content="(.*?)"/>',response.text)[0]
            print(description)
            if response.xpath("//p/img/@src").extract():
                image=response.xpath("//p/img/@src").extract()
                for ima in image:
                    print('http://www.ailab.cn'+ima)
            else:
                image=response.xpath("//center/img/@src").extract()
                for ima in image:
                    print('http://www.ailab.cn'+ima)
        except:
            print()
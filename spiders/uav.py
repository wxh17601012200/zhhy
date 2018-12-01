from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import requests,random


class Uav(CrawlSpider):
    name = 'uav'
    allowed_domains = []
    start_urls=  [
        "http://www.81uav.cn/uav-news/4.html"
    ]
    rules = (
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/4_\d+.html"),follow=True),
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html",restrict_css="div.news_left a"),callback="parse_item",follow=False)
    )

    def parse_item(self,response):
        # print(response.url)
        sel = Selector(response)
        if sel.xpath("//h1/text()").extract_first():#标题
            title = sel.xpath("//h1/text()").extract_first()
        else:
            title = ''
        print(title)
        if sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}"):#发布时间
            data_str = sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}")[0]
        else:
            data_str = ''
        print(data_str)
        if sel.css("div.info::text").re("\w+"):#来源
            source = sel.css("div.info::text").re("\w+")[5]
        else:
            source = ''
        print(source)
        try:
            if sel.css("div.info::text").re("\w+"):#作者
                author = sel.css("div.info::text").re("\w+")[7]
            else:
                author = ''
            print(author)
        except:
            pass
        if sel.xpath("//div[@id='article']/p/text()").extract():#正文
            conts = sel.xpath("//div[@id='article']/p/text()").extract()
            for cont in conts:
                print(cont)
        else:
            conts = ''
        if sel.xpath("//div[@id='article']/p/img/@src").extract():#图片文件
            imgs = sel.xpath("//div[@id='article']/p/img/@src").extract()
        else:
            imgs = ''
        for img in imgs:
            print(img)
            i = requests.get(img)
            id_name = str(random.randint(1,10000000000))
            # with open(id_name+'.jpg','wb')as f:
            #     f.write(i.content)
        if sel.xpath("//div[6]/a/text()").extract():#文章链接
            hrefs = sel.xpath("//div[6]/a/text()").extract()
        else:
            hrefs = ''
        for href in hrefs:
            print(href)






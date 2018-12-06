# -*- coding: utf-8 -*-
import scrapy,requests,random,os,json,re


class DySpider(scrapy.Spider):
    name = 'dy'
    # allowed_domains = ['www.dy.com']
    # start_urls = ['http://v1-dy.ixigua.com/5e746d2188f324b01893751cdffb7a1d/5c05e939/video/m/220559684d1c3e64992bc01c0638bee1c5211610ae3800006cfc081c763a/?rc=MzxzcXl4bXJsajMzaWkzM0ApQHRAbzhEOjU0OzgzNDMzPDc1OzNAKXUpQGczdylAZmh1eXExZnNoaGRmOzRAbDVqY2QyYm8tXy0tNi0vc3MtbyNvIy4uLjE1LS4tLTIxLS0uLi9pOmItbyM6YC1vI3BiZnJoXitqdDojLy5e ']
    headers = {
        'Host': 'api.amemv.com',
'Connection': 'keep-alive',
'Accept-Encoding': 'gzip',
'X-SS-TC':'0',
'User-Agent': 'com.ss.android.ugc.aweme/251 (Linux; U; Android 4.4.2; zh_CN; OPPO R11; Build/NMF26X; Cronet/58.0.2991.0)'
    }#接口的headers
    cookies ={'Cookie: install_id': '52967880819', ' ttreq': '1$9679e194560925274e19d68b3a91dcd9706774de', ' qh[360]': '1', ' odin_tt': '655046507a70544d6e6b43306f46504f7ad866f7f71ba9e93cf006ae6aa770138bdb8f7afbf9cabe850107ccce89e9ac'}#接口的cookie

    headers1={
        'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }#匹配出来的playadd的headers

    def start_requests(self):#起始url
        url = 'https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=0&user_id=60424463447&count=20&retry_type=no_retry&iid=52967880819&device_id=60118732048&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=251&version_name=2.5.1&device_platform=android&ssmix=a&device_type=OPPO+R11&device_brand=OPPO+&language=zh&os_api=19&os_version=4.4.2&uuid=355757010154546&openudid=9a541b94ce564513&manifest_version_code=251&resolution=1080*1920&dpi=320&update_version_code=2512&_rticket=1543895210556&ts=1543895209&as=a1a5df30896a8c58054355&cp=f2a0c159925d0584e1akio&mas=01d05b1cf812495c50b6fb5184e8ccf195acaccc2cac0c1cacc61c'
        yield scrapy.Request(url,callback=self.parse,headers=self.headers,cookies=self.cookies)
    def parse(self, response):#json匹配视频详情页的url
        data = json.loads(response.text).get("aweme_list")
        for d in data:
            url = d['share_url']
            yield scrapy.Request(url,callback=self.parse1,headers=self.headers1)
    def parse1(self,response):#正则匹配源码中的视频地址
        plays = re.findall(r'playAddr: "(.*?)",',response.text)
        for play in plays:
            yield scrapy.Request(url=play,callback=self.parse2,headers=self.headers1)
    def parse2(self,response):
            i=requests.get(response.url)
            path = './dy/'#同级建文件夹
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
            name = str(random.randint(1,100))#随机创建name
            with open('./dy/'+name+'.mp4','wb')as f:#保存到文件夹本地
                f.write(i.content)

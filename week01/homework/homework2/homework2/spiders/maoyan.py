'''
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址： https://maoyan.com/films?showType=3

要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
'''

'''
可以直接在电影清单页面直接抓取信息，为了便于以后抓取更多信息，同时练习老师讲的内容加深印象，
就直接爬到每部电影详细页面
'''
import scrapy
from scrapy.selector import Selector
from homework2.items import Homework2Item
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def start_requests(self):
        print('{:-^50}'.format('start'))
        for i in range(0, 1):#作业要求是只爬前十名，前十名在第一页，这里做一个扩展，如果要求爬前二十名的时候好修改
            url = f'https://maoyan.com/board/4?offset={i * 10}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        urls = Selector(response=response).xpath('//p[@class="name"]/a[1]/@href').extract()
        for url in urls:
            yield scrapy.Request(url='https://maoyan.com'+url, callback=self.parse2)
    
    def parse2(self, response):
        name = ('').join(Selector(response=response).xpath('//h1[@class="name"]/text()').extract())
        kind = ('').join(Selector(response=response).xpath('//a[@class="text-link"]/text()').extract()).replace(' ','')
        timer = ('').join(Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()').extract())[:10]
        item = Homework2Item()
        item['name'] = name
        item['kind'] = kind
        item['timer'] = timer
        yield item

# https://maoyan.com/films/247791
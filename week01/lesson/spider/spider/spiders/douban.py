import scrapy
from scrapy.selector import Selector
from spider.items import SpiderItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def start_requests(self):
        i = 0
        url = f'https://movie.douban.com/top250?start={i}&filter='
        yield scrapy.Request(url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            # print('--------------')
            # print(title)
            # print(link)
            print('--------------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())
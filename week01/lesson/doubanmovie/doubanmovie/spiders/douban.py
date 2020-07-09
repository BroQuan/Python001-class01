import scrapy
from bs4 import BeautifulSoup
from doubanmovie.items import DoubanmovieItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def start_requests(self):
        for i in range(1):
            url = f'https://movie.douban.com/top250?start={i * 25}&filter='
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        title_list = soup.findAll('div', {'class': 'hd'})
        for i in title_list:
            item = DoubanmovieItem()
            title = i.find('a').find('span').text 
            link = i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find('div', {'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item
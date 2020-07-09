import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

header = {'user-agent':UserAgent().random}
url = 'https://movie.douban.com/top250'

rq = requests.get(url, headers=header)
bs_info = bs(rq.text, 'html.parser')    #html.parser效率较低，我经常用lxml，需要库lxml

title = bs_info.select('#content > h1')[0].text
print(title)

movie_names = bs_info.findAll('div',{'class':'info'})
for i in movie_names:
    movie_name = i.find('span',{'class':'title'}).text
    print(movie_name)
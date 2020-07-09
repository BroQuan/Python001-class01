import requests
from lxml import etree
from fake_useragent import UserAgent
import pandas as pd

header = {'user-agent':UserAgent().random}
url = 'https://movie.douban.com/top250'
rq = requests.get(url, headers=header)

e_html = etree.HTML(rq.text)

names = e_html.xpath('//*[@id="content"]/div/div[1]/ol//li/div/div[2]/div[1]/a/span[1]/text()')
directors_time = e_html.xpath('//*[@id="content"]/div/div[1]/ol//li/div/div[2]/div[2]/p/text()')
directors = []
for i in range(0, len(directors_time), 4):
    directors.append(directors_time[i].replace(' ','').replace('\n','').split('\xa0')[0].replace("导演:",""))
show_time = []
for i in range(1, len(directors_time), 4):
    show_time.append(directors_time[i].replace(' ','').replace('\n','').split('\xa0')[0])

movies = [names, directors, show_time]
movies = (list(zip(*movies)))
print(movies)
movie_list = pd.DataFrame(data=movies)
movie_list.to_csv(r'./movielist.csv',encoding='utf-8',index=False,header=False)
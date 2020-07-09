'''
安装并使用 requests、bs4 库
爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
以 UTF-8 字符集保存到 csv 格式的文件中。
'''
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()
user_agent = ua.random

header = {'User-Agent': user_agent}
url = 'https://maoyan.com/board/4'
rq = requests.get(url=url, headers=header)
bs = BeautifulSoup(rq.text, 'lxml')
time.sleep(1)
movie_list = bs.find('dl', {'class': 'board-wrapper'}).findAll('p', {'class': "name"})
print(movie_list)
titles = []
types = []
times = []

for i in movie_list:
    time.sleep(1)
    url = 'https://maoyan.com' + i.find('a').get('href')
    rq = requests.get(url=url, headers=header)
    bs = BeautifulSoup(rq.text, 'lxml')
    titles.append(bs.find('h1', {'class': 'name'}).text)
    tmp = bs.findAll('li', {'class': 'ellipsis'})
    types.append(tmp[0].text.replace('\n', '').replace(' ', ''))
    times.append(tmp[2].text)

print(titles)
print(times)
print(types)

movies = [titles, times, types]
movies = (list(zip(*movies)))
top10 = pd.DataFrame(data=movies)
top10.to_csv(r'./maoyan10.csv',encoding='utf-8', index=False, header=False)
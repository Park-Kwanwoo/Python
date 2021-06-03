# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=thu'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

img_list = soup.find('ul', class_='img_list')
webtoons = img_list.select('dl')

lst = list()

for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    # print('{} [{}]'.format(title, star))
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)

# print(lst)
res = {}
res['webtoons'] = lst

res_json = json.dumps(res, ensure_ascii=False)

with open('webtoons.json', 'w', encoding='UTF-8') as f:
    f.write(res_json)

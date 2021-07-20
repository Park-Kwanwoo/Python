# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.iei.or.kr/intro/teacher.kh'
img_head = "https://www.iei.or.kr"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

teacher_list = soup.find('div', class_='intro_list')
teachers = teacher_list.select('li')

lst = list()

for teacher in teachers:
    name = teacher.find('p').text
    img_url = teacher.find('img')['src']
    tmp = {}
    tmp['name'] = name
    tmp['img'] = img_head + img_url
    lst.append(tmp)

res = {}
res['kh'] = lst
print(res)

res_json = json.dumps(res, ensure_ascii=False)

with open('teacher.json', 'w', encoding='UTF-8') as f:
    f.write(res_json)
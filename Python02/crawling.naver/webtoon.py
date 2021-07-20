# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re

for j in range(0, 7):
    url = 'https://www.iei.or.kr/intro/teacher.kh'
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, 'html.parser')
    webtoons = soup.select('li dl')
    i = 0
    match = re.search(r'[\w]', str(list(day.get(list(day.keys())[j]))))
    print(match.group())
    for webtoon in webtoons:
        i = i + 1
        if i <= 3:
            continue
        title = webtoon.find('a')['title']
        star = webtoon.find('strong').text
        print('{} [{}]'.format(title, star))



from bs4 import BeautifulSoup
import urllib.request
import re

day = {'mon': '월', 'tue': '화', 'wed': '수', 'thu': '목', 'fri': '금', 'sat': '토', 'sun': '일'}
for j in range(0, 7):
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + list(day.keys())[j]
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
        title = webtoon.find('a').text
        star = webtoon.find('strong').text
        print('{} [{}]'.format(title, star))



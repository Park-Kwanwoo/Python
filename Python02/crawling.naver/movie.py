# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(resp, 'html.parser')

movies = soup.find_all('dl', class_='lst_dsc')
# movies 안에 있는 제목과 별점을 pasing 해서 제목 [별점] 형태로 출력

for movie in movies:
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    print(title, ' [', star, ']')

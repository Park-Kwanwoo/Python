# -*- coding:utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/crawling')
def result_json():
    # https://movie.naver.com/movie/running/current.nhn
    # 제목, 별점을 {'title': 제목, 'star': 별점} 형태로 크롤링 후 {'movies' : [{}, {}, {}]} json객체를 만든 후 리턴
    url = 'https://movie.naver.com/movie/running/current.nhn#'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    movies = soup.find_all('dl', class_='lst_dsc')
    result_list = list()

    for movie in movies:
        res = dict()
        res['title'] = movie.find('a').text
        res['star'] = movie.select('.num')[0].text
        result_list.append(res)

    result_dict = {'movies': result_list}
    result_json = json.dumps(result_dict, ensure_ascii=False)

    return result_json
if __name__ == '__main__':
    app.run(host='localhost', port=8686)

# -*- coding:utf-8 -*-

from wordcloud import WordCloud
import json

cloud = WordCloud(font_path='Binggrae-Bold.otf', background_color='white', max_words=30, width=400, height=300)

with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)


res = dict()
for wt in webtoon['webtoons']:
    res[wt['title']] = int(float(wt['star']) * 100)

visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud.png')

# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.score

# res01 = collection.insert_one({'name': '모두한', 'kor': 56, 'eng': 87, 'math': 100})
# print(res01.inserted_id)

"""
res02 = collection.insert_many(
    [
        {'name': '안재웅', 'kor': 90, 'eng': 80, 'math': 70},
        {'name': '벡주환', 'kor': 80, 'eng': 80, 'math': 80},
        {'name': '박태영', 'kor': 70, 'eng': 80, 'math': 90}]
)
"""
# print(res02.inserted_ids)

for doc in collection.find():
    print(doc)
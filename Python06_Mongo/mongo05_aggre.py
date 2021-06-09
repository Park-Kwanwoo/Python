# -*- coding:utf-8 -*-

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.test
collection = db.score

# math 점수가 80보다 큰 document들의 math 평균
aggre = collection.aggregate(
    [
        {'$match': {'math': {'$gt': 70}}},
        # {'$project': {'math': 1}},
        {'$group': {'_id': 'math', 'average': {'$avg': '$math'}}}
    ]
)

print(aggre)
pprint(list(aggre))
# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.score

# res01 = collection.delete_one({'name': '조세호'})
# print(res01.deleted_count)

# test field가 존재하는 모든 document
# res02 = collection.delete_many({'test': {'$exists': True}})
# print(res02.deleted_count)

# 모든 document들을 삭제
# collection.delete_many({})

for doc in collection.find():
    print(doc)



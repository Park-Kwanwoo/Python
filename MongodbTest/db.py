from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.newDB  # db 를 하나 만들고
userCollection = db.user  # db 에서 collection 을 만든다.

# insert_one() 으로 db 를 추가
userCollection.insert_one({'name': 'mik_a', 'age': '100'})
userCollection.insert_one({'name': 'kim', 'age': '100'})
userCollection.insert_one({'name': 'park', 'age': '100'})
userCollection.insert_one({'name': 'lee', 'age': '100'})
# find() 로 collection 에 저장된 데이터를 불러와서 출력한다
for i in userCollection.find():
    print(i)


# collection 의 데이터를 전부 삭제한다.
userCollection.delete_many({})

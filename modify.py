#-*-


from pymongo import MongoClient

client = MongoClient()
db = client.snack
comments=db.comments


for doc in comments.find({}):
		print doc

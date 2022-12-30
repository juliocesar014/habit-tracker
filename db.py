from pymongo import MongoClient

## Create you db in MongoDB Compass (localhost)

client = MongoClient('mongodb://localhost:27017')
db = client.allhabits ##DB: allhabits
collection = db.habits ##Collection = habits
print(db)
print(collection)



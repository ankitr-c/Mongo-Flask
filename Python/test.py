from pymongo import MongoClient
import datetime
from bson import ObjectId
uri='mongodb+srv://bbt0987:BBT0987@cluster0.jcazi2w.mongodb.net/?retryWrites=true&w=majority'
client=MongoClient(uri)

db=client.get_database('userdb')
table=db.get_collection('Todo')

def insert_data():
    data={
        "title":"test2 title",
        "desc":"test2 desc",
        "created_date":datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S"),
    }
    table.insert_one(data)                 
# insert_data()
def delete_data():
    table.delete_one({"_id": ObjectId("6546a061d68afb3f6541dea5")})
# delete_data()
def show_all():
    data=list(table.find())
    print()
    for ch in data:
        print(ch)

show_all()
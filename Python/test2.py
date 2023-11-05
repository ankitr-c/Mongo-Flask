from pymongo import MongoClient
import datetime
from bson import ObjectId
from flask import Flask,jsonify,request

uri='mongodb+srv://bbt0987:BBT0987@cluster0.jcazi2w.mongodb.net/?retryWrites=true&w=majority'
client=MongoClient(uri)

db=client.get_database('userdb')
table=db.get_collection('Todo')

app=Flask(__name__)


@app.route('/')
def show_all():
    data=list(table.find())
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(list(data))
    # for ch in data:
    #     print(ch)

@app.route('/insert', methods=['POST'])
def insert_data():
    data={
        "title":request.form['title'],
        "desc":request.form['desc'],
        "created_date":datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S"),
    }
    table.insert_one(data)   
    return 'data inserted successfully'              
# insert_data()
def delete_data():
    table.delete_one({"_id": ObjectId("6546a061d68afb3f6541dea5")})
delete_data()


if __name__ == "__main__":
    app.run(debug=True, port=8000)
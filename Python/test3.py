from pymongo import MongoClient
import datetime
from bson import ObjectId
from flask import Flask,jsonify,request,redirect,render_template

uri='mongodb+srv://bbt0987:BBT0987@cluster0.jcazi2w.mongodb.net/?retryWrites=true&w=majority'
client=MongoClient(uri)

db=client.get_database('userdb')
table=db.get_collection('Todo')

app=Flask(__name__)


@app.route('/', methods=['POST'])
def insert_data():
    data={
        "title":request.form['title'],
        "desc":request.form['desc'],
        "created_date":datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S"),
    }
    table.insert_one(data)   
    return render_template('index.html', data=data)

@app.route('/delete', methods=['POST'])
def delete_data():
    table.delete_one({"_id": ObjectId("6546a061d68afb3f6541dea5")})
    table.delete_one({"_id": ObjectId(request.form['title'])})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
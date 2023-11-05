from flask import Flask, render_template, request, redirect
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Replace with your MongoDB Atlas connection string
app.config['MONGO_URI'] = 'mongodb+srv://bbt0987:BBT0987@cluster0.jcazi2w.mongodb.net/?retryWrites=true&w=majority'

# mongo = PyMongo(app)
client=MongoClient('mongodb+srv://bbt0987:BBT0987@cluster0.jcazi2w.mongodb.net/?retryWrites=true&w=majority')
db= client.get_database('userdb')
todos=db.get_collection('Todo')
# Define a collection for your Todos
# todos = mongo.db.userdb

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        created_date = datetime.utcnow()
        todo = {"title": title, "desc": desc, "date_created": created_date}
        todos.insert_one(todo)

    allTodo = todos.find()
    return render_template('index.html', allTodo=allTodo)

@app.route('/update/<ObjectId:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todos.update_one({"_id": sno}, {"$set": {"title": title, "desc": desc}})
        return redirect("/")

    todo = todos.find_one_or_404({"_id": sno})
    return render_template('update.html', todo=todo)

@app.route('/delete/<ObjectId:sno>')
def delete(sno):
    todos.delete_one({"_id": sno})
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

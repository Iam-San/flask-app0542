import pymongo
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET',]) # To render Homepage
def home_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])  # This will be called from UI
def handle_login():
    if (request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        client = pymongo.MongoClient(f"mongodb+srv://root:root@cluster0.7hiaf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['flask_web_app']
        coll = db['webapp_log']
        coll.insert_one({'username': username,
                         'password': password,
                         'time_stamp': str(datetime.now())})
        return render_template('logout.html')


@app.route('/logout', methods=['POST'])  # This will be called from UI
def handle_logout():
    if (request.method=='POST'):
        return render_template('login.html')



if __name__ == '__main__':
    app.run()

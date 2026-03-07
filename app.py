from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://weecan2026_db_user:hk1234@flasklearner.abs2boi.mongodb.net/?appName=flasklearner")
db = client["studentDB"]
collection = db["students"]

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        data = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
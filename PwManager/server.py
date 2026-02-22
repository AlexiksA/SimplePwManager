from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import PwManager as pman

app = Flask(__name__)
CORS(app)

@app.route('/')
def showIndex():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def genKey():
    key = pman.genKey()
    data = ({"key": key})
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def getKey():
    key = request.form.get('my_data')
    data = pman.viewPw(key)
    dict = []
    for i in data:
        user, pswd = i.split('|')
        dict.append({"user": user, "password": pswd})
   
    return jsonify(dict)

app.run(debug=True, port=5000)
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import PwManager as pman

app = Flask(__name__)
CORS(app)

@app.route('/')
def showIndex():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def addKey():
    name = request.form.get("usern")
    pwd = request.form.get("passw")
    key = request.form.get("keyIn")
    if name and pwd and key:
        pman.addPw(name, pwd, key)
        return jsonify({"status": "succes", "message": "cont trimis"})
    return jsonify({"status": "error", "message": "ai uitat sa scrii ceva"}), 400

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
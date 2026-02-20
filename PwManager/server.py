from flask import Flask, jsonify, request
from flask_cors import CORS
import PwManager as pman

app = Flask(__name__)
CORS(app)

@app.route('/get', methods=['GET'])
def GetPw():
    pman.viewPw()
    data = {'user':'gigel', 'password':'12345'}
    return jsonify(data)


app.run(debug=True, port=5000)
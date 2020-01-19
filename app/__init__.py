from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "hello ljs93kr!!"


@app.route('/data')
def data():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    print(type(data))
    return jsonify(data)


@app.route('/login', methods=['GET'])
def login():
    user = request.args.get('userId')
    returndata = {'userId': user, 'password': '1234!@#$'}
    return jsonify(returndata)


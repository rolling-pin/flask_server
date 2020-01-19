from flask import Flask
from flask import jsonify, request
from app.models.user import *

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route('/login', methods=['GET'])
def login():
    returndata = getUser(request.args)
    return jsonify(returndata)


@app.route('/login', methods=['POST'])
def regist():
    returndata = registUser(request.get_json())
    return jsonify(returndata)


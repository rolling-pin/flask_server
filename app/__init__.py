from flask import Flask
from flask import jsonify, request
from app.models.user import *
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route('/data')
def data():
    returnValue = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(returnValue)


@app.route('/login', methods=['GET'])
def login():
    returndata = getUser(request.args)
    return jsonify(returndata)


@app.route('/login', methods=['POST'])
def regist():
    returndata = registUser(request.get_json())
    return jsonify(returndata)


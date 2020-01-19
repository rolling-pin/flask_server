from flask import Flask
from flask import jsonify, request
from app.models.database import *
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
    args = request.args

    db = Database()
    query = 'SELECT * FROM "USER_INFO" WHERE "LOGIN_ID" = %s AND "LOGIN_PW" = %s'
    param = [args.get('loginId'), args.get('password')]
    result = db.excuteQuery(query, param)

    returndata = {'errorcode': 1, 'msg': 'invalid ID or Password'}
    if result:
        returndata = {'errorcode': 0, 'msg': 'exist user', 'result': 'OK', 'userId': result[0][1], 'password': result[0][4], 'email': result[0][0], 'userNm': result[0][2]}

    return jsonify(returndata)


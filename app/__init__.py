from flask import Flask
from flask import jsonify, request
import psycopg2

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
    connectionInfo = "host='rollingpin-db.caduakykgikn.ap-northeast-2.rds.amazonaws.com' dbname='postgres' user='rollingpin' password='rollingpin'"
    connection = psycopg2.connect(connectionInfo)
    cur = connection.cursor()

    loginId = request.args.get('loginId')
    password = str(request.args.get('password'))
    cur.execute('SELECT * FROM "USER_INFO" WHERE "LOGIN_ID" = %s AND "LOGIN_PW" = %s', [loginId, password])
    result = cur.fetchall()
    returndata = {'result': 'no data'}
    if(result):
        returndata = {'result': 'OK','userId': result[0][1], 'password': result[0][4], 'email': result[0][0], 'userNm': result[0][2]}

    return jsonify(returndata)


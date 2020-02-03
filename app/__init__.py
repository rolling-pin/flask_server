from flask import Flask
from flask import jsonify, request
import app.models.user as user
import app.models.category as category

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route('/login', methods=['GET'])
def getUser():
    returndata = user.getUser(request.args)
    return jsonify(returndata)


@app.route('/registUser', methods=['POST'])
def registUser():
    returndata = user.registUser(request.get_json())
    return jsonify(returndata)


@app.route('/getTotalFavorite', methods=['GET'])
def getTotalFavorite():
    returndata = category.getTotalFavorite(request.args)
    return returndata


@app.route('/getUserFavorite', methods=['GET'])
def getUserFavorite():
    returndata = category.getUserFavorite(request.args)
    return returndata


@app.route('/registUserFavorite', methods=['POST'])
def registUserFavorite():
    returndata = category.registUserFavorite(request.get_json())
    return jsonify(returndata)


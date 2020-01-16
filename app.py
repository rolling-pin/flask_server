from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data')
def data():
    jsonData = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(jsonData)

if __name__ == '__main__':
    app.run()

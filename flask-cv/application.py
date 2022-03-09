from crypt import methods
from flask import Flask, request, jsonify
import requests
import json

application = app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return {'msg': 'This is a post request'}
    return {'msg': 'This is a get request'}

@app.route('/<name>', methods=['GET'])
def identification(name):
    return {'message': 'My name is ' +name+ ', Welcome to API'}


#Run server
if __name__ == '__main__':
    app.run(debug=True, port=8082)
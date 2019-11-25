#!flask/bin/python
from flask import Flask, request
from flask_restful import Api
import requests
import os

app = Flask(__name__)
api = Api(app)

prox_ip = os.environ["prox_ip"]
print(prox_ip)

@app.route('/', defaults={'path': ''},methods = ['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])

def catch_all(path):
	if request.method == 'POST':
		req = requests.post('http://' + prox_ip + ':5000' + '/' + path,  headers=request.headers,  json=request.get_json())
		return req.content
	elif request.method == 'PUT':
		req = requests.put('http://' + prox_ip + ':5000' + '/' + path, headers=request.headers,  json=request.get_json())
		return req.content
	elif request.method == 'DELETE':
		req = requests.delete('http://' + prox_ip + ':5000' + '/' + path)
		return req.content
	elif request.method == 'GET':
		req = requests.get('http://' + prox_ip + ':5000' + '/' + path)
		return req.content

@app.route('/healthcheck')
def healthy():
	return 'healthy',200

if __name__ == '__main__':
	app.run('0.0.0.0',port=5000)
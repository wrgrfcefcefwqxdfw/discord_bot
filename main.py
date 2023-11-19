from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class HelloWorld(Resource):
    def get(self):
        return {'rohan': 'bruh'}


class Name(Resource):
    def get(self, name):
        return jsonify({'hello': name})


api.add_resource(HelloWorld, '/')
api.add_resource(Name, '/name/<str:name>')

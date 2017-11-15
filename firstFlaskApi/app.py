from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

student = []

class Student(Resource):
    def get(self, name):
        return {"message": name}

    def post(self, name):
        data = request.get_json()
        return data["price"], 201

api.add_resource(Student, '/student/<string:name>')

app.run(port=8000, debug=True)

from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Welcome(Resource):
    def get(self):
        return {'welcome': 'Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!'}
        
class Motivation(Resource):
    def get(self):
        message = """Na het volgen van de bootcamp hoop ik: Een beter beeld te hebben van best practices op het gebied van 
        testautomatisering; Te leren van inzichten en perspectieven van mede-bootcampers; Uitgedaagd te worden om een nieuwe
        test tool en programmeertaal te proberen; Mijn portfolio met test automation code met een flink aantal scripts uit
        te breiden; Beter te begrijpen hoe je test automation aan pakt om zinnige en stabiele testcases te maken, en 
        last but certainly not least: Het lijkt me gewoon heel erg vet om aan de bootcamp mee te doen!!
            """

        return {'hello': 'world',
            'message': message}

api.add_resource(HelloWorld, '/')
api.add_resource(Welcome, '/welcome/')
api.add_resource(Motivation, '/motivation/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
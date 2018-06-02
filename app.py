from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/welcome/")
def welcome():
    message = "Welkom bij de bootcamp toelatings opdracht. Werk alsjeblieft zorgvuldig en netjes. Succes!!"
    return jsonify(
        author="unknown",
        message=message
    )

@app.route("/motivation/")
def motivation():
    message = """Na het volgen van de bootcamp hoop ik: Een beter beeld te hebben van best practices op het gebied van 
testautomatisering; Te leren van inzichten en perspectieven van mede-bootcampers; Uitgedaagd te worden om een nieuwe
test tool en programmeertaal te proberen; Mijn portfolio met test automation code met een flink aantal scripts uit
te breiden; Beter te begrijpen hoe je test automation aan pakt om zinnige en stabiele testcases te maken, en 
last but certainly not least: Het lijkt me gewoon heel erg vet om aan de bootcamp mee te doen!!
    """

    return jsonify(
        author="Ico Bakker",
        message=message
    )


if __name__ == '__main__':
    app.run(debug=True)
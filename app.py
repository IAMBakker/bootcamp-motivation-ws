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
        status="200",
        message=message
    )

@app.route("/motivation/")
def motivation():
    message = "Hier komt mijn motivatie"
    return jsonify(
        status="200",
        message=message
    )


if __name__ == '__main__':
    app.run(debug=True)
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
    message = "Spicy jalapeno bacon ipsum dolor amet ham pork fatback, meatball chuck turkey sirloin ribeye jowl " \
              "tri-tip alcatra bresaola prosciutto boudin. Porchetta boudin pork chop landjaeger burgdoggen bacon " \
              "ribeye filet mignon spare ribs pastrami chicken fatback capicola venison t-bone. Capicola turducken " \
              "shank, pancetta cow pork belly pork loin porchetta drumstick burgdoggen. Hamburger biltong short ribs," \
              " cow andouille t-bone jerky ham spare ribs tail landjaeger beef turkey buffalo swine."
    return jsonify(
        author="Ico Bakker",
        message=message
    )


if __name__ == '__main__':
    app.run(debug=True)
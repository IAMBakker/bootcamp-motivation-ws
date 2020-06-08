# bootcamp-motivation-ws
A small webservice responsible for delivering messages for the bootcamp assignment

## How to run:
1) Optional: create a virtual environment for the project.
2) Run `pip install -r requirements.txt`
3) Run `python app.py` to "deploy" the service.

## How to run (using docker):
1) Run `docker image build -t flask-webservice .`
2) Run `docker container run -p 5000:5000 --name flask-motivation-ws flask-webservice`

## How to use:
1) Visit `localhost:5000/motivation` in your favourite browser
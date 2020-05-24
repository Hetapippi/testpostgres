import flask
from main import app

@app.route('/')
def show_hello():
    return 'Hello Heroku World!'

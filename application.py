from flask import Flask
application = Flask(__name__)
app = application

@application.route('/')
@application.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@application.route('/about/')
def about():
    return '<h3>Moovbot.</h3>'

from flask import Flask
application = Flask(__name__)
app = application

@application.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

from flask import Flask
application = Flask(__name__)
app = application


@application.route('/')
def hello_world():
    return 'Hi! Its Moovbot,How can I help you'

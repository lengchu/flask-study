from flask import Flask

app = Flask(__name__)

route = app.route

@route('/', methods = ['GET'])
def home():
    return '<h1>Home</h1>'


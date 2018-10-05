from flask import Flask, render_template, session
from models import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
route = app.route

@route('/', methods = ['GET'])
def home():
    user_id = session.get('user_id')
    if user_id is None:
        name = ''
    else:
        user = User.get_by_id(user_id)
        name = user.username
    return render_template('index.html', name = name)


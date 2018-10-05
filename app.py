from flask import Flask, render_template, session, g, Blueprint
from models import User
from utils import login_required, register_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
route = app.route
register_bp(app)

@route('/', methods = ['GET'])
@login_required
def home():
    name = g.user.username
    return render_template('index.html', name = name)


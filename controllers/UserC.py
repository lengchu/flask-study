from flask import session, Blueprint, render_template
from models import User

bp = Blueprint('user', __name__)

@bp.route('/user', methods = ['GET'])
def findUser(): 
    return '<h1>user</user>'


@bp.route('/login', methods = ['GET'])
def login():
    return render_template('login.html', action = '/login')


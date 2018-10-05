from app import route, render_template
from flask import request
from models import User

@route('/user', methods = ['GET'])
def findUser(): 
    return '<h1>user</user>'


@route('/login', methods = ['GET'])
def login():
    return render_template('login.html', action = '/login')


@route('/login', methods = ['POST'])
def handleLogin():
    un = request.form['username']
    pw = request.form['password']
    try:
        user = User.get(User.username==un,
                        User.password==pw)
        return user.username
    except:
        return 'username and passwor not match'


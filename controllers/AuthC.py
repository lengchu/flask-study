import functools
from flask import redirect, g, url_for, Blueprint, session, request
from models import User

bp = Blueprint('auth', __name__)

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('user.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.get_by_id(user_id)


@bp.route('/login', methods = ['POST'])
def handleLogin():
    un = request.form['username']
    pw = request.form['password']
    try:
        user = User.get(User.username==un,
                        User.password==pw)
        session['user_id'] = user.id
        return redirect('/')
    except:
        return 'username and passwor not match'


@bp.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return redirect('/')


@bp.route('/register', methods = ['POST'])
def handleRegister():
    un = request.form['username']
    pw = request.form['password']
    try:
        user = User.create(username = un, password = pw)
        session['user_id'] = user.id
        return redirect('/')
    except:
        return 'unknown errore'


from UserC import bp as userBp
from AuthC import login_required, bp as authBp

def register_bp(app):
    app.register_blueprint(userBp)
    app.register_blueprint(authBp)


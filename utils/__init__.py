from flask import Blueprint
from auth import login_required, bp

def register_bp(app):
    app.register_blueprint(bp)

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from app.views import api_bp
from app import db, app


def setup_app():
    auth = HTTPBasicAuth()
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(api_bp)
    db.init_app(app)

    return app



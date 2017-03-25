from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from app.views import api_bp
from app import db, app

auth = HTTPBasicAuth()
app.config['DEBUG'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(api_bp)
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100,
            debug=False)
    # app.run(host='localhost', port=5100,
    #         debug=False)

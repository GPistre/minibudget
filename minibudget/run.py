from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from setup_app import setup_app

application = setup_app()

if __name__ == '__main__':
    # application.run(host='0.0.0.0', port=5100,
    #             debug=False)
    application.run()

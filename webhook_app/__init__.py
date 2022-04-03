import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort
from scripts.auth import twitter_auth
import webhook_app.config


api = twitter_auth()
db = SQLAlchemy()
has_db_connection = False

def create_app(test_config=None):
    """
    """
    # ref: https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/
    # ref: https://towardsdatascience.com/how-to-set-up-a-production-grade-flask-application-using-application-factory-pattern-and-celery-90281349fb7a
    app = Flask(__name__)
    FLASK_CONFIG_TYPE = os.getenv('FLASK_CONFIG_TYPE', default = 'webhook_app.config.DevelopmentConfig')
    app.config.from_object(FLASK_CONFIG_TYPE)

    from . import webhooks
    app.register_blueprint(webhooks.bp)
    
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    return app


import os
from flask import Flask, request, abort

def create_app(test_config=None):
    """
    """
    # ref: https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/
    # ref: https://towardsdatascience.com/how-to-set-up-a-production-grade-flask-application-using-application-factory-pattern-and-celery-90281349fb7a
    app = Flask(__name__)
    
    from webhook_app.config import DevelopmentConfig, ProductionConfig
    FLASK_CONFIG_TYPE = ProductionConfig
    app.config.from_object(FLASK_CONFIG_TYPE)

    from webhook_app.models import db
    db.init_app(app)

    from webhook_app.webhooks import bp
    app.register_blueprint(bp)
  
    return app


import os

class Config(object):
    """
    """
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', default='dev')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', default='postgres://development...')
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', default='postgres://testing...')


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default='postgres://production...')
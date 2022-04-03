from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Account(db.Model):
    """
    Class object for modeling tweet for database
    """
    __tablename__ = 'account'
    account_id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(15))
    created_at = db.Column(db.DateTime)


class Tweet(db.Model):
    """
    Class object for modeling tweet for database
    """
    __tablename__ = 'tweet'
    tweet_id = db.Column(db.Integer, primary_key=True)
    tweet_text = db.Column(db.String(280))
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    created_at = db.Column(db.DateTime)

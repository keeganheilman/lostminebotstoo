import os
import tweepy


def twitter_auth(
        c_key=None,
        c_secret=None,
        a_token=None,
        a_secret=None):
    """
    Return: tweepy API object (with keys and secrets)
    """

    consumer_key = os.getenv('CONSUMER_KEY', default = c_key)
    consumer_secret = os.getenv('CONSUMER_SECRET', default = c_secret)
    access_token = os.getenv('ACCESS_TOKEN', default = a_token)
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET', default = a_secret)
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


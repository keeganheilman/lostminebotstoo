import secrets
import tweepy

def authenticate(
        c_key=None,
        c_secret=None,
        a_token=None,
        a_token_secret=None):
    secret = Secret()
    consumer_key = c_key or secret.consumer_key
    consumer_secret = c_secret or secret.consumer_secret
    access_token = a_token or secret.access_token
    access_token_secret = a_token_secret or secret.access_token_secret
    auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret, access_token, access_token_secret)

    return tweepy.API(auth)


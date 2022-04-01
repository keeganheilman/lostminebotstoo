import tweepy
import psycopg2
from secrets import Secret

def twitter_auth(
        c_key=None,
        c_secret=None,
        a_token=None,
        a_token_secret=None):
    secret = Secret()
    consumer_key = c_key or secret.consumer_key
    consumer_secret = c_secret or secret.consumer_secret
    access_token = a_token or secret.access_token
    access_token_secret = a_token_secret or secret.access_token_secret
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def sql_auth(
        s_user=None,
        s_pw=None,
        s_host=None,
        s_port=None,
        s_db=None):
    secret = Secret()
    sql_user = s_user or secret.sql_username
    sql_pw = s_pw or secret.sql_pw
    sql_host = s_host or secret.sql_host
    sql_port = s_port or secret.sql_port
    sql_db = s_db or secret.sql_db
    cursor=None
    try:
        conn = psycopg2.connect(
            user=sql_user,
            password=sql_pw,
            host=sql_host,
            port=sql_port,
            database=sql_db)
        cursor = conn.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return cursor


def _test():
    return False

if __name__ == '__main__':
    _test()
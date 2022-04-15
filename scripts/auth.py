# MIT License

# Copyright (c) 2022 Molly White

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import tweepy
import psycopg2
from secrets import Secret

def twitter_auth(
        c_key=None,
        c_secret=None,
        a_token=None,
        a_token_secret=None):
    """
    Return: tweepy API object (with keys and secrets)
    """
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
    """
    Return: psycopg2 cursor object (connected) 
    """
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
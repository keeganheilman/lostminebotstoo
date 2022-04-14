from scripts.auth import twitter_auth
from scripts.auth import sql_auth
import pandas as pd
from pandas import json_normalize
import os  
import logging

# logging.basicConfig(level=logging.DEBUG)

# logger = logging.getLogger("Tweepy")
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename="tweepy.log")
# logger.addHandler(handler)





def tweets_to_csv(df, filepath='data/tweets.csv'):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  
    df.to_csv(filepath)



def get_twitter_api():
    return twitter_auth()

def get_psql_api():
    return sql_auth()


def retrieve_tweets(twi_api):
    """
    Retrieve the n most recent tweets by an user_handle
    n may be greater than 200; use paging. If rate limits or paging limits are reached,
      exit gracefully and return the tweets that have been retrieved.
    
    Return a list of tweepy Status objects
    """
              
    return twi_api.home_timeline(count=1)



def create_tweets_dataframe(tweets):
    """
    Create a dataframe from a given sequence of tweets, each represented by one tweepy Status object.
    The dataframe should have the following columns:
        'retweet_count', int
        'created_at', datetime
        'full_text', string
        'favorited', bool
        'retweeted', bool
        'lang', string
        'favorite_count', int
        'hashtags', [string]
        'user_mentions', [string]
        'urls', [string]
    """
    df_array = []
    for tweet in tweets:
        df_array.append(tweet._json)

    t_df = json_normalize(df_array)
    t_df = t_df[['id','used.id','text','created_at']]
    t_df.rename(columns = {'id':'tweet_id','user.id':'account_id'})
    return t_df


if __name__ == "__main__":
    print("SCRATCH.py...")
    twi_api = get_twitter_api()
    # sql_api = get_psql_api()
    screen_names = ['lostminebotstoo', 'keeganheilman']
    for sn in screen_names:
        print(f'{sn}: {twi_api.get_user(screen_name=sn).id}')

    # latest_tweet = retrieve_tweets(twi_api)
    # print(latest_tweet)
    # df = create_tweets_dataframe(latest_tweet)
    # tweets_to_csv(df)


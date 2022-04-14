from scripts.auth import twitter_auth
from datetime import datetime
from scripts.honeypot import write_honeypot_tweet

api = twitter_auth()

def get_latest_tweet():
    """
    """
    latest = api.home_timeline(count=1)
    print(latest)
    return latest

def send_tweet(status_update):
    """
    """
    api.update_status(status_update)


if __name__ == "__main__":
    print(len(get_latest_tweet()))
    status_update = write_honeypot_tweet()
    send_tweet(status_update)


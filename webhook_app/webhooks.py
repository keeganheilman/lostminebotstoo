import base64
import hashlib
import hmac
import re
import json
import os
from flask import Blueprint, request, abort
from webhook_app.webhooks_data import *
from webhook_app.auth import twitter_auth

api = twitter_auth()

bp = Blueprint('webhooks', __name__)
  
@bp.route('/hello', methods=['GET'])
def hello():
    # print(request.json)
    return 'Hello World!'


# Defines a route for the POST request
@bp.route("/", methods=["POST"])
def handle_webhook():
    if not is_valid_webhook(request):
        abort(403)
    body = request.json
    if "tweet_create_events" in body:
        handle_events(body["tweet_create_events"])
    return "", 204


# ref:https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks
# Defines a route for the GET request
@bp.route('/', methods=['GET'])
def webhook_challenge():
    # creates HMAC SHA-256 hash from incomming token and your consumer secret
    sha256_hash_digest = hmac.new(
        os.getenv('CONSUMER_KEY', default=''),
        msg=request.args.get('crc_token'),
        digestmod=hashlib.sha256
    ).digest()

    # construct response data with base64 encoded hash
    response = {
        'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
    }

    # returns properly formatted json response
    return json.dumps(response)        


### Helper
def is_probably_spam(tweet):
    """
    Some additional checks so that people who interact with the bot in good faith won't all get reported.
    """
    if len(tweet["entities"]["urls"]) > 0:
        # Contains a URLredis from_url psycopg2 equivalentd
        return True
    if re.search(EMAIL_PATTERN, tweet["text"]):
        # Contains an email address; https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        return True
    if re.search(SCAMMY_PATTERN, tweet["text"]):
        # With the easy tells out of the way, check for some other common indicators
        return True
    return False


def report(users):
    """
    Send reports and record the number of users reported
    """
    for user in users:
        api.report_spam(user_id=user["id"])
        print("Reported user:", user["screen_name"])

    # if has_db_connection:
    #     reported = int(db.get("reported")) or 0
    #     reported += len(users)
    #     print("Total # reported:", reported)

    #     db.set("reported", reported)


def handle_events(events):
    """
    Handles tweets, retweets, replies, quote tweets, mentions
    """
    to_report = []
    for event in events:
        if event["user"]["id"] in ALLOWLISTED_USER_IDS:
            # Avoid reporting the bot itself, Molly, etc.
            continue
        if event["in_reply_to_user_id"] == BOT_ID or (
            event["is_quote_status"] and event["quoted_status"]["user"]["id"] == BOT_ID
        ):
            # Reply to the bot, quote tweet of the bot
            if is_probably_spam(event):
                to_report.append(event["user"])
    if len(to_report) > 0:
        report(to_report)


def is_valid_webhook(req):
    """
    Check the webhook signature to ensure this came from Twitter
    """
    if req.headers.has_key("x-twitter-webhooks-signature"):
        signature = req.headers.get("x-twitter-webhooks-signature")
        request_body = req.get_data(as_text=True)
        sha256_hash_digest = hmac.new(
            bytes(os.environ.get("API_KEY_SECRET"), "utf-8"),
            msg=bytes(request_body, "utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        hash_val = "sha256=" + base64.b64encode(sha256_hash_digest).decode("utf-8")
        return hmac.compare_digest(signature, hash_val)
    return False

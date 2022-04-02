import functools
import hashlib
import base64
import hmac
import json
import os
from flask import Blueprint, request, abort
from executor import handle_events, is_valid_webhook

bp = Blueprint('webhooks', __name__)

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

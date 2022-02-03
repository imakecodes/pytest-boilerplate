import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_APP_TOKEN"]
client = WebClient(token=slack_token)

def send_message(channel, message):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]

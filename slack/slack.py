#!/usr/bin/env python3

# <hint>
# This script is a template for sending messages to Slack.
# everything that was set as a content in the notification configuration will be sent as a slack message.
# please set recipients to your Slack webhook URL. ("https://hooks.slack.com/services/...")
# read more about Slack webhook URL: https://api.slack.com/messaging/webhooks
# </hint>

import json
import http.client
import urllib.parse
import sys

# Function to send an HTTP POST request
def send_http_request(webhook_url, headers, payload):
    parsed_url = urllib.parse.urlparse(webhook_url)
    host = parsed_url.netloc
    url_path = parsed_url.path

    conn = http.client.HTTPSConnection(host)
    conn.request("POST", url_path, body=payload, headers=headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()

    return res.status, data.decode('utf-8')

# Function to send a Slack message
def send_slack_message(webhook_url, message):
    payload = json.dumps({"text": message})
    headers = {'Content-Type': 'application/json'}
    status, response_data = send_http_request(webhook_url, headers, payload)

    if status == 200:
        print(f"Successfully sent message to Slack: {message}")
    else:
        sys.stderr.write(f"Failed to send message to Slack. Status code: {status}, Reason: {response_data}")


if __name__ == "__main__":
    # Read JSON from stdin
    input_json = json.load(sys.stdin)
    message = input_json.get('data', '')
    recipients = input_json.get('recipients', [])

    if not message:
        sys.stderr.write("No 'data' field in the input JSON or it is empty.\n")
        exit(1)

    if not recipients:
        sys.stderr.write("No 'recipients' field in the input JSON or it is empty.\n")
        exit(1)

    # Send messages to Slack
    for webhook_url in recipients:
        send_slack_message(webhook_url, message)

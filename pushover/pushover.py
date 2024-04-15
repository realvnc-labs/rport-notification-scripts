#!/usr/bin/env python3

# <hint>
# This script is a template for sending messages to Pushover.
# everything that was set as a content in the notification configuration will be sent to Pushover.
# read more about Pushover user key: https://pushover.net/api#identifiers
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


# Function to send message via Pushover
def send_pushover_message(api_token, user_key, message):
    webhook_url = "https://api.pushover.net/1/messages.json"
    payload = urllib.parse.urlencode({
        "token": api_token,
        "user": user_key,
        "message": message
    })

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    status, response_data = send_http_request(webhook_url, headers, payload)

    if status == 200:
        print(f"Successfully sent message via Pushover: {message}")
    else:
        sys.stderr.write(f"Failed to send message via Pushover. Status code: {status}, Reason: {response_data}")


if __name__ == "__main__":
    # Replace with your Pushover credentials
    pushover_api_token = 'YOUR_PUSHOVER_API_TOKEN'
    pushover_user_key = 'YOUR_PUSHOVER_USER_KEY'

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

    # Send message via Pushover
    send_pushover_message(pushover_api_token, pushover_user_key, message)

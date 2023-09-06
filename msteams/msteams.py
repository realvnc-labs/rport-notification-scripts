#!/usr/bin/env python3

# <hint>
# This script is a template for sending messages to Microsoft Teams.
# everything that was set as a content in the notification configuration will be sent to Microsoft Teams.
# please set recipients to your Teams webhook URL. ("https://webhook.office.com/...")
# read more about Teams webhook URL: https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
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


# Function to send message to Microsoft Teams
def send_teams_message(webhook_url, message):
    payload = json.dumps({
        '@type': 'MessageCard',
        '@context': 'http://schema.org/extensions',
        'summary': 'RPort Notification',
        'sections': [{
            'activityTitle': 'RPort Notification',
            'text': message
        }]
    })

    headers = {'Content-Type': 'application/json'}
    status, response_data = send_http_request(webhook_url, headers, payload)

    if status == 200:
        print(f"Successfully sent message to Teams: {message}")
    else:
        sys.stderr.write(f"Failed to send message to Teams. Status code: {status}, Reason: {response_data}\n")


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

    for recipient in recipients:
        # Assuming recipients are Teams webhook URLs
        send_teams_message(recipient, message)

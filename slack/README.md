# Slack Message Sender Script Documentation

## Overview

This Python script sends messages to Slack channels using incoming webhooks. 
The script reads a JSON payload from standard input, which contains the message text and a list of
webhook URLs (recipients). The script uses Python's built-in `http.client` and `json` libraries to send the message.

## Requirements

- Python 3.x

## Usage

To use this script with RPort, copy it to the directory specified in the RPort server configuration
file under `notification_script_dir`. Then, specify this script in the RPort user interface.

## Test

To test the script manually, you can run it by piping in the JSON payload. The payload should
contain a `data` field for the message text and a `recipients` field for the Slack webhook URLs.

```bash
echo '{"data":"Your message here","recipients":["Webhook_URL_1", "Webhook_URL_2"]}' | ./slack.py
```

## Hashbang

The script includes a hashbang (`#!/usr/bin/env python3`) at the top. To make the script executable, use:

```bash
chmod +x slack.py
```

## Code Explanation

- `send_http_request(webhook_url, headers, payload)`: Sends an HTTP POST request to the specified webhook URL.
  
- `send_slack_message(webhook_url, message)`: Sends a message to a Slack channel via its webhook URL.

## External Resources

For more information on setting up incoming webhooks in Slack, see the
[Slack API Documentation](https://api.slack.com/messaging/webhooks).

## Error Handling

Errors and exceptions are printed to standard error (`stderr`). Any output on `stderr` will be
considered by the RPort server as a notification processing failure. You can view all notifications along
with your script's log messages in the RPort user interface. Output from both `stderr` and `stdout` is limited
by default to 2KB.

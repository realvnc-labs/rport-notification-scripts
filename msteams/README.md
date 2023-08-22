# Teams Message Sender Script

## Overview

This Python script sends messages to Microsoft Teams channels using incoming webhooks. The script reads a
JSON payload from standard input, which contains the message text and a list of webhook URLs
(recipients). It then sends the message to the specified Teams channels using Python's built-in
`http.client` library.

## Requirements

- Python 3.x

## Usage

To use this script with RPort, copy it to the directory specified in the RPort server configuration
file under `notification_script_dir`, and point to it in the user interface.

## Test

To test the script manually, you can run it by piping in the JSON payload. The payload should contain
a `data` field for the message and a `recipients` field for the Teams webhook URLs.

```bash
echo '{"data":"Your message here","recipients":["Webhook_URL_1", "Webhook_URL_2"]}' | ./msteams.py
```

## Hashbang

The script includes a hashbang (`#!/usr/bin/env python3`) at the top. Make the script executable with:

```bash
chmod +x msteams.py
```

## Code Explanation

- `send_http_request(webhook_url, headers, payload)`: Sends an HTTP POST request to the specified
webhook URL.
  
- `send_teams_message(webhook_url, message)`: Sends a message to a Teams channel via its webhook URL.

## External Resources

For more information on setting up incoming webhooks in Microsoft Teams, see the
[Teams Webhook API Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).

## Error Handling

Errors and exceptions are printed to standard error (`stderr`). Any output on `stderr` will be treated
by the RPort server as a failure to process the notification. You can view all notifications with your
script log messages in the RPort user interface. Output from both `stderr` and `stdout` is limited by
default to 2KB.

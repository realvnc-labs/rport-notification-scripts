# Pushover Message Sender Script

## Overview

This Python script sends notifications via the Pushover service. The script reads a JSON payload from standard input.
This payload contains the message text. 
The script uses Python's built-in `http.client` and `urllib.parse` libraries to send these messages.

## Requirements

- Python 3.x

## Usage

To use this script with RPort, copy it to the directory specified in the RPort server configuration
file under `notification_script_dir`. Then, point to it from the RPort user interface.

## Test

To manually test the script, you can run it by piping in the JSON payload.
The payload should contain a `data` field for the message text.

```bash
echo '{"data":"Your message here"}' | ./pushover.py
```

## Hashbang

The script includes a hashbang (`#!/usr/bin/env python3`) at the top. To make the script executable, use:

```bash
chmod +x pushover.py
```

## Code Explanation

- `send_http_request(webhook_url, headers, payload)`: Sends an HTTP POST request to a specified webhook URL.
  
- `send_pushover_message(api_token, user_key, message)`: Sends a message via the Pushover service using a given
- API token and user key.

## External Resources

For more information on using the Pushover API, you can check the
[Pushover API Documentation](https://pushover.net/api).

## Error Handling

Errors and exceptions are printed to standard error (`stderr`). Any output on `stderr` will be considered by the RPort
server as a notification processing failure.
You can view all notifications along with your script's log messages in the RPort user interface.
Output from both `stderr` and `stdout` is limited by default to 2KB.
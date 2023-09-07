# Syslog Message Logger Script

## Overview

This Python script logs messages to the system's syslog using the Python built-in `syslog` library.
The script reads a JSON payload from standard input, which should contain a `data` field for the message
text. The script logs this message to the syslog with a default priority of `LOG_INFO`.

## Requirements

- Python 3.x
- A Unix-like operating system with syslog

## Usage

To use this script with RPort, copy it to the directory specified in the RPort server configuration
file under `notification_script_dir`, and then point to it in the user interface.

## Test

To test the script manually, you can run it by piping in the JSON payload. The payload should contain
a `data` field for the message.

```bash
echo '{"data":"Your log message here"}' | ./syslog_logger.py
```

## Hashbang

The script includes a hashbang (`#!/usr/bin/env python3`) at the top. Make the script executable with:

```bash
chmod +x syslog_logger.py
```

## Code Explanation

- `log_to_syslog(message, priority=syslog.LOG_INFO)`: Logs a message to the system's syslog.
  It accepts two parameters:
  - `message`: The message to log.
  - `priority`: The priority of the message, default is `syslog.LOG_INFO`.

## External Resources

For more information on syslog in Python, see the 
[`syslog` Python Documentation](https://docs.python.org/3/library/syslog.html).

## Error Handling

The script does not currently implement explicit error handling. Syslog will typically handle errors
internally. Any output on `stderr` will be treated by the RPort server as a failure to process the
notification. You can view all notifications with your script log messages in the RPort user interface.
Output from both `stderr` and `stdout` is limited by default to 2KB.

## Customizing Priority

You can extend this script to accept different priorities by modifying the `priority` parameter in the
`log_to_syslog` function. Check the Python `syslog` documentation for the list of available priorities.
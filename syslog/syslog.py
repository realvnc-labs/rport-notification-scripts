#!/usr/bin/env python3

import sys
import json
import syslog


def log_to_syslog(message, priority=syslog.LOG_INFO):
    syslog.openlog(ident="RPort server", logoption=syslog.LOG_PID, facility=syslog.LOG_USER)
    syslog.syslog(priority, message)
    syslog.closelog()


if __name__ == "__main__":
    input_json = json.load(sys.stdin)
    message = input_json.get('data', '')
    log_to_syslog(message)

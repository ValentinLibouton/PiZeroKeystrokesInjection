#!/usr/bin/env python3
# Author:   Valentin Libouton
# Contact:  pizerokeystrokesinjection.g1uw8@8shield.net
# Github:   https://github.com/ValentinLibouton
# Project:  PiZeroKeystrokesInjection
# V1

"""
    For development only. Allows you to stop a keystroke that doesn't stop
    Execute in terminal:
        python3 release_kb.py
"""

null_char = chr(0)
report = null_char * 8
with open('/dev/hidg0', 'rb+') as fd:
    fd.write(report.encode())

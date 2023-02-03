#!/bin/sh
# Author:   Valentin Libouton
# Contact:  pizerokeystrokesinjection.g1uw8@8shield.net
# Github:   https://github.com/ValentinLibouton
# Project:  PiZeroKeystrokesInjection
# Version:	V1
# Date:		03/02/2023

#########################################################################
#	This file is executed automatically when the raspberry pi starts	    #
#																		                                    #
#########################################################################
# 1 - Copy this file in /home/pi directory                              #
# 2 - Copy autostart.service in /lib/systemd/system/ directory          #
# 3 - sudo chmod +x /home/pi/autostart.sh                               #
# 4 - sudo chmod 644 /lib/systemd/system/autostart.service              #
# 5 - sudo systemctl daemon-reload                                      #
# 6 - sudo systemctl enable autostart.service                           #
# 7 - sudo reboot                                                       #
#                                                                       #
#########################################################################

echo "Log - PiZeroKeystrokesInjection: systemctl autostart.service : started"
echo "Log - PiZeroKeystrokesInjection: /home/pi/autostart.sh : started"
echo "Log - PiZeroKeystrokesInjection: run 'python3 /home/pi/run_keystrokes.py'"

python3 /home/pi/run_keystrokes.py

# mv /home/pi/command_file.txt /home/pi/command_file.txt.bak

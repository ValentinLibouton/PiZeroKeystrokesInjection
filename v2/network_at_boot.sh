#!/bin/sh
# Author:   Valentin Libouton
# Contact:  pizerokeystrokesinjection.g1uw8@8shield.net
# Github:   https://github.com/ValentinLibouton
# Project:  PiZeroKeystrokesInjection
# Version:	V2
# Date:		02/04/2023


# Boot without waiting for network connection
sudo raspi-config nonint do_boot_wait 0

# Boot after waiting for network connection
sudo raspi-config nonint do_boot_wait 1
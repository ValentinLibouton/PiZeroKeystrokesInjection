# PiZeroKeystrokesInjection V2

## Ideas

- [Network At Boot](#network-at-boot)
- [KEYFILE command](#keyfile-command)
- [Simplify the code](#simplify-the-code)
- [Installer](#installer)
- [HID Descriptor](#hid-descriptor)


## Network At Boot
Easily enable or disable the boot wait from the autostart.sh file

## `KEYFILE` command
1. Creation of a **kbkey_directory** folder as a library of pre-registered scripts
2. Use of the **.kbkey** extension to differentiate `KEYFILE` from the use of the already existing `WRITE` command
3. Example: see line 6 in the example below
```code
DELAY 3
# This is a comment
REPLAY 2 6
CTRL_LEFT s
CTRL_LEFT ALT_LEFT t
KEYFILE configure_network.kbkey
CTRL_LEFT ALT_LEFT DELETE
ALT_LEFT TAB
```

## Simplify the code
- Some testing currently in progress in the v2 folder
- Rename **command_file.txt** to **inject.kbkey**

## Installer
- Verification if the files are present at startup, if not installation of these. Also allows the installation of the system.
- If there is internet, allow the update from github repository
- Uninstaller

## HID Descriptor
- 0x05 : Utilisation des codes de page standard
- 0x01 : Utilisation de la page de codes générique du bureau
- 0x09, 0x06 : Utilisation de la commande clavier
- 0xA1, 0x01 : Utilisation de la commande de rapport
- 0x05, 0x07 : Utilisation de la page de codes des touches
- 0x19, 0xE0 : Utilisation du code de la première touche
- 0x29, 0xE7 : Utilisation du code de la dernière touche
- 0x15, 0x00 : Utilisation de la valeur minimale pour les données d'entrée
- 0x25, 0x01 : Utilisation de la valeur maximale pour les données d'entrée
- 0x75, 0x01 : Utilisation d'un octet de données pour représenter chaque touche
- 0x95, 0x08 : Utilisation de 8 bits de données pour chaque touche
- 0x81, 0x02 : Utilisation de l'ID du rapport 2
- 0x95, 0x01 : Utilisation d'un bit de remplissage
- 0x75, 0x08 : Utilisation d'un octet de remplissage
- 0x81, 0x03 : Utilisation de l'ID du rapport 3
- 0x95, 0x05 : Utilisation de 5 bits de remplissage
- 0x75, 0x01 : Utilisation d'un bit de données pour chaque touche de fonction
- 0x05, 0x08 : Utilisation de la page de codes des LEDs
- 0x19, 0x01 : Utilisation du code de la première LED
- 0x29, 0x05 : Utilisation du code de la dernière LED
- 0x91, 0x02 : Utilisation de l'ID du rapport 2
- 0x95, 0x01 : Utilisation d'un bit de remplissage
- 0x75, 0x03 : Utilisation de 3 bits de données pour les LED
- 0x91, 0x03 : Utilisation de l'ID du rapport 3
- 0x95, 0x06 : Utilisation de 6 bits de remplissage
- 0x75, 0x08 : Utilisation d'un octet de remplissage
- 0x15, 0x00 : Utilisation de la valeur minimale pour les données de sortie
- 0x25, 0x65 : Utilisation de la valeur maximale pour les données de sortie
- 0x05, 0x07 : Utilisation de la page de codes des touches
- 0x19, 0x00 : Utilisation du code de la première touche
- 0x29, 0x65 : Utilisation du code de la dernière touche
- 0x81, 0x00 : Utilisation de l'ID du rapport 0
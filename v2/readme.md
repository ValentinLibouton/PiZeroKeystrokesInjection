# PiZeroKeystrokesInjection V2

## Ideas

- Embed the boot wait command in the autostrat.sh file
- Simplify the code

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
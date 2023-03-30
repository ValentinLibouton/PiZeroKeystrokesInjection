import struct
import keyboard
"""
    Ce fichier à pour but de faire des tests de
    différentes idées de codes en vue de la V2.
"""


def hex_string_to_key(hex_string):
    """
    Convertit une chaîne de caractères représentant une clé en
    format hexadécimal en une chaîne de caractères représentant
    la touche correspondante.

    :param hex_string: une chaîne de caractères en format hexadécimal représentant une clé.
    :return: une chaîne de caractères représentant la touche correspondante.
    """
    hex_string_without_nulls = hex_string.replace('\x00', '')
    values = tuple(int(hex_string_without_nulls[i:i + 2], 16) for i in range(0, len(hex_string_without_nulls), 2))
    binary_string = struct.pack('B', *values)
    char_string = binary_string.decode('ascii')
    return char_string


def chr_string_to_key(chr_string):
    """
    Convertit une chaîne de caractères en une chaîne de caractères représentant une touche clavier.

    :param chr_string: la chaîne de caractères à convertir
    :return: une chaîne de caractères représentant une touche clavier
    """
    values = tuple(ord(c) for c in chr_string)
    binary_string = struct.pack('{}B'.format(len(values)), *values)
    char_string = binary_string.decode('ascii')
    return char_string


def test_de_base():
    """
    :return: hexadecimal representation of the 'm' key
    """
    print("Test: 0")
    char_string = chr(0)+chr(0)+chr(51)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)
    key = chr_string_to_key(char_string)

    print(repr(key))  # affiche "\x00\x003\x00\x00\x00\x00\x00"
    print(key)  # affiche "  3     "
    return key


def test_1():
    print("Test: 1")
    values = (0, 0, 51, 0, 0, 0, 0, 0)
    binary_string = struct.pack('8B', *values)
    char_string = binary_string.decode('ascii')
    print(repr(char_string))  # affiche "\x00\x003\x00\x00\x00\x00\x00"


def test_2():
    print("Test: 2")
    values = (0, 0, 51, 0, 0, 0, 0, 0)
    char_string = ''.join(chr(v) for v in values)
    print(repr(char_string))  # affiche "\x00\x003\x00\x00\x00\x00\x00"


def test_3():
    """
    Ce test doit être exécuté en tant que root
    `sudo python3 v2/keystrokes_test.py`
    :return:
    """
    print("Test: 2")
    print("Pressez la touche m du clavier...")
    # Presser la touche "m" du clavier belge
    keyboard.press_and_release('m')

    # Vérifier si la touche "m" est actuellement enfoncée
    while True:
        if keyboard.is_pressed('m'):
            print('La touche "m" est enfoncée')
            break


def test_4():
    print("Test: 4")
    hex_string = '\x00\x003\x00\x00\x00\x00\x00'
    key = hex_string_to_key(hex_string)
    print(repr(key))  # affiche '\x03'
    print(key)  # affiche <0x03>
    return key


test_de_base()
test_1()
test_2()
# test_3()
test_4()

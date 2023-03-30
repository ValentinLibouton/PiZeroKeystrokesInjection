#!/usr/bin/env python3
# Author:   Valentin Libouton
# Contact:  pizerokeystrokesinjection.g1uw8@8shield.net
# Github:   https://github.com/ValentinLibouton
# Project:  PiZeroKeystrokesInjection
# Version:  V3
# Date:     03/02/2023
import struct
import conversion
import time
write_speed = 0.03
global replay_list
replay_list = []


def check_file(filename):
    try:
        with open(filename, "r") as f:

            if len(f.read()) == 0:
                print("File empty")
                return False
            else:
                print("File not empty")
                return True

    except IOError:
        print("Check_file: File doesn't exist")
        return False
    except:
        print("Check_file: Unknown error")
        return False


def read_file(filename):
    """
    :param filename: User commands text file
    :return: False only if error (not used)
    """
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                main_list(line)
    except IOError:
        print("read_file: File doesn't exist")
        return False
    except:
        print("read_file: Unknown error")
        return False


def main_list(line):
    """
    :param line: line of text file
    :return:
    """
    global replay_list
    if line == "\n":
        print("Blank line")
    elif line.split()[0] == "STRING":
        string_mode(line)
    elif line.split()[0] == "DELAY":
        delay_mode(line)
    elif line.split()[0] == "WRITE":
        # Not implemented
        write_mode(line)
    elif line.split()[0] == "#":
        comment_mode(line)
    elif line.split()[0] == "REPLAY":
        replay_mode(line)
    else:
        command_mode(line)
    replay_list.append(line)


def string_mode(line):
    """
    :param line: line of text file
    :return:
    """
    string = str(line[len(line.split()[0]) + 1:])  # take string after "STRING "
    print("Write: ", string)
    for char in string:
        time.sleep(write_speed)
        for key, value in conversion.belgian_keyboard.items():
            if char == key:
                unicode_list = build_unicode_byte(value)
                # print("Type de la liste: ", type(unicode_list))
                for i in range(len(unicode_list)):
                    write_report(unicode_list[i])


def delay_mode(line):
    """
    :param line: line of text file
    :return:
    """
    delay_time = int(line[len(line.split()[0]) + 1:])  # take time after "DELAY "
    print("Delay time: ", delay_time)
    time.sleep(delay_time)


def write_mode(line):
    """This mode allows you to take a file from the Pi Zero and write its
    full contents to the machine to which the Pi Zero is connected.
    This mode is faster to send complete files
    :param line: line of text file
    :return:
    """
    aux_filename = line[len(line.split()[0]) + 1:]  # take file after "WRITE"
    print("Beginning of writing: ", aux_filename)
    if check_file(aux_filename):
        try:
            with open(aux_filename, "r") as aux_f:
                string = ""
                for line in aux_f.readlines():
                    string = line
                    print("writing of: ",string)
                    for index in range(len(string)):
                        time.sleep(write_speed)
                        for key, value in conversion.belgian_keyboard.items():
                            if string[index] == key:
                                unicode_list = build_unicode_byte(value)
                                for i in range(len(unicode_list)):
                                    write_report(unicode_list[i])
                    # ENTER key for newline
                    write_report(chr(0) + chr(0) + chr(40) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0))
                    # Release key for newline
                    write_report(chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0))
                print("End of writing: ", aux_filename)
        except IOError:
            print("write mode: File doesn't exist")
            return False
        except:
            print("write mode: Unknown error")
            return False


def comment_mode(comment):
    """
    Allows the user to comment on their text file
    Ex: # This is a comment
    Can be used as log by SSH
    :param comment: line of text file
    :return:
    """
    print("Comment: ", comment)


def replay_mode(line):
    """
    :param line: line of text file
                Ex: REPLAY 2 6 : replay the last 6 lines twice
    :return:
    """
    try:
        global replay_list
        if len(line.split()) == 1:
            print("Missing args in REPLAY mode")
        elif len(line.split()) == 2:
            occurence = line.split()[1]
            numbs_lines = 1
        elif len(line.split()) >= 3:
            occurence = line.split()[1]
            numbs_lines = line.split()[2]

        if len(line.split()) > 3:
            print("Pay attention! - Too many args in REPEAT mode")
        occurence = int(occurence)
        numbs_lines = int(numbs_lines)
        start_line = len(replay_list) - numbs_lines
        if start_line < 0:
            start_line = 0
        end_line = len(replay_list)
        for _ in range(occurence):
            for index in range(start_line, end_line):
                main_list(replay_list[index])
    except:
        print("Replay mode: Error - Only integer value after REPLAY command. Ex. REPLAY 2 6")


def command_mode(line):
    """
    For command lines like CTRL_LEFT, WIN, TAB, INSERT, ENTER, BACK
    :param line: line of text file
    :return:
    """
    commands = line.split()
    byte_tuple = (0, 0, 0, 0, 0, 0, 0, 0)
    for command in commands:
        print("Command: ", command)
        for key, value in conversion.belgian_keyboard.items():
            if command == key:
                byte_tuple = merge_tuples(byte_tuple, value)
                unicode_list = build_unicode_byte(byte_tuple)
    for i in range(len(unicode_list)):
        write_report(unicode_list[i])


def merge_tuples(tuple1, tuple2):
    """
    This function allows to merge in a tuple a series of keys such
    as CTRL_LEFT ALT_LEFT DELETE or ALT_LEFT TAB or WIN PAUSE
    :param tuple1: len == 8
    :param tuple2: len == 8
    :return: result type(tuple) len == 8
    """
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    if len(tuple1) == len(tuple2):
        for index in range(len(tuple1)):
            result[index] += tuple1[index] + tuple2[index]
        return tuple(result)
    else:
        print("Error len() tuple")
        return False


def build_unicode_byte(tuples):
    """
    This function generates the list of keys for the current command
    Ex:
        if case:
            for "ä" you have to press the key ¨ and a
            for "^" you have to press twice
        else case:
            for "a" you must press the key once
            for "CTRL_LEFT ALT_LEFT DELETE" this kind of key combos arrive in a single tuple
            and are assembled beforehand by the function merge_tuples(tuple1, tuple2)

    :param tuples: tuple or tuple in tuples
    :return: list of unicode_byte type(list)
    """
    null_char = chr(0)
    release_keys = ""
    release_keys += null_char * 8
    unicode_byte = ""
    result = []
    if type(tuples[0]) is tuple:
        # accented keys and double keystrokes
        for tup in tuples:
            unicode_byte = ""
            for elem in tup:
                unicode_byte += chr(elem)
            result.append(unicode_byte)
    else:
        # others keys
        for elem in tuples:
            unicode_byte += chr(elem)
        result.append(unicode_byte)
    result.append(release_keys)
    # print("Ready to send this list of bytes: ", result)
    return result


def write_report(report):
    """
    This function is the final function that sends the keyboard command to the connected machine
    :param report: keystroke in unicode format in a variable of type string
    :return:
    """
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


if __name__ == "__main__":
    filename = "command_file.txt"
    if check_file(filename):
        read_file(filename)

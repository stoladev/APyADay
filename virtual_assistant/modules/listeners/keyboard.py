from utils import debug
from pynput.keyboard import Key, Controller


def keyboard_input():
    debug.log("Listening for keyboard input...")
    command = input("Command: ")

    if command is not None:
        return command

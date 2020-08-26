from modules.handlers import command_handler
from utils import debug


def keyboard_input():
    debug.log("Listening for keyboard input...")
    command = input("Command: ")

    command_handler.check_cmnd("amy " + command)

    return keyboard_input()

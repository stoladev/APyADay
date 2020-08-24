from commands import open_command
from utils import debug


def main(command):

    if "amy" in command:
        debug.log("Command recognized. Captured speech: " + command + "\n")
    else:
        debug.log("Command NOT recognized. Captured speech: " + command + "\n")
        return False

    if open_command.check(command):
        return True

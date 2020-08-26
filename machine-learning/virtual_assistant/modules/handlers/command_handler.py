from playsound import playsound
from commands import open_command
from modules.handlers import thread_handler
from utils import debug


def check_cmnd(command):
    """
    Checks the commands that are registered after grabbing input once the hotkey is pressed.

    Procedure:
    Searches through the command using regex.
    Runs through commands that are currently limited to if statements.

    Still needed:
    Transfer checks to use machine learning.
    Sync data between app and cloud.
    """

    if "amy" in command:
        debug.log("Command RECOGNIZED.")
        debug.log("Command: " + command + "\n")
    else:
        debug.log("Command NOT RECOGNIZED.")
        debug.log("Command: " + command + "\n")
        return

    if open_command.check(command):
        return
    elif "exit" in command:
        thread_handler.stop_threads()
    else:
        playsound("audio/cmnd_not_recognized_audio.mp3")

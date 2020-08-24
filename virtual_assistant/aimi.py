from modules import responder
from modules import listener
from commands import command_handler
from utils import debug
import tkinter as tk

window = tk.Tk()

debug.activated = True

responder.respond("Hello! What can I do for you?")


def assistant(command):
    """
    Checks the commands that are registered after grabbing input once the hotkey is pressed.
    
    Procedure:
    Searches through the command using regex.
    Runs through commands that are currently limited to if statements. 

    Still needed:
    Transfer checks to use machine learning.
    Sync data between app and cloud.
    """

    if command_handler.main(command):
        return

    else:
        responder.respond("Sorry, I'm not sure what you'd like me to do.")


while True:
    assistant(listener.listen())

from modules import responder
from modules import listener

import re
import webbrowser


def assistant(command):
    """
    Checks the commands that are registered after grabbing input once the hotkey is pressed.
    
    Procedure:
    Searches through the command using regex.
    Runs through commands that are currently limited to if statements. 

    ToDo:
    Transfer checks to use machine learning.
    """

    if "open" in command:

        reg_ex = re.search("open (.+)", command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = "https://www." + domain
            webbrowser.open(url)

        else:
            responder.respond("Sorry, I'm not sure what you'd like me to do.")


while True:
    assistant(listener.listen())

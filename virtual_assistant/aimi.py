from playsound import playsound

from commands.command_handler import check_cmnd
from modules import responder
from modules.gui.main_gui import root
from modules.listeners import listener
from utils import debug


debug.activated = True

playsound("audio/start_audio.mp3")
root.mainloop()


# while True:
# check_cmnd(listener.listen())

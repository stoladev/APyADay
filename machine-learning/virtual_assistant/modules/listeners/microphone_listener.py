import speech_recognition as sr

from modules.handlers import command_handler
from utils import debug


def microphone_input():
    """
    Uses speech recognition to translate audio picked up by the microphone into
    text, which it then returns.

    Procedure:
    Listens to the microphone.
    Marks the end of the command using a pause threshold of 1 second.
    Listens for ambient noise, preventing any listening of commands during that period.
    Tries to convert the audio into text, printing it to console.
    If the try is successful, returns the command string.
    """

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        debug.log("Setting pause threshold...")
        listener.pause_threshold = 1

        debug.log("Adjusting for ambient noise...")
        listener.adjust_for_ambient_noise(source, duration=1)

        debug.log("Listening for audio...")
        audio = listener.listen(source)

    try:
        debug.log("Recognizing audio through Google...")
        command = listener.recognize_google(audio).lower()

    except sr.UnknownValueError:
        debug.log("Exception: no translatable audio captured. Restarting capture...")
        return microphone_input()

    command_handler.check_cmnd(command)
    return microphone_input()

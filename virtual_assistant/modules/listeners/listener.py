
from modules.listeners.keyboard import keyboard_input
from modules.listeners.microphone import microphone_input

debug_mode = True


def listen():
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

    keyboard_input()
    microphone_input()

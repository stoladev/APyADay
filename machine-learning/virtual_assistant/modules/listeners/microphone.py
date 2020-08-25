import speech_recognition as sr
from utils import debug


def microphone_input():
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
        command = microphone_input()

    return command

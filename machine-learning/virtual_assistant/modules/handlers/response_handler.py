import gtts
import os
import errno
from playsound import playsound

from utils import debug


def respond(text):
    """
    Speaks to the user with audio using the passed in text.
    
    Procedure:
    Creates an audio folder for all audio clips if one hasn't been created yet.
    Uses TTS to create an .mp3 file.
    Plays the .mp3 file using playsound.
    Removes the file to prevent permission issues when overwriting.
    """

    for _ in text.splitlines():

        try:
            os.makedirs("audio")
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

        debug.log("Grabbing and saving audio...")
        text_to_speech = gtts.gTTS(text=text, lang="en")
        text_to_speech.save("audio/tts_audio.mp3")

        debug.log("Command:")
        debug.log(text)
        playsound("audio/tts_audio.mp3", True)
        os.remove("audio/tts_audio.mp3")

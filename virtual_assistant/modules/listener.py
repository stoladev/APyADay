import speech_recognition as sr

listening = False


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

    listener = sr.Recognizer()
    global listening

    with sr.Microphone() as source:

        if not listening:
            print("Listening...")

        listening = True
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source, duration=1)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio).lower()

        # if "amy" in command:
        print("Command recognized. Captured speech: " + command + "\n")
        listening = False
        # else:
        #     print("Command NOT recognized. Captured speech: " + command + "\n")
        #     command = listen()
        #     listening = False

    except sr.UnknownValueError:
        print("No speech captured. Restarting capture...")
        command = listen()

    return command
